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

# assets

[![verify](https://github.com/carpe-diem-innovations-inc/assets/actions/workflows/verify.yml/badge.svg)](https://github.com/carpe-diem-innovations-inc/assets/actions/workflows/verify.yml)

Brand assets for [Carpe Diem Innovations Inc.](https://github.com/carpe-diem-innovations-inc),
served over GitHub Pages at `assets.carpedieminnovationsinc.com`.

## ‼ This repository is public, but nothing here is licensed

**These assets are proprietary. All rights reserved.** Public visibility exists for one
reason: GitHub Pages cannot serve files from a private repository. It is a hosting
requirement, not an invitation.

You may **not** reuse, redistribute or modify the contents — logos, signature marks, or
anything else here. See [`NOTICE`](NOTICE).

There is deliberately **no `LICENSE` file**, and its absence is load-bearing rather than an
oversight. Under copyright, no licence means no permission; adding a permissive one would give
away a company's identity marks. The verification below actively fails if a `LICENSE` file
appears, so nobody can add one by reflex while tidying up.

## Verification

Every push is verified before it lands. There is no application here, so "works" means the
things this repo exists to serve are actually servable.

| stage | what it proves | where |
|---|---|---|
| **works** | every image is a real image of its claimed format and non-empty; `CNAME` still carries a hostname; `NOTICE` still reserves all rights; no `LICENSE` has appeared | locally, then again in CI |
| **safe** | no committed secrets, a clean tree, this README documenting verification | locally |
| **elsewhere** | the same checks pass on a clean runner | GitHub Actions, `ubuntu-latest` |

```bash
python scripts/verify_assets.py
```

Standard library only, so it runs anywhere with no install step.

The checker lives in `scripts/` rather than `.verify/` on purpose: `.verify/` is excluded from
the hash the verification receipt attests, so a checker kept there could be weakened without
invalidating an existing pass. In `scripts/`, editing the checker changes the attested content
and forces re-verification.

## Layout

```
sig/     signature marks, served by URL from the signature tooling
CNAME    the custom domain for Pages
NOTICE   the rights reservation - this is the licence position
scripts/ the structural checker
```
