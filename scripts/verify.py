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
    '일상웹툰.md': 'c3b12cfcfa298d2efab90c5f42f87c53da8bab550b5f8de91a7ac6ebf7425a33',
    '카툰애니.md': '66c00119583a4d58aa8d999f724063ecd5166ba41f9a67861ac187f98b574515',
    '팬아트애니.md': 'c3b02ae2159f3b66bfed2887eb43bc1897187992a2f6b7db3dd9e44a75656027',
}
actual={p.name for p in STYLE_DIR.glob("*.md")}
assert actual==set(EXPECTED), (actual, set(EXPECTED))
for filename,digest in EXPECTED.items():
    assert hashlib.sha256((STYLE_DIR/filename).read_bytes()).hexdigest()==digest, filename
print(f"OK: {len(EXPECTED)} original prompts match expected SHA-256 digests.")
