# 四篇真实论文：章节、句子与段落对照

2026-11-02第二轮，与[前轮两篇](nature-am-writing-study.md)互补。本轮重新核读另外四篇既有论文的PDF，不把卡片摘要当原文阅读，不增加入库数量。下面的英文是对已发表工作的独立概括，不是原文引句、近译或当前作者结果；只迁移组织动作。

## 来源及实际阅读范围

页码是PDF文件页序，从1起。四份正文及B22 SI的SHA256均与已有目录一致。获取入口、版本和哈希见各阅读卡；原文、页面图留在外部资料库。

| 来源 | 本轮阅读 | 边界 |
|---|---|---|
| [B05 · Nature：Recovery of isolated lithium through discharged state calendar ageing](https://doi.org/10.1038/s41586-023-06992-8) | pp.1–6全部主文、摘要及Fig.1–4图注，p.8方法；目视p.2 | [作者组托管出版社版](corpus/b05.md)，19页；未通读扩展数据或独立SI |
| [B22 · Nature：Selective ion transport through hydrated micropores in polymer membranes](https://doi.org/10.1038/s41586-024-08140-2) | pp.1–6全部主文、摘要及Fig.1–4图注；p.8 Cross-over及NMR方法；目视p.4。另核SI封面、文件p.36（印刷p.35）Table 3及说明 | [出版社开放版](corpus/b22.md)，18页；SI共43页，仅所列范围已读 |
| [B04 · Advanced Materials：Diagnosing the Electrostatic Shielding Mechanism for Dendrite Suppression in Aqueous Zinc Batteries](https://doi.org/10.1002/adma.202307708) | pp.1–2摘要与引言相关段；p.4成像比较和Fig.2图注；p.9 Raman及添加剂对照相关段；p.10机制收束、结论和Fig.6图注；目视p.4 | [机构库出版社版](corpus/b04.md)，12页；局部对照，未完整通览主文、未读SI实验或视频 |
| [B12 · Advanced Materials：Achieving Planar Zn Electroplating in Aqueous Zinc Batteries with Cathode-Compatible Current Densities by Cycling under Pressure](https://doi.org/10.1002/adma.202401576) | pp.1–2摘要、引言和性能入口；p.6从SEM到力学测试；p.8覆盖率比较及Fig.4图注；p.10器件结果与结论；目视p.8 | [机构库排版副本](corpus/b12.md)，11页，卷期/在线日期未填全，保留版本限制；未完整通览其余主文或SI |

本记录补充历史卡，不提升目录中的历史篇级计数。原文存在符号、单位或上下文疑义时保留待核，不因期刊层级直接移植或擅自纠正。未独立复算数据、验证全部模型或核读未列出的SI。

## 从章节职责落到编辑动作

按当前任务选择，不要求一篇稿件采用全部动作。

| 部分 | 真实定位与组织动作 | 对本稿的修改 |
|---|---|---|
| 题名、小标题 | B12 p.1将适用电流与施压条件写入贡献；B05 p.1强调静置状态 | 保留改变贡献含义的条件，删除无区分度的“高性能”；特定状态有效不能泛化为任意工况 |
| 摘要 | B05 p.1围绕静置状态不同带来的结果差异；B12 p.1由正负极工况不匹配引出施压 | 从关键对照或使用约束进入，选择一条主要证据链，不堆仪器名和最佳数字 |
| 引言 | B04 pp.1–2质疑跨电池体系直接移植解释；B22 p.1区分干态设计和水合后结构 | 将“研究较少”具体化为待检验的迁移前提或工作状态问题；缺口仍须有文献依据 |
| 结果 | B05 p.2区分容量来源，再说明CE尚不能回答什么；B12 p.6指出SEM不能充分表征力学完整性 | 下一实验应解决一个具体判断；若只重复已有事实，合并而非增加仪器段 |
| 讨论 | B22 pp.5–6保留小孔带来的电导代价；B05 p.6讨论回收与腐蚀竞争、长期收益递减 | 围绕用途解释选择，明确代价影响哪个收益及时间范围；保留已有积极结果 |
| 结论 | B04 p.10回到机制跨体系适用性；B12 p.10回到阴极兼容电流并承认施压实施挑战 | 回答开篇同层级问题，将已验证结果与未来工程实现分开 |
| 方法 | B05 p.8说明TGC取样改变隔膜的理由、图像人工阈值修正；B22 p.8因检测限改用薄层复合膜 | 写明影响比较的操作变更及理由，交代数据怎样成为报告量，不默认各测试同一试样 |
| 图注 | B22 p.4 Fig.3g分别标K体系模拟与Li体系NMR及时间尺度；B12 p.8 Fig.4区分Pt上TEM与Zn箔上SEM | 分面板标对象、条件与实测/计算/示意身份，避免总图题抹去差别 |
| SI | B22主文p.8指向SI Table 3；SI文件p.36写明薄层厚度及裸分子尺寸的解释边界 | 正文指向具体表或Note，SI交代样品条件与量的定义；数字不能脱离构型复用 |
| 数据可用性 | B12 p.10采用向通讯作者申请的方式 | 按本项目真实共享安排撰写，不从范文复制未落实的访问承诺 |

## 四种真实句段推进

### 竞争解释 → 判别条件 → 剩余歧义 → 补充测量

**B05，pp.2–3及p.8。**

> Zhang et al. considered two explanations for the improved efficiency after discharged-state rest: more complete removal of newly deposited lithium or recovery of previously inactive capacity. A cycle returning more charge than it received supports the latter explanation, but does not by itself identify the recovered material. Titration gas chromatography then provided evidence for a contribution from isolated metallic lithium.

第一句明确竞争解释；第二句说明判断已推进到哪里、仍缺什么；第三句让测量承担剩余问题。不能压成“效率提高证实死锂完全回收”；TGC归属仍受原文反应前提约束。

### 性能两端 → 使用约束 → 有依据的选择

**B22，pp.5–6。**

> Wang et al. did not select the membrane with the smallest pore gates for the flow-battery demonstration. Stronger confinement improved selectivity but restricted ionic conduction. The intermediate membrane, cPIM-Ph, combined low crossover with useful conductivity and was therefore evaluated at the device level.

第一句提出需要解释的选择；第二句给出权衡；第三句连接用途。原文后续器件测试承担验证，“被选中”本身不是验证。不能把不同膜的最高电导与最佳选择性拼给同一样品。

### 共同条件 → 生长路径分化 → 机制问题

**B04，p.4；p.9谱学段限定解释范围。**

> Yuan et al. followed zinc deposition with and without LiCl under a common imaging current density. With the additive, existing deposits developed into thicker, merged blocks, while fewer secondary nucleation events were observed. This comparison directs attention to where additional zinc grows; the accompanying changes in solvation also require consideration when interpreting the additive effect.

前两句用条件与过程差别替代“更均匀、更优异”；第三句是结合p.9的编辑综合，不是作者结论引句。添加盐的作用不能自动全部归于一种离子。

### 相似终态 → 不同响应 → 分开机制

**B12，p.8及Fig.4；力学动机见p.6。**

> Li et al. obtained improved electrode coverage both by raising the plating current density and by applying pressure at a lower rate. These similar outcomes did not imply identical deposition mechanisms: pressure did not consistently produce the increase in nucleation overpotential associated with higher current density. The two routes therefore require separate mechanistic accounts.

第一句建立相似性；第二句给出判别响应；第三句收束到有限认识。Pt上液池TEM与Zn箔上SEM分别承担任务，不可合写为“原位TEM直接观测压力作用”。

## 段落与全文复核

段落推进来自新增证据、区分解释、改变尺度或适用边界。若下一句只有“进一步证明”，返回实际证据决定是否删除、合并或改写；允许平行证据，不强造因果。

本轮篇级可参考已通览的两篇Nature：B05沿“效果—来源判别—观察装置—过程—应用与边界”展开；B22沿“工作状态结构—跨尺度输运—用途权衡—器件验证”展开。两篇AM仅支持所列部分对照，不称全篇结构审查。修后反查摘要与结尾是否仍保留结果中的关键代价、实验身份和解释范围。
