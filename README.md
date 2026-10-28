# 녹용화풍

[화풍 예시 갤러리](https://nokryong-style-room.tunedpike66.chatgpt.site/)

**녹용화풍 (Nokryong Image Styles)**은 이미지 생성 작업에서 화풍 이름에 맞는 **원본 Markdown 프롬프트를 정확하게 불러오기 위한 스킬 라이브러리**입니다.

화풍을 막연히 추측하거나 다른 스타일로 치환하지 않고, 각 화풍의 원문을 읽어 이미지 생성 지침에 적용하도록 설계했습니다.

## 수록 화풍

| 화풍 | 원본 프롬프트 |
| --- | --- |
| 아마추어 웹툰 | [아마추어웹툰.md](skills/nokryong-art-style/styles/아마추어웹툰.md) |
| 인디망가 | [인디망가.md](skills/nokryong-art-style/styles/인디망가.md) |
| 잉크애니 | [잉크애니.md](skills/nokryong-art-style/styles/잉크애니.md) |
| 치비애니 | [치비애니.md](skills/nokryong-art-style/styles/치비애니.md) |
| 흑백망가 | [흑백망가.md](skills/nokryong-art-style/styles/흑백망가.md) |
| 일상웹툰 | [일상웹툰.md](skills/nokryong-art-style/styles/일상웹툰.md) |
| 카툰애니 | [카툰애니.md](skills/nokryong-art-style/styles/카툰애니.md) |
| 팬아트애니 | [팬아트애니.md](skills/nokryong-art-style/styles/팬아트애니.md) |


## 작동 방식

1. 사용자 요청에서 화풍 이름을 확인합니다.
2. 해당 화풍의 `.md` 파일 **전체**를 불러옵니다.
3. 원본 화풍 규칙은 변경하지 않고, 인물·배경·행동·구도 등의 요청을 별도로 결합합니다.
4. 이미지 생성·수정 시 원본 화풍의 선, 채색, 명암, 비례, 표현 밀도 등의 조건을 우선 적용합니다.

스킬은 프롬프트 선택·적용 과정을 정의합니다. 실제 이미지 결과는 사용하는 생성 모델에 따라 달라질 수 있습니다.

## 설치

### Codex 등 스킬을 지원하는 에이전트

저장소를 복제한 후 `skills/nokryong-art-style` 폴더를 해당 에이전트의 스킬 디렉터리에 복사합니다.

```bash
git clone https://github.com/nokryong/nokryong-image-styles.git
```

Codex에서 개인 스킬 디렉터리 `~/.agents/skills/`를 사용하는 경우:

```bash
mkdir -p ~/.agents/skills
cp -R nokryong-image-styles/skills/nokryong-art-style ~/.agents/skills/
```

### 플러그인 패키지

`plugin.json`과 `skills/` 디렉터리를 포함한 저장소 구조를 사용합니다. 사용 중인 ChatGPT 환경이 개인 플러그인 등록을 지원하는 경우 패키지로 등록할 수 있습니다. GitHub 저장소를 복제하는 것만으로 ChatGPT에 자동 설치되지는 않습니다.

## 사용 예시

```text
인디망가 화풍으로 비 내리는 밤거리의 우체통을 그려줘.
치비애니로 마법서를 들고 달리는 모험가를 그려줘.
녹용화풍에서 사용할 수 있는 화풍 목록을 알려줘.
```

## 저장소 구조

```text
.
├── README.md
├── LICENSE                         # MIT: 스킬 및 소프트웨어 구성요소
├── plugin.json
├── scripts/
│   └── verify.py                   # 원본 화풍 파일 SHA-256 검사
└── skills/
    └── nokryong-art-style/
        ├── SKILL.md                # 화풍 선택·적용 절차
        ├── agents/
        │   └── openai.yaml
        └── styles/
            ├── LICENSE             # CC BY 4.0: 원본 화풍 프롬프트
            ├── 아마추어웹툰.md
            ├── 인디망가.md
            ├── 잉크애니.md
            ├── 치비애니.md
            ├── 흑백망가.md
            ├── 일상웹툰.md
            ├── 카툰애니.md
            └── 팬아트애니.md
```

원본 프롬프트 무결성 확인:

```bash
python scripts/verify.py
```

## 라이선스

이 저장소는 구성요소에 따라 라이선스가 다르게 적용됩니다.

| 대상 | 라이선스 |
| --- | --- |
| 스킬 및 소프트웨어 구성요소(`SKILL.md`, `plugin.json`, `scripts/` 등) | [MIT](LICENSE) |
| `skills/nokryong-art-style/styles/*.md` 원본 화풍 프롬프트 8개 | [CC BY 4.0](skills/nokryong-art-style/styles/LICENSE) |

화풍 프롬프트를 재배포하거나 수정본을 공유할 때에는 원저작자 **nokryong**과 원본 출처, [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 라이선스를 표시하고 변경 여부를 밝혀야 합니다. 두 라이선스 모두 상업적 이용을 허용합니다.

이 라이선스 구분은 **프롬프트 문서의 이용 조건**을 설명하며, 이를 사용해 생성한 모든 이미지에 동일한 저작자 표시 의무가 자동으로 적용된다는 의미는 아닙니다.
