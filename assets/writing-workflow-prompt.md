# 写作流程图生成记录

`writing-workflow.png` 于 2026-10-30 使用内置 `image_gen` 工具生成；`readme-hero.png` 仅作为视觉风格参考，不是编辑目标。未使用 CLI、代码绘图或后期像素编辑。原始生成文件直接复制到本目录。

- 尺寸：2172 × 724 px（3:1）
- 文件大小：1,811,106 字节
- SHA-256：`e107f1d9f2aa679304284b20ae6a34820d81578700f13523e7ccd3ee8c0a3c44`
- 已目视核对标题、五个步骤及副标题，文字均与提示词一致。
- 四条主箭头从左到右；唯一回弯箭头从 REVIEW 指回 DRAFT，表示审查后修改。
- 纸页、形貌及曲线为概念插画，不是实验结果。

## 最终生成提示词

```text
Use case: infographic-diagram.
Asset type: Professional scientific open-source README editorial workflow infographic.
Primary request: Create a new wide approximately 3:1 infographic, about 2400 x 800 pixels, illustrating the scientific writing workflow with exactly five equal-width steps, in one horizontal row.
Input images: Image 1 is a reference image for palette, typography, materials and understated editorial style only; it is NOT an edit target. Create an entirely new composition. Do not repeat the hero title, electrode structure, manuscript pile, footer or layout.
Scene/backdrop: Light ivory background with generous whitespace, elegant midnight navy typography and muted teal rules and arrows.
Style/medium: Refined scientific editorial infographic with delicate miniature research illustrations, subtle realistic 3D material textures and soft shadows. Restrained, precise, polished, calm, readable.
Composition: Title centered at the top. Five evenly spaced equal-width steps below. Each step has one miniature illustration, a bold readable heading, and a concise readable subtitle. Illustrations from left to right: research papers with a simple unlabeled figure; evidence nodes with connections; a manuscript page; a review magnifier over a page; organized delivery files with a small source-mapping mark. Do not make the artwork busy.
Text (verbatim): Top title EXACT "The writing workflow".
Step 1 heading EXACT "EVIDENCE"; subtitle EXACT "Figures & data".
Step 2 heading EXACT "ARGUMENT"; subtitle EXACT "Claims & support".
Step 3 heading EXACT "DRAFT"; subtitle EXACT "Write & compare".
Step 4 heading EXACT "REVIEW"; subtitle EXACT "Sentence to manuscript".
Step 5 heading EXACT "DELIVER"; subtitle EXACT "Text & source map".
Arrow semantics: Four simple thin main arrows point strictly left to right, EVIDENCE → ARGUMENT → DRAFT → REVIEW → DELIVER. Add exactly one separate curved return arrow below, starting at REVIEW and curving back to DRAFT with its arrowhead at DRAFT; this means revision. Keep the return arrow clear of all text. No other arrows.
Constraints: All headings and subtitles must be easily legible when the image is displayed at 900 pixels wide. These specified phrases are the only text. No extra stages. Illustrative research artwork, not scientific experimental results.
Avoid: Journal logos, fictitious numerical values, dense equations, tiny unreadable type, neon, gradients that overwhelm the background, stock photography, duplicated hero imagery, watermarks, decorative clutter.
```

