# Nature / Advanced Materials 句子表达复核

结论：现有试写稿的术语、主要事实和证据区分已有良好基础，但不能由上一轮高分直接判为Nature或Advanced Materials的成熟发表表达。仍有可定位的空泛引导句、信息负荷集中和重复限定。本轮据实际原文补强句子审查规则，并给出编辑示范；不宣称整篇稿件或以后每次生成都已达到期刊水准。

## 对照对象与实际阅读

本次检查的是上一轮生成的[锌电解液段落](../real-paper/outputs/zinc-optimized-post-review.md)和[固态硅负极段落](../real-paper/outputs/solidstate-optimized.md)，共34句，不是用户尚未提供的正式稿。科学事实仍来自原两篇Nature Communications研究。新增Nature/AM论文仅用于表达和组织对照，未将其数值或机制迁入练习稿。

| 参照 | 实际版本与定位 | 比较的表达动作 |
|---|---|---|
| Lu等，*Ligand-channel-enabled ultrafast Li-ion conduction*，Nature 627, 101–107 (2024)，[出版社](https://www.nature.com/articles/s41586-024-07045-4)、[高校站点公开PDF](https://bpb-us-e1.wpmucdn.com/blog.umd.edu/dist/7/477/files/2024/02/a21f7670-47bb-49ed-b24c-c65c9626dea5-17deb821140e7716.pdf) | 出版社元数据确认2024-02-28发表；实际核读9页排版副本中的第3–6页相关结果、Fig.2/4及第8页相关方法。该副本首页在线日期仍为占位符，不能称与最终版本逐字相同。 | 模型段由要解释的问题进入具体量和比较，再接互补证据；界面段使观察对象、对照与局部解释相邻。 |
| Yuan等，*Diagnosing the Electrostatic Shielding Mechanism for Dendrite Suppression in Aqueous Zinc Batteries*，Advanced Materials 36, 2307708 (2024)，[出版社](https://advanced.onlinelibrary.wiley.com/doi/10.1002/adma.202307708)、[高校公开库](https://wrap.warwick.ac.uk/id/eprint/186968/) | 正式出版版12页；首次在线2023-10-25，卷期为2024。核读Results and Discussion中的LC-TEM段及Raman段、正文测试条件与Fig.2/3/5图注，查看PDF第4–5、9页实图/正文。未核读SI方法及视频。 | 成像句沿对象和时间推进，比较句直接呈现形貌差别；Raman段区分峰归属、相对强度变化与进一步解释。 |

两篇均为真实原始研究，但样本很小，体系也不完全相同。这里比较同功能的观察、比较、模型和解释句，不统计“顶刊通用句式”，也不将来源中的强因果语气照搬。没有开展研究结果复现或完整稿件宏观评测。

## 逐句检查发现

完整记录见[34句复核表](sentence-review.md)及[原句、判断与输入哈希](sentence-review.json)。判断由主代理在知道来源及版本的情况下完成，属于非盲编辑审读；没有新增外部专家评分，也没有改写原始六组输出或评分。

- **可保留的基础：** 观察、拟合与模拟分开；物理量、条件、对照及因果边界大体明确。较长但只有一个清楚比较任务的句子不必拆短。
- **实质不足：** 部分句子只宣布“提供信息”或“支持解释”，下一句才给出发现；有的配方句或趋势句承载过多独立任务。
- **需要有选择地压缩：** 重要限定不能删，但相同功能的引导或收束可以合并。报告口吻与正文口吻也应区分：本次第三人称是文献练习的身份要求，不应为模仿论文的we而改成虚假的新实验。

上一轮五维评分覆盖事实、表征精度、段落论证、结论校准和总体可读性，分档较粗且存在上限效应。本次细化了信息落点、句内负荷、主题连接、具体搭配和限定重复，不能把新编辑建议解释为旧稿存在重大科学错误。

## 具体改写示范

以下原句来自本项目的生成练习，修改句为本次编辑示范，均不是Nature/AM作者原句，也不是新增一轮技能自动生成结果。事实依据沿用原练习事实包；本次没有给正文补造新图号。

**1．把空泛的方法引导合入具体发现（Z3.1–Z3.2）。**

原句：
> Molecular dynamics (MD) simulations provided a structural interpretation of these observations. The solvent-separated ion-pair fraction decreased from 72.57% in SE to 50.41% in DE and 41.82% in HDE.

修改：
> Molecular dynamics (MD) simulations predicted a decrease in the solvent-separated ion-pair fraction from 72.57% in SE to 50.41% in DE and 41.82% in HDE.

模型身份、三个数值及比较方向均保留，读者更早看到实际结果。这借鉴的是模型—量—比较的组织方式，不是Nature论文中的锂体系机制。

**2．按比较任务拆句，不按固定词数拆句（Z3.3）。**

修改：
> The AGG fraction increased from 3.96% in SE to 33.07% in DE, then decreased to 25.45% in HDE. By contrast, the CIP fraction increased from 16.52% in DE to 32.73% in HDE.

原句包含的AGG非单调趋势和DE→HDE的CIP比较被分别展开；没有声称SE→DE的CIP同向变化，也没有把模型比例改成Raman拟合占比。相邻的HDE综合句可继续保留。

**3．压缩通用铺垫，保留决定解释范围的模型假设（S2.1–S2.3）。**

修改：
> Finite-element simulations with randomly distributed Si spheres and linear-elastic behavior predicted lower, more uniform von Mises stresses in the elastic electrolyte than in Li₆PS₅Cl during lithiation-induced expansion. The modeled redistribution is consistent with reduced mechanical disruption and improved contact preservation.

这一版本保留“预测”与“相符”的层级。后续关于非共价键断裂未直接观测、配方/加工/对电极不匹配的限定仍须保留，不能因压缩此处而消失。

**4．把段落关系写具体，再删除重复收束（S3）。**

原段首只说电化学结果把解释置于具体构型中；具体的接触—循环关系到段末才出现。可将关系前置，随后给分构型证据，并保留时间边界：

> The cycling results are consistent with contact preservation contributing to stability under the reported conditions. At 25 °C without additional pressure, the reported capacity retention of Li||Si coin cells was 90.8% after 300 cycles in tests at 0.2 and 0.4 C. Separately, Si||LFP coin cells delivered 151.4 mAh g⁻¹ at 0.5 C, normalized to LFP mass, with a reported capacity retention of 98.3% after 100 cycles. Their Si electrodes underwent one lithiation/delithiation cycle before full-cell assembly. However, the 20-cycle XR-CT images cannot establish uninterrupted contact throughout the longer cycling tests.

这里删除的是重复的关系句，温度、压力口径、倍率、构型、质量基准、预循环和20圈观察的时间边界均保留。数据的保持率分母未额外推定。

## 已落实到技能与剩余范围

[英文流程](../../references/english-workflow.md#对标目标期刊的句子表达)现增加明确的句子检查标准，并由[表征指南](../../references/characterization-writing.md)接入：先查事实，再查表达成熟度，修改后回查保义及整段连贯。不设置固定30词上限，不把删除限定当作语言升级，也不把单句模仿当作期刊风格验证。

原“句子—段落—文章”闭环继续适用。本次两段审查和示范不能验证全文叙事、作者真实结果质量或新规则的稳定生成效果；新规则未进行新一轮有/无技能盲测。只有拿到实际稿件及图数据后，才能对那篇稿件逐段、跨章节作出具体判断。

新增两篇PDF及来源/格式/哈希记录存放于此前的空间充足资料库，未放入技能仓库。nature-polishing本次仅借鉴保义、问题诊断和正文压缩规则；未采用其固定句长建议，也不称完成其全部流程。
