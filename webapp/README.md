# IMEI Research Desk Web App

Serve the repository root with `python -m http.server 8000` and open `http://127.0.0.1:8000/webapp/`. The resource catalog loads from `../data/resources.json`; the browser validator works locally and does not upload input.

Installable/offline behavior requires localhost or HTTPS. The Python CLI is available from the repository root: `python -m imei_research.cli --imei 490154203237518`. See `../FULL_PROJECT.md` and `../docs/repository-review.md` for project scope and resource review.

This is a research and validation UI, not an IMEI changer. It does not generate, rewrite, clone or track identifiers.
