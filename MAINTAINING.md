# Maintaining the prompt library

`catalog/prompts.json` is the content source. Each prompt has a stable ID, task category, source IDs, wording, and `in_pdf` flag. The 54 core prompts appear in all formats; the two Acquisition.gov examples have `in_pdf: false` by design.

```sh
python -m pip install -r requirements-build.txt
python tools/build.py
python tools/build.py --check
python tools/verify.py
```

Commit the catalog and generated README, `docs/` PDF, and `site/` together. The PDF is built reproducibly with ReportLab's standard fonts; no browser or font download is required. The printed edition is a content date, not an assurance of complete live testing.

To update the public website, first commit/push this repository, then run `python tools/sync_public.py --prompts-repo /path/to/federal-contracting-prompts` in `1102tools-deploy`. Commit its public snapshot and `catalog-source.json`, validate it, and deploy `_site/` with Wrangler. The sync script records the exact source commit and catalog hash. Do not edit generated prompt text in the website repository.

Historical PDFs may contain superseded prompts and retired setup links. They are not current install instructions. Server setup and testing evidence live in the MCP repository's individual server directories.
