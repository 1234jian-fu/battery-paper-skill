# 从检查意见到正文修改

用于已有文字事实基本正确、却仍像测试报告，或逐句润色后全文重点不清的情况。沿用[三级审查](review-protocol.md)的范围和来源要求；这里只补充修改决策，不新增固定评分、必填报表或期刊句式模板。先按任务参看[Nature / AM真实正文对照](nature-am-writing-study.md)的来源定位、结构分析及真实来源重述；下文A/B示例则是独立构造的教学情景，不是论文引文。二者分别标识，合成示例不能代替真实对照。

## 先定位缺陷，再决定修改幅度

从现稿指出一个具体阅读障碍，例如“读完仍不知道A与B的差别出现在哪个条件”，而不是“学术性不足”。选择能解决它的最小修改；若缺的是证据，改措辞不能补齐证据。

| 现稿的具体问题 | 修改动作 | 修后判断 |
|---|---|---|
| 一段依次介绍仪器，读者需自行拼出发现 | 提取共同回答的问题，把关键比较放在中心，保留各方法独有的信息 | 不看仪器名，也能说出本段新增了什么认识 |
| 句子都正确，但段中存在两项独立结论 | 按结论与各自依据拆段；共同条件只在适当位置定义一次 | 两段均有足够依据，不产生无功能的孤立过渡段 |
| 为解释后文才在末尾定义基准或样品状态 | 将前提移到首次需要处，并删去原位置重复 | 比较首次出现时即可理解，后文指代仍明确 |
| 一段每句都有“表明”，结论重复升格 | 保留直接观察，将确需整合的推断集中到证据充分的位置 | 每个推断有明确对象和依据，不把同向信号累计成唯一因果 |
| 改稿新增了多个限定句，遮住主要结果 | 合并作用域相同的限定；把方法细节移回方法或图注 | 发现仍清楚，改变结论的限制仍在主张附近 |
| 摘要与结论逐字复述结果数据 | 按下表重新分配信息，保留各自独立理解所需条件 | 每处承担不同任务，压缩没有改变证据身份 |
| 宏观顺序有问题，但句子已反复打磨 | 先按理解依赖移动证据模块，再改模块间承接 | 不再为迁就原顺序补空泛连接句 |

## 同一发现进入不同部分时，改变职责而非强度

先选一项中心发现及其决定性条件，检查它在现有各部分承担的作用。只查稿件实际包含的部分，不强制单列讨论或结论。

| 位置 | 应保留的信息 | 不应重复搬入的信息 |
|---|---|---|
| 题名 | 可由全文支撑的贡献中心与必要对象范围 | 全部性能指标、尚未验证的机制和应用承诺 |
| 摘要 | 问题、关键动作、主要发现及决定其含义的条件 | 仪器目录、多个支持同一判断的次要数列 |
| 引言末段 | 研究如何回答缺口，关键比较为何必要 | 后文每个结果的逐项预告 |
| 结果 | 对象与共同基准、决定性差异、互补证据与局部解释 | 无助于当前判断的操作细节和反复宣传 |
| 讨论 | 各结果共同改变的认识、与既有解释的关系、可支持的含义 | 把结果换同义词再报一遍；没有新依据的因果升级 |
| 结尾 | 对开篇问题的回答、可迁移认识及边界 | 与摘要等量重复背景和数字；突然增加新发现 |
| 方法、图注和SI | 分别承载复现过程、读图条件和可定位的扩展证据 | 只在SI披露会改变主文中心结论的反例 |

摘要独立阅读所需的条件允许重复。删重复时依据功能，不以字面重合率裁决。讨论的增量可以是明确一个评价条件、缩小解释范围或提出有依据的检验方向，不必制造普适机制。

## 表征段的实质改写示例

**合成事实：** A、B是同构型电池；25 °C、相同载量与协议下，100圈容量保持率为89%和71%。循环前两组截面接触形貌相近。100圈后、相同荷电状态的取样截面中，B的脱离区域更明显；对应状态的拟合界面电阻为A 42 Ω、B 83 Ω。没有分离接触和化学变化的贡献，没有给定重复次数或显著性检验。

**待改稿：** `SEM was used to characterize A and B. B showed more detached regions after cycling. EIS further confirmed the excellent interfacial stability of A. A retained 89% of its capacity after 100 cycles, whereas B retained 71%. These results demonstrate that A suppresses contact loss and thereby prevents capacity fading.`

**改写：** `At 25 °C, A retained 89% of its capacity after 100 cycles, compared with 71% for B under the same loading and cycling protocol. Although the initial cross-sectional contact morphologies were similar, B showed more pronounced detached regions after cycling when sampled at the same state of charge. At this state, the fitted interfacial resistance was lower for A than for B (42 versus 83 Ω). The higher capacity retention of A thus coincided with less pronounced contact detachment and a lower fitted interfacial resistance; the respective contributions of contact and chemical changes remain unresolved.`

修改的是论证：先建立性能差异，再用初始状态与循环后状态连接形貌变化，最后并列电化学响应。删除没有依据的“confirmed”“prevents”，保留明确观察及有限综合。没有新增“均匀”“显著”“重复证实”等事实。若上一段已报告容量比较，可缩为一句承接，不必重报两组数字。

同一事实在其他部分可以这样取舍，以下英文仍是合成示例：

- **摘要中的发现句：** `Under matched loading and cycling conditions at 25 °C, A retained 89% of its capacity after 100 cycles, compared with 71% for B, alongside less pronounced contact detachment at the sampled state.` 不把关联压缩成因果。
- **讨论中的综合句：** `The initial similarity and post-cycling divergence in contact morphology connect the performance contrast to an evolving interfacial difference, although the present comparison does not isolate its contribution to capacity loss.` 综合比较的含义，不再重复全部数值；相关限制若紧邻且已充分表达，可与前句合并。
- **结尾中的回答句：** `A improved capacity retention under the tested conditions, with accompanying differences in contact morphology and fitted interfacial resistance.` 该句只是本情景允许的收束；没有更多证据时，不为了显得深刻而补写材料设计定律。

## 对照真实论文时，留下一项可核验的修改

按[语料索引](literature-corpus.md)选功能匹配的来源，核读完整相关段及必要上下文。简短记录“来源定位—它的组织动作—本稿具体改动—不能迁移的内容”，例如：源段用初始对照建立变化，因此将本稿循环前证据提前；源段的物种归属不能沿用。没有实际核读来源时，将当前工作称为内部编辑，不声称完成Nature或AM原文对照。

比较前后稿时先核事实，再判断读者能否更快识别关键比较、证据分工与有范围的回答。若新版只是更长、更像范文或用了更强动词，返回具体缺陷重新修改。保存有效好句，问题已解决就停止本轮；修订改变事实、顺序或句段边界时，更新既有映射与交叉引用。
