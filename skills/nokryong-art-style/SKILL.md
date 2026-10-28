---
name: nokryong-art-style
description: "Use this skill when creating, editing, comparing, or choosing images in the user-authored 녹용화풍 art styles: 아마추어웹툰, 인디망가, 잉크애니, 치비애니, 흑백망가, 일상웹툰, 카툰애니, 팬아트애니, 러프애니, 데포망가, 무테애니. Before generating, read the entire original Markdown source for the requested style. The art-style source takes priority over generic defaults and illustrative references."
---

# 녹용화풍 — original-source art style selector

This skill includes **exactly eleven unmodified source style prompts**. The bundled Markdown files, not this overview, determine the image's rendering. Select styles using the exact registry below and apply their full source documents.

## Available styles — exact registry

| User-facing style (also accept spaces between syllable groups, `.md` suffix) | Source file |
| --- | --- |
| 아마추어 웹툰 / 아마추어웹툰 | `styles/아마추어웹툰.md` |
| 인디망가 | `styles/인디망가.md` |
| 잉크애니 | `styles/잉크애니.md` |
| 치비애니 | `styles/치비애니.md` |
| 흑백망가 | `styles/흑백망가.md` |
| 일상웹툰 | `styles/일상웹툰.md` |
| 카툰애니 | `styles/카툰애니.md` |
| 팬아트애니 | `styles/팬아트애니.md` |
| 러프애니 | `styles/러프애니.md` |
| 데포망가 | `styles/데포망가.md` |
| 무테애니 | `styles/무테애니.md` |

Use only styles in this registry, and never substitute a different style for the one the user requested.

## Required workflow for generation and editing

1. **Identify the exact style.** Resolve the user's named style using the registry above. Normalize trivial spacing and the `.md` suffix only. Never infer that a different style name refers to one of these eleven. If several styles are requested for separate outputs, resolve each one independently.
2. **Open and read the *entire* corresponding local Markdown source** before composing any image instruction or calling an image generation/editing tool. Neither the style name, a short description, memory of previous images, nor this SKILL.md substitutes for the complete source. If the source cannot be read, state that limitation and do not pretend to have applied it.
3. **Preserve the source verbatim.** Do not edit, shorten, summarize, translate, reword, reorder, add to, or remove clauses from the original document. When direct prompt forwarding is available, use the full unchanged source as a separate high-priority style block followed by separately delimited scene instructions; otherwise apply the complete read source as faithfully as the image tool permits and do not falsely claim that it was forwarded literally.
4. **Keep style separate from subjects.** Characters, their identities, scene, camera, framing, props, actions and user-provided composition belong in the separate user-request block; do not rewrite the original style document to combine them. The selected style controls lines, brushwork, coloring, shading, deformation, surface finish and rendering detail. If the user supplies a reference image, use it for subject/identity/pose only unless explicitly told otherwise. Do not absorb the reference image's rendering style by default.
5. **No spontaneous polish.** Do not introduce rendering choices the selected style forbids or that the user did not request, such as extra gradients, outlines, highlights, makeup, glossy finishes, text overlays, watermarks or elaborate backgrounds. Resolve competing directions by respecting higher-priority constraints and the user's current explicit request; never quietly modify the stored source file.
6. **Check and correct.** After generation, compare the result against the source's full applicable requirements where possible. When asked to regenerate, reread the selected full style file before correcting. No exact visual match can be guaranteed by a skill alone.

## Other requests

- **List styles:** list exactly the eleven registry names and do not invent others.
- **Choose for me:** select one of the eleven based on the user's specific request, then read its entire source before generating; report which style was chosen. If selection is genuinely ambiguous, ask for the style name.
- **Multiple styles for different images:** load each corresponding source separately; do not mix styles unless explicitly instructed.
- **Character requests:** preserve the user's character descriptions and references; do not invent identity details or let them change the selected style's rendering rules.
- **Provenance questions:** report the exact local filename that was read, and never claim a file was loaded if it was not.

The eleven original style documents are included byte-for-byte and should not be edited or silently replaced during routine use.
