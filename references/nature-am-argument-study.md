# 真实论文对照：让主张、验证与全文回答对应

本轮核读日期：2026-11-02。来源为[B58 Nature](corpus/b58.md)、[B59 AM](corpus/b59.md)、[B60 AM](corpus/b60.md)，精确版本及阅读范围见卡片。以下仅引必要短语；英文重述由本项目独立撰写，用于展示编辑选择，不是原句、作者稿或可换材料名套用的模板。未复算原始实验。

## 1. 从多个结果中作出设计选择，而非报完一串优点

**B58**：[Electrolyte design for Li-ion batteries under extreme operating conditions](https://www.nature.com/articles/s41586-022-05627-8)，DOI `10.1038/s41586-022-05627-8`。作者公开排版校样物理页3，配方选择段短摘：**“Taking all the above factors”**。该段在物性比较之后作选择，再进入选定配方的结构分析；可借鉴的是选择依据与后续验证之间的关系。

独立英文重述：

> Electrolyte selection balanced Li–solvent binding, ionic transport and electrochemical stability. The selected formulation was then examined through solvation analysis and cell tests. Performance across temperature and rate conditions should remain tied to the corresponding test protocols.

这三句分别完成“选择依据—验证分工—综合范围”。p.4 Fig.3与SI物理页31的低温协议提醒编辑者：冷态充放电和室温充电后低温放电不属于同一验证；不能把不同温度、倍率下的最好结果合成一个同时达到的工况。p.5三电极结果只支持被测条件下的判断。学习其多目标取舍，不将某个单一溶剂描述符写成普适最优准则。

## 2. 用测量缺口驱动段落推进

**B59**：[Measuring Zn Transference with Precision: Insights for Dendrite-Free Zinc Metal Anodes](https://advanced.onlinelibrary.wiley.com/doi/10.1002/adma.202502245)，DOI `10.1002/adma.202502245`。§2.1末段短摘：**“but a closer examination”**；下一节转入Zn迁移数的测量。这里的转折有具体对象：总电导不能直接回答目标离子的输运问题。

独立英文重述：

> Higher bulk conductivity did not imply improved Zn-specific transport. Measurements using a modified Hittorf method resolved this distinction, while spectroscopy and molecular dynamics examined the accompanying solvation changes. Cycling results provided a separate assessment of cell behaviour.

段落先指出当前指标尚不能回答什么，再引入对应测量，随后分配谱学、模型及循环结果的任务。不是在每句末尾重复“confirmed”。§2.2的实测迁移数与§2.3基于自扩散的模拟估计不应写成同一测量；趋势相近也不等于数值吻合。§2.4报告的长时间循环需连同可能微短路和仍在运行的状态理解；SI Figs.S12–15补充终点、重复和倍率协议。不得把仍在运行的时长写成确定失效寿命，也不能把较大不确定度下的近零估计改成精确为零。

## 3. 把代价写进推进过程，而非留到审查附注

**B60**：[Synergistic Coupling of Host and Electrolyte Achieving 1270 Wh L−1 in Anode-Free Lithium Metal Batteries](https://advanced.onlinelibrary.wiley.com/doi/10.1002/adma.202515906)，DOI `10.1002/adma.202515906`。§2.3短摘：**“Despite this initial loss”**。其作用是承接初始不可逆损失，再推进长期性能比较；不是用一个让步词消除代价。

独立英文重述：

> The host–electrolyte combination incurred an initial irreversible loss but improved capacity retention during subsequent cycling. These observations distinguish the formation-stage cost from the longer-term benefit. Pouch-cell energy density requires a separate accounting of cell construction and volume.

§2.3、§2.6与SI组装方法、Table S5支持区分初期、长期和器件层级；不能省去阶段差异而笼统声称所有性能同时提升。SI Figs.S16、S24含Cu-BEL对照，不能仅看主文三组展示便断言缺第四组。称“组合方案改善”与定量证明超加和交互效应是不同命题；后者需同指标、同条件及明确交互定义。器件体积指标不可换成质量指标或脱离封装计量范围。

## 各部分怎样落实编辑动作

以下是从来源提炼的编辑决策，不是三篇原文的逐段翻译或固定章节模板。

| 部分 | 写作时作出的选择 | 修订后检查 |
|---|---|---|
| 题名 | 选实际解决的问题和对象；指标进入题名时保留其计量身份 | 不把局部比较扩大成普适优越性 |
| 摘要 | 用一个核心发现统领设计、测量或器件结果，选决定含义的条件 | 不把分别测试的温度、倍率、载量拼成一个器件 |
| 引言 | 从已有方法不能回答的具体问题引出本研究比较，而非列完文献就宣布创新 | 后文的关键测量确实回答该缺口 |
| 结果 | 依问题需要安排设计取舍、可比性、判别测量、解释与性能；允许不同贡献采用不同次序 | 下一小节承接真实未决问题，不靠过渡词制造依赖 |
| 表征与计算 | 先写观察或估计，再交代它改变了哪项判断；给互补方法不同任务 | 模型趋势、物种归属与直接测量没有互换身份 |
| 讨论 | 解释为何某项指标不足，以及多项证据共同支持到哪一步 | 初期代价、终点定义和替代解释仍可见 |
| 结尾 | 回答引言的问题，保留可迁移认识所需边界 | 不突然升级成全工况最优或唯一机制 |
| 方法 | 写足决定比较成立的协议、校准与排除条件 | 影响主张理解的条件在正文也有适当提示 |
| 图注与SI | 给面板、状态和重复/终点定义；把SI关键对照接回正文论证 | 关键反证不被藏入SI；没有把归档当成核读 |

## 句子—段落—全文的修改实例

以下“改前”是人为概括的薄弱结构，不冒充原文或实际作者稿；“改后”是编辑组织方案，不虚构新实验。

- **句子重心：** 从“测了电导、测了迁移数、又做了MD”改为“哪项总体现象留下了什么未决问题，哪项测量回答它”。仅在方法确实能分辨时使用这一结构，不能补造验证能力。
- **段落任务：** 从“每句一个优点，末句宣称全面改善”改为“建立比较—说明初期代价—报告后期收益—给有限综合”。条件已明确时不句句重复，段尾只保留新增认识。
- **全文依赖：** 从“设计→所有表征→全部性能→总结优点”改为按当前问题串联“为何选它→证据能区分什么→哪些测试支持目标用途→代价与边界→对开篇问题的回答”。这是一种可选重排，不推翻有效的确认结构。

改完先遮住摘要和结论，只从结果、图注及必要SI重建答案；再核对两处压缩是否保留同一对象、比较基准和边界。若重建的答案只能支持特定协议，摘要不得变成全工况主张。随后检查每个段落是否推进该答案；不推进的内容应删、合并或转入合适位置。执行入口见[论证设计](argument-design.md)、[实质修订](editorial-revision.md)和[三级审查](review-protocol.md)。
