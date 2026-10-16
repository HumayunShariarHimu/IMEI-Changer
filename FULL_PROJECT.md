# IMEI Research Desk — full project entry point

The full project combines the existing Bengali research guide with a responsive web workspace, Python validation utilities, batch reports, a resource catalog, tests and repository review notes.

## Quick start

Static web app: serve the repository root with `python -m http.server 8000`, then open `/webapp/` if using the webapp folder. Python validator: `python -m imei_research.cli --imei 490154203237518`. Tests: `python -m unittest discover -s tests -v`.

See `docs/repository-review.md` for the per-repository audit ledger and `data/resources.json` for searchable metadata intended for the UI.

## License conflict requiring owner decision

The root LICENSE is Apache-2.0 while the existing README says MIT. Do not overwrite either until the intended license is confirmed. Each third-party repository has its own license and must be reviewed separately.

## Safety scope

This is for format validation, research documentation and authorized read-only diagnostics. It does not change/generate/clone IMEIs or write NVRAM/EFS/partitions.
