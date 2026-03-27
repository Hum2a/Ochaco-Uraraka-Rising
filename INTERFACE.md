# Web modding (schema 1)

Ann Takamaki–style **bucket CSS**: one global stylesheet plus `sites-01` … `sites-06` scoped by URL patterns in `manifest.json`.

- **Global:** `webmodding/ochaco-uraraka.css` matches all `https://` and `http://` pages for scrollbars, links, and atmospheric pink/brown mist.
- **Buckets:** site-specific tweaks without loading every rule on every page.

Shaders in `shader/` are not wired in `manifest.json` by default; add a `shaders` block if you want GX shader entries.
