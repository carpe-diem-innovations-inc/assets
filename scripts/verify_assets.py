"""Structural check for the brand-asset host.

There is no application here, so "works" means the things this repo exists to serve are
actually servable: every image is a real image, the custom-domain file is intact, and the
notice that reserves all rights is still present and still says so.

Standard library only, on purpose - this must run anywhere with no install step.

Lives in scripts/ rather than .verify/ deliberately: .verify/ is excluded from the hash the
verification receipt attests, so a checker kept there could be weakened without invalidating
an existing pass. Here, editing the checker changes the attested content and forces a
re-verification.
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
JPEG_MAGIC = b"\xff\xd8\xff"
SVG_HINT = b"<svg"

failures: list[str] = []
checked = 0


def fail(msg: str) -> None:
    failures.append(msg)


# --- every image is a real image -----------------------------------------
images = sorted(
    p for p in ROOT.rglob("*")
    if p.is_file()
    and p.suffix.lower() in {".png", ".jpg", ".jpeg", ".svg"}
    and ".git" not in p.parts
)
if not images:
    fail("no image assets found - this repo exists to serve them")

for img in images:
    checked += 1
    head = img.read_bytes()[:512]
    rel = img.relative_to(ROOT).as_posix()
    if img.stat().st_size == 0:
        fail(f"{rel}: empty file")
    elif img.suffix.lower() == ".png" and not head.startswith(PNG_MAGIC):
        fail(f"{rel}: not a PNG despite the extension")
    elif img.suffix.lower() in {".jpg", ".jpeg"} and not head.startswith(JPEG_MAGIC):
        fail(f"{rel}: not a JPEG despite the extension")
    elif img.suffix.lower() == ".svg" and SVG_HINT not in head.lower():
        fail(f"{rel}: no <svg> element in the first bytes")

# --- the custom domain must be intact ------------------------------------
cname = ROOT / "CNAME"
if not cname.exists():
    fail("CNAME missing - GitHub Pages would drop the custom domain")
else:
    host = cname.read_text(encoding="utf-8").strip()
    if not host or "." not in host:
        fail(f"CNAME does not contain a hostname: {host!r}")
    else:
        checked += 1

# --- the rights reservation must still reserve rights --------------------
notice = ROOT / "NOTICE"
if not notice.exists():
    fail("NOTICE missing - this repo is public and grants no licence; the notice is what says so")
else:
    text = notice.read_text(encoding="utf-8").lower()
    if "all rights reserved" not in text:
        fail("NOTICE no longer reserves all rights")
    else:
        checked += 1

# --- and it must NOT have acquired an open licence -----------------------
for name in ("LICENSE", "LICENSE.md", "COPYING"):
    if (ROOT / name).exists():
        fail(
            f"{name} present: these are proprietary brand assets and are deliberately "
            "unlicensed. Public visibility exists to serve them over Pages, not to grant reuse."
        )

print(f"checked: {checked} item(s), {len(images)} image(s)")
for f in failures:
    print(f"  FAIL {f}")
sys.exit(1 if failures else 0)
