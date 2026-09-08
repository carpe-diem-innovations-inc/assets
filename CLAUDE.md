> ‼‼ ORPHANED AS A HOST — 2026-09-07
>
> **Nothing is served from this repository any more.**
> `assets.carpedieminnovationsinc.com` was a Cloudflare-proxied CNAME to GitHub Pages; it is
> now a **Worker custom domain** on `cdi-site`, and the signature assets are served from
> `cdi-site/src/sig/`.
>
> ‼ **THE `CNAME` FILE IS THEREFORE INERT.** It still reads
> `assets.carpedieminnovationsinc.com`, which now looks like a claim to be the host and is
> not one. **It is left in place deliberately** — deleting it would make a GitHub Pages
> fallback harder to restore in a hurry, and this is the rollback path if the Worker ever
> has to be undone.
>
> ‼ **IF `sig/` HERE EVER DIVERGES FROM `cdi-site/src/sig/`, THE OTHER REPO IS WHAT THE
> WORLD SEES.** The three PNGs were byte-identical at the cutover and were verified as such
> before and after.

# CLAUDE.md
version: 1.0
role: code-surface project layer — assets (CDI brand-asset host)
deploy: auto-loaded (Code walks cwd upward)
status: active

Inherits the account-level canon (auto-composed as Code walks cwd upward). Adds repo
specifics only — nothing restated.

- **Owner:** carpe-diem-innovations-inc (admin). **Surface:** code.
- **Role:** static host for deployed CDI brand assets (GitHub Pages; `CNAME` →
  assets.carpedieminnovationsinc.com). Serves `sig\`; not a build project.
- **Upstream:** receives working variants from `export-assets`; masters originate in the
  `cdi-assets` chat/cowork project (`_claude\projects\cdi-assets\`).
- **Rule:** deployed files are outputs — do not hand-edit; regenerate upstream and redeploy.
