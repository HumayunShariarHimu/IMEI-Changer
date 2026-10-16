"""Local single/batch IMEI format validation CLI."""
import argparse,csv,json,sys
from pathlib import Path
from .validator import validate_imei

def main(argv=None):
 p=argparse.ArgumentParser(description="Local 15-digit/Luhn validator")
 g=p.add_mutually_exclusive_group(required=True);g.add_argument('--imei');g.add_argument('--batch',type=Path)
 p.add_argument('--json',action='store_true');p.add_argument('--csv-out',type=Path);a=p.parse_args(argv)
 values=[a.imei] if a.imei is not None else a.batch.read_text(encoding='utf-8').splitlines()
 rows=[validate_imei(v).to_dict() for v in values if str(v).strip()]
 if a.csv_out:
  with a.csv_out.open('w',newline='',encoding='utf-8') as f:
   w=csv.DictWriter(f,fieldnames=list(rows[0]) if rows else ['input_value']);w.writeheader();w.writerows(rows)
 if a.json: print(json.dumps(rows,ensure_ascii=False,indent=2))
 else:
  for r in rows: print(f"{'PASS' if r['valid_format_and_checksum'] else 'CHECK'}: {r['normalized']} | digits={r['digit_count']} | Luhn={r['luhn_valid']}")
 return 0 if rows and all(r['valid_format_and_checksum'] for r in rows) else 1
if __name__=='__main__': sys.exit(main())
