# Repository review ledger

## Primary repository

Repository: https://github.com/HumayunShariarHimu/IMEI-Changer

The connected GitHub history query returned four commits on `main`: `fe76b82` Initial commit; `51b533d` Update README; `216c73b` Update README; `5400b5a` Fix README formatting. The visible branch search surfaced only `main`, and the returned commit search did not show historical Python files. This does not prove no older copy exists: check forks, local backups, old ZIPs and related repositories before concluding the code is unrecoverable.

## License mismatch

The repository root `LICENSE` is Apache License 2.0, but the README includes an MIT license statement. This is a material conflict. Do not change the license or copy third-party source until the intended project license is clarified and README/metadata are made consistent.

## References reviewed

- `Untouchable17/Android-IMEI-Changer`: inspect current tree, branch and license before adapting.
- `flipphoneguy/mtk-imei-switcheroo-app`: README describes rooted MTK IMEI and MAC NVRAM operations, history, backup/restore and a build script; GitHub search shows GPL-3.0. No write path is embedded here.
- `viki3d/change-imei-android`: APK and README are visible; reviewed releases page showed no releases. APK provenance/build reproducibility needs review.
- `alltechdev/mtk-imei-switcheroo`: Python CLI, NVRAM docs, ADB live patch scripts and device validation docs. Listed as upstream research, not vendored.
- `D3crypT0r/IMEI-Find`: Python/Qt/ADB tool cited by primary guide; license needs verification.
- `JonnyBytesMe/imei-validator`: validation reference; check upstream license before reuse.
- `bstein/py-imei-generator`: generator reference; this project intentionally does not generate identifiers.
- `github.com/topics/imei-masker`: discovery page only; not an endorsement.

## New implementation

`imei_research/validator.py` is an independent local 15-digit/Luhn implementation. `imei_research/cli.py` supports single and batch JSON/CSV validation. `data/resources.json` catalogs references with role, license status and review notes. Tests use synthetic examples.

## Boundaries

No IMEI generation, rewriting, cloning, tracking, blacklist evasion, NVRAM/EFS/partition writing or automated private identifier extraction. External links are not audited or endorsed by inclusion.
