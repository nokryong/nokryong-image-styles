#!/usr/bin/env python3
"""Validate style selection and full original-byte integrity against hashes embedded below."""
from pathlib import Path
import hashlib
ROOT=Path(__file__).resolve().parents[1]
STYLE_DIR=ROOT/"skills"/"nokryong-art-style"/"styles"
EXPECTED={
    '아마추어웹툰.md': 'f4a49dddcd9fbe7950911f1cf6d195269b110fc6b3d8bc4e23136dcc95478b5f',
    '인디망가.md': '0077bdc28c47df5774f8337fe56fc827fa6b2f276caaac71ab765a0393162b4b',
    '일상웹툰.md': '4f0a2bfbb66949c942cd940129f12489605ec8f6ae721a78ccfa11e3e3be84c0',
    '팬아트애니.md': '50cf5510166e3242074cd74dc897e0ec8b40366b16df53de76372ff3fcdb0440',
    '카툰애니.md': 'e23b9876fc3ce090d8baaf2a58d328307c5758d18fa6aa0d064cd8d1544129e1',
    '무테애니.md': '3ff89ca0755bc51ab8f35e55e73897394890a3397c55a84ec9a6cf44742fa1a7',
    '러프칼라망가.md': 'ff15536478f2e12d67219b201234e923dbdead90d50d285d82dd594793da9c8b',
    '치비애니.md': '1d129af8eb07009cb560235d63d6daac307869a19a95fa254f2254d55bbdbd2a',
    '디시콘.md': '13710c3a444da4a2fb11f5cdfa3dc319f3d85aeabad3070f059fb98728bd7c12',
}
actual={p.name for p in STYLE_DIR.glob("*.md")}
assert actual==set(EXPECTED), (actual, set(EXPECTED))
for filename,digest in EXPECTED.items():
    assert hashlib.sha256((STYLE_DIR/filename).read_bytes()).hexdigest()==digest, filename
print(f"OK: {len(EXPECTED)} original prompts match expected SHA-256 digests.")
