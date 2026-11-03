#!/usr/bin/env python3
"""Package the English website while retaining translations in the repository."""
import argparse
from html import escape
import json
from pathlib import Path
import shutil

SOURCE = Path(__file__).resolve().parents[1]
BASE = "https://pcbcontrol.github.io/alarmmate-support"
PAGES = ("index.html", "privacy/index.html", "usage/index.html", "support/index.html")
SHARED = ("favicon.ico", "apple-touch-icon.png", ".nojekyll", "robots.txt", "sitemap.xml")
LEGACY = {
    "ca/index.html": "/",
    "ca/privacitat/index.html": "/privacy/",
    "ca/us/index.html": "/usage/",
    "ca/suport/index.html": "/support/",
}


def build(output):
    output = output.resolve()
    if output == SOURCE or SOURCE in output.parents and output.parts[len(SOURCE.parts)] != "_site":
        raise ValueError("Use _site or an output directory outside the source repository")
    if output.exists() and any(output.iterdir()):
        raise ValueError("Output directory must be empty")
    output.mkdir(parents=True, exist_ok=True)
    for name in PAGES + SHARED:
        source = SOURCE / name
        if not source.is_file() or source.is_symlink():
            raise ValueError(f"Expected a regular source file: {name}")
        if name in PAGES:
            html = source.read_text(encoding="utf-8")
            if '<html lang="en">' not in html or 'hreflang="ca"' in html or 'class="language"' in html:
                raise ValueError(f"Expected an English-only page: {name}")
        target = output / name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
    if any(path.is_symlink() for path in (SOURCE / "assets").rglob("*")):
        raise ValueError("Assets must not contain symlinks")
    shutil.copytree(SOURCE / "assets", output / "assets")
    for name, path in LEGACY.items():
        target_url = escape(BASE + path, quote=True)
        target = output / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Page moved · AlarmMate</title><meta name="robots" content="noindex"><link rel="canonical" href="{target_url}"><meta http-equiv="refresh" content="0; url={target_url}"></head><body><p>This page has moved to the <a href="{target_url}">AlarmMate website in English</a>.</p></body></html>
''', encoding="utf-8")
    print(json.dumps({"output": str(output), "english_pages": len(PAGES), "legacy_redirects": len(LEGACY), "translations_retained_in_source": True}))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path("_site"))
    build(parser.parse_args().output)
