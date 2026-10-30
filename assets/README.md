# README 视觉资产

## 封面插画

`readme-hero.png` 是使用内置 `image_gen` 工具生成的 README 横幅，生成日期为 2026-10-30。使用默认内置模式，未使用 CLI、代码绘图或后期像素编辑。原始生成文件直接复制到本目录。

- 尺寸：2172 × 724 px（3:1）
- 文件大小：2,020,484 字节
- SHA-256：`94513d15c17bfc61c39413e964797c43edb6b31241449e3025e8b724a5920600`
- 用途：电池研究证据到论文写作的概念插画。图中的材料层、谱线、曲线及显微形貌均为示意，不是实验结果，也不应作为科学证据使用。
- 已目视检查标题、副标题、三级写作短语、构图和完整边界；未添加期刊标识或实验数值。

## 最终生成提示词

```text
Use case: stylized-concept.
Asset type: Professional scientific open-source README hero banner.
Primary request: Create one polished, restrained editorial hero for "Battery Paper Skill".
Composition/framing: Wide 3:1 landscape, approximately 2400 x 800 pixels. Airy whitespace. Left side contains a clear large title and secondary line. Right side contains carefully composed isometric metallic electrode layers transitioning into a refined stack of manuscript sheets and abstract evidence traces. Keep every element comfortably within the banner, with generous margins.
Scene/backdrop: Light ivory background.
Style/medium: Luxurious restrained scientific editorial design, high-end subtle 3D forms and material textures.
Color palette: Midnight navy precise editorial typography with muted teal accents.
Materials/textures: Refined metallic electrode layers, softly textured manuscript paper, subtle realistic shadows; sophisticated and understated.
Text (verbatim): Large left title EXACT "Battery Paper Skill"; secondary left line EXACT "From evidence to manuscript"; small footer EXACT "SENTENCE → PARAGRAPH → MANUSCRIPT".
Constraints: These three phrases are the only text. Make all text accurate and readable at README width. This is illustrative research artwork, not a scientific result.
Avoid: Journal logos, fake experimental values, dense illegible equations, neon, stock photography, other text, watermarks, flashy decoration.
```

## 流程与审查配图

两张配图均以封面为风格参考，使用内置 `image_gen` 另行生成并原样保存；没有使用 CLI 或后期像素修改。

| 配图 | 用途 | 完整提示词与检查记录 |
|---|---|---|
| [writing-workflow.png](writing-workflow.png) | 资料、论证、写作、审查、交付及修改回路 | [生成记录](writing-workflow-prompt.md) |
| [review-levels.png](review-levels.png) | 句子、段落、文章三个审查尺度与回填闭环 | [生成记录](review-levels-prompt.md) |

插画中的曲线、显微形貌与文稿均为概念示意，不承载实验事实。流程细节以 README 的中文说明、Mermaid 图与技能规则为准。

## 期刊标识来源

下列刊名图从出版社或其官方站点取得，2026-10-30 核对链接后原样保存，用于说明语料来源。标识及期刊名称归各自权利人所有，不表示合作、认证或背书。AM / AEM 图片是 Wiley 新闻站公开的历史资源，不宣称为最新品牌版本。

README 使用的三个 `*-card.svg` 是代码维护的 SVG 展示容器：为原始 Nature 系列矢量标识添加白色底板与留白，仅等比例缩放和定位，不改动刊名字形或颜色，以便在 GitHub 浅色与深色主题下阅读。原始 SVG 同时保留在本目录。

| 文件 | 官方图片来源 | 期刊入口 |
|---|---|---|
| `nature.svg` | [Nature Asia](https://www.natureasia.com/static/common/nature/img/logo-nature-black.svg) | [Nature](https://www.nature.com/) |
| `nature-energy.svg` | [Nature Asia](https://www.natureasia.com/static/ja-jp/nenergy/img/nenergy-logo-black.svg) | [Nature Energy](https://www.nature.com/nenergy/) |
| `nature-communications.svg` | [Springer Nature](https://fullyopen.springernature.com/_nuxt/img/logo-nature-communications.7592758.svg) | [Nature Communications](https://www.nature.com/ncomms/) |
| `advanced-materials.jpg` | [Advanced Science News](https://www.advancedsciencenews.com/wp-content/uploads/2012/01/Advanced-Materials-logo-e1354198651856.jpg) | [Advanced Materials](https://advanced.onlinelibrary.wiley.com/journal/15214095) |
| `advanced-energy-materials.jpg` | [Advanced Science News](https://www.advancedsciencenews.com/wp-content/uploads/2012/01/Advanced-Energy-Materials-logo.jpg) | [Advanced Energy Materials](https://advanced.onlinelibrary.wiley.com/journal/16146840) |

