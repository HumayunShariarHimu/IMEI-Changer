"""Loopback-only local JSON API and static file server."""
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from urllib.parse import urlparse
import argparse,json
from .validator import validate_imei
ROOT=Path(__file__).resolve().parent.parent
class Handler(SimpleHTTPRequestHandler):
 def __init__(self,*args,**kwargs): super().__init__(*args,directory=str(ROOT),**kwargs)
 def end_headers(self):
  self.send_header('X-Content-Type-Options','nosniff');self.send_header('Referrer-Policy','no-referrer');self.send_header('Cache-Control','no-store');super().end_headers()
 def do_POST(self):
  path=urlparse(self.path).path
  if path not in ('/api/validate','/api/batch'): self.send_error(404);return
  try:
   size=int(self.headers.get('Content-Length','0'))
   if size>64000: self.send_error(413);return
   body=json.loads(self.rfile.read(size) or b'{}')
   if path=='/api/validate': result=validate_imei(body.get('imei','')).to_dict()
   else:
    values=body.get('imeis',[])
    if not isinstance(values,list) or len(values)>500: self.send_error(400,'imeis must be a list of at most 500 values');return
    result=[validate_imei(v).to_dict() for v in values]
   data=json.dumps(result,ensure_ascii=False).encode();self.send_response(200);self.send_header('Content-Type','application/json; charset=utf-8');self.send_header('Content-Length',str(len(data)));self.end_headers();self.wfile.write(data)
  except (ValueError,json.JSONDecodeError): self.send_error(400,'Invalid JSON')
def main():
 p=argparse.ArgumentParser();p.add_argument('--host',default='127.0.0.1');p.add_argument('--port',type=int,default=8765);a=p.parse_args();print(f'Local API at http://{a.host}:{a.port}');ThreadingHTTPServer((a.host,a.port),Handler).serve_forever()
if __name__=='__main__':main()
