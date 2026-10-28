#!/usr/bin/env python3
"""Validate style selection and full original-byte integrity against hashes embedded below."""
from pathlib import Path
import hashlib
ROOT=Path(__file__).resolve().parents[1]
STYLE_DIR=ROOT/"skills"/"nokryong-art-style"/"styles"
EXPECTED={
    '아마추어웹툰.md': '30e7af81856bd5f9c3b573e36c020a604d759e54ca7fbc41daa168b32f92500d',
    '인디망가.md': 'ea6b3c8a0e0d0bc20c93ab2eb9134ba3dbd809ec3db32271fd0a16dd7133afe1',
    '잉크애니.md': '55fc3175f779631a7bbf52cc89a9114aca6d2f010f9e7dcd1571fb62ab448f6c',
    '치비애니.md': 'cc897c624e624df5bc9f6761cf21b885a546dfe35948f30931aea9fac3cd8b63',
    '흑백망가.md': 'a74398f56857d0017791e1233581ff3bd3272fd7a28b32575695ef6a0496e19a',
}
actual={p.name for p in STYLE_DIR.glob("*.md")}
assert actual==set(EXPECTED), (actual, set(EXPECTED))
for filename,digest in EXPECTED.items():
    assert hashlib.sha256((STYLE_DIR/filename).read_bytes()).hexdigest()==digest, filename
print(f"OK: {len(EXPECTED)} original prompts match expected SHA-256 digests.")
