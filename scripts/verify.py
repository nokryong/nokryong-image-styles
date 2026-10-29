#!/usr/bin/env python3
"""Validate style selection and full original-byte integrity against hashes embedded below."""
from pathlib import Path
import hashlib
ROOT=Path(__file__).resolve().parents[1]
STYLE_DIR=ROOT/"skills"/"nokryong-art-style"/"styles"
EXPECTED={
    '아마추어웹툰.md': 'b0a02f4e7ed891d51b3b7251e63ead6cc7abb438dda6d2e59c99b7630927c568',
    '인디망가.md': '4db5e483c9fa155f862b855efa60f0dc2bea935986080c7d721d1089097f6076',
    '일상웹툰.md': 'f9a6411fc8f12b0aa0f86e176902aff62a67e8f6f851ab47e68b300b51be446c',
    '흑백망가.md': '366268b16a0cb47d2e49908ae1472370f56ace0163291a141465272df22792d6',
    '잉크애니.md': 'edaee380a746727ed9e7f8c40354757adccf002550907f11bdb05b32ccf38083',
    '팬아트애니.md': '439ddad6e05506ca4228cb248c22a0bd673fd717fa60af765a926e38ea926da3',
    '카툰애니.md': 'e379abd27bd6b5b6d24730f52b61a9371b2e4c8a099fa2fd997ea8b923bf2a18',
    '치비애니.md': '62780c9818a24e6f89785c61e067ce6824fbee6e1a8e764e840b52728df382f8',
    '러프애니.md': 'e0914a370d2df9ecaabcaf711b9f0e8ae5b326529133bc7d67263cb9b4eb1d2a',
    '무테애니.md': '10bd2733a11ba78b4685a426f54ee03ff9a3a1aeb4498e22fbe50608ab1604bb',
    '붓애니.md': 'ac0bb69b5aa887964bf1bb01ff76541d13838c0c329506feb53a69e37e940992',
}
actual={p.name for p in STYLE_DIR.glob("*.md")}
assert actual==set(EXPECTED), (actual, set(EXPECTED))
for filename,digest in EXPECTED.items():
    assert hashlib.sha256((STYLE_DIR/filename).read_bytes()).hexdigest()==digest, filename
print(f"OK: {len(EXPECTED)} original prompts match expected SHA-256 digests.")
