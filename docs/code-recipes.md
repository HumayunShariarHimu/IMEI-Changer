# Code recipes and usage

## Python Luhn validator

The implementation lives in `imei_research/validator.py` and is independently tested. Use it with synthetic values in tests:

```python
from imei_research.validator import validate_imei
result = validate_imei("490154203237518")
print(result.valid_format_and_checksum)
```

## CLI batch processing

Create a local UTF-8 text file with one candidate value per line, then run:

```bash
python -m imei_research.cli --batch imeis.txt --json
python -m imei_research.cli --batch imeis.txt --csv-out results.csv
```

Do not commit real device identifiers or put them in public logs.

## JavaScript check digit

The browser implementation is in `webapp/app.js`. It removes separators, checks the 15-digit length, calculates the Luhn check digit from the first 14 digits, and reports whether the supplied final digit matches. It does not call an external API.

## PHP reference implementation

```php
function validImei(string $value): bool {
    $digits = preg_replace('/[^0-9]/', '', $value);
    if (strlen($digits) !== 15) return false;
    $sum = 0;
    for ($i = 0; $i < 14; $i++) {
        $n = (int)$digits[$i];
        if ($i % 2 === 1) { $n *= 2; if ($n > 9) $n -= 9; }
        $sum += $n;
    }
    return ((10 - ($sum % 10)) % 10) === (int)$digits[14];
}
```

## Read-only Android diagnostics

`scripts/diagnostics.sh` uses ADB to report connected devices, manufacturer, model and Android version. It intentionally does not query IMEI, SIM data or private partitions. Modern Android restricts persistent identifier access; a web page cannot directly read the host phone's IMEI.

## Local JSON API

Run `python -m imei_research.server --host 127.0.0.1 --port 8765`. Send JSON to `POST /api/validate` with `{"imei":"490154203237518"}`, or to `POST /api/batch` with `{"imeis":["490154203237518"]}`. This is a development server; keep it on loopback and do not expose it publicly.

## Not included

No identifier generation, NVRAM rewriting, live patching, blacklist bypass or device tracking is included. Third-party write-capable scripts remain linked as research references only.
