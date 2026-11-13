#!/usr/bin/env python3
"""Safely expand the original MailTrace project archive into the repository tree.

This is a one-time migration helper. It deliberately excludes secrets, real mailbox
data, generated files, and the invalid placeholder model weight from the supplied ZIP.
"""
from __future__ import annotations

import hashlib
import os
import re
import zipfile
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[2]
ARCHIVE = ROOT / "MailTrace-AI-SIH.zip"
PREFIX = "MailTrace-AI-SIH/"
PRESERVE_ROOT = {
    "README.md", ".gitignore", ".env.example", "LICENSE",
    "CONTRIBUTING.md", "SECURITY.md", "CHANGELOG.md",
}
FORBIDDEN_PARTS = {".git", ".github", ".idea", ".vscode", "__pycache__", "node_modules"}
FORBIDDEN_SUFFIXES = {".eml", ".msg", ".mbox", ".pem", ".key", ".safetensors", ".bin", ".pt", ".pth"}
SECRET_NAME = re.compile(r"(^|/)(credentials|token)\.json$", re.IGNORECASE)


def safe_destination(name: str) -> Path | None:
    if not name.startswith(PREFIX) or name.endswith("/"):
        return None
    relative = name[len(PREFIX):]
    pure = PurePosixPath(relative)
    if pure.is_absolute() or ".." in pure.parts:
        return None
    if any(part in FORBIDDEN_PARTS for part in pure.parts):
        return None
    if pure.name == ".gitkeep" or pure.name == ".DS_Store":
        return None
    if relative in PRESERVE_ROOT:
        return None
    if relative.lower().endswith(tuple(FORBIDDEN_SUFFIXES)) or SECRET_NAME.search(relative):
        return None
    if relative.startswith("backend/.secrets/"):
        return None
    destination = (ROOT / Path(*pure.parts)).resolve()
    if ROOT.resolve() not in destination.parents:
        return None
    return destination


def main() -> None:
    if not ARCHIVE.is_file():
        raise SystemExit(f"Expected migration archive not found: {ARCHIVE.name}")

    written = 0
    skipped = 0
    with zipfile.ZipFile(ARCHIVE) as archive:
        for entry in archive.infolist():
            destination = safe_destination(entry.filename)
            if destination is None:
                skipped += 1
                continue
            destination.parent.mkdir(parents=True, exist_ok=True)
            payload = archive.read(entry)
            destination.write_bytes(payload)
            written += 1

    model_dir = ROOT / "ml/models/dataset3_v1.0.0"
    model_dir.mkdir(parents=True, exist_ok=True)
    weights = model_dir / "model.safetensors"
    if weights.exists():
        weights.unlink()

    # The supplied archive's model weight entry is a 134-byte placeholder. Do not
    # publish it as a real checkpoint; keep the manifest and metadata for provenance.
    ARCHIVE.unlink()
    print(f"Expanded {written} project files; skipped {skipped} unsafe/placeholder entries.")
    print("The trained model weights were not included; see README.md for setup details.")


if __name__ == "__main__":
    main()
