# Nature / Advanced Materials：真实正文到写作决策

2026-11-02回到归档PDF核读，而非沿用阅读卡摘要。下列短摘仅用于定位与分析；中文说明和英文重述均为独立撰写，不是原文译文或作者新结果。用于改进技能的开发案例不能同时当作独立质量验收。

## 来源与阅读边界

| 来源 | 版本与本轮核读范围 | 图文核对与限制 |
|---|---|---|
| [B03 · Nature：Ligand-channel-enabled ultrafast Li-ion conduction](https://doi.org/10.1038/s41586-024-07045-4) | [高校公开PDF](https://bpb-us-e1.wpmucdn.com/blog.umd.edu/dist/7/477/files/2024/02/a21f7670-47bb-49ed-b24c-c65c9626dea5-17deb821140e7716.pdf)，9页；pp.1–7摘要、引言、全部主文结果与结尾，pp.8–9方法；图注Fig.1–4 | 目视pp.2、4；文件哈希与[B03卡](corpus/b03.md)一致。早期排版副本，首页在线日期占位符保留，未与最终VOR逐字比对；SI本轮未读，不独立验证其推导和补充证据 |
| [B39 · Advanced Materials：Piezoresistive Free-standing Microfiber Strain Sensor for High-resolution Battery Thickness Monitoring](https://doi.org/10.1002/adma.202212189) | [KIT公开PDF](https://publikationen.bibliothek.kit.edu/1000157998/150678391)，11页；pp.1–9摘要、引言、全部结果讨论、结论和实验部分；图注Fig.1–4 | 目视pp.7–8；文件哈希与[B39卡](corpus/b39.md)一致。KIT早期排版副本，日期差异沿用卡片记录；pp.10–11文后内容不计精读；SI未取得，不核验其图表及视频 |

页码均指所列PDF从1起的文件页序。这里完成的是主文组织通览与相关句段分析，不是实验复现、所有图像的定量核验或全文科学背书。两篇既有来源不增加语料篇数，也不据此重写既有目录的历史阅读计数。

## Nature：用不能被既有解释覆盖的比较推动研究

**可定位短摘。** p.2，溶剂筛选小节首段：`Despite having similar solvation energy`。p.3，筛选段后的实验段：`To validate the electrolyte-design criteria`。

**句子与段落。** p.2不是简单列出候选溶剂的数值：作者先给常见关系，再用溶剂化能相近却有不同解离和电导表现的成对比较，说明单个描述量不足。随后才引入迁移能垒与溶剂化壳体积。p.3的实验段接住刚提出的筛选依据；p.4机制段先给模拟任务与驻留时间，再解释局部交换并引入输运指标。读者能识别每次新增量要回答的问题。

**直接改变技能的动作。** 引言或结果需要提出新描述量时，先寻找现有证据中旧解释无法区分的比较，再定义新量及其能区分什么。没有这种比较时，按实际用途说明描述量，不编造反常现象。机制段首次引入模型量，应交代其来源及物理含义，再用它连接已见现象；避免“MD进一步证明机理”独占一句。

**宏观结构。** p.1提出输运与界面要求的矛盾；pp.2–3筛选和电导检验；p.4给出分子解释及输运指标；pp.4–5器件工况验证；pp.5–6回到界面化学；pp.6–7收束。这是两条证据线汇合：输运快与界面适配分别需要支撑。界面分析位于器件结果之后，说明“所有表征必须先于性能”并非必要结构。若按此顺序写自己的稿件，性能段应保留尚未证明的解释为待回答问题，不能提前把后文未展开的机制写成已经确证。

**不能照搬。** 原文的极端工况、模型指标及推广语气属于该研究；“超快”“普适”不能因为出现在Nature就变成默认词汇。不同构型、温度和倍率下的最佳结果不能拼成同一次器件验证。SI未核读意味着这里不能独立复核输运指标的全部推导。

**基于真实来源的英文重述练习（非引文、非新研究正文）。**

> In the solvent comparisons reported by Lu et al., similar solvation energies did not imply similar salt dissociation or ionic conductivity. The study therefore considered solvation-shell volume and a transport barrier alongside solvation energy. Conductivity measurements then tested the selected formulation, while molecular simulations examined ion exchange within its solvation environment.

对应p.2首段及后续参数定义、pp.3–4电导和模拟段。三句分别承担“比较暴露不足—增加解释维度—区分实验检验与模拟任务”；没有把模拟改成直接实测，也不复制原段全部数列。这是对已发表工作的概括，不可换材料名后作为作者原创结果。

## Advanced Materials：先建立测量资格，再解释器件信号

**可定位短摘。** p.7，§2.1的电池过程描述：`Notably, cell shrinkage starts while still charging in the CV phase`；紧随的解释入口为 `This observation leads to the assumption`。

**句子与段落。** 作者先交代器件布置、基准仪器及循环阶段，再用“仍在充电却开始收缩”组织观测，随后才提出松弛解释。pp.6–7先讨论传感器可校准范围、检测能力、响应速度与重复应变测试，§2.1才转向电池；测量能力是解释应用信号的前提。p.8 Fig.4图注将中心参考位移与边缘纤维的换算位移分开命名。

**直接改变技能的动作。** 过程表征按阶段及转折写，先说明相对于哪种预期出现差异，再提出有根据的解释。不同探针对照时，在数值或图注中保留位置、直接测量/换算身份和比较目的；时序相似可用于过程追踪，不能自动改成同位置绝对量吻合。把观测与解释分句，并不意味着每个观察都要加“可能”。

**宏观结构。** pp.1–2从电池监测需求落到传感器能力缺口；pp.2–3建立材料与结构；pp.4–5处理力学及电阻响应；pp.6–7建立可用测量范围和耐久性；pp.7–8检验电池监测；p.9回到方法价值。这条结构要求“新测量能否用”先于“由新信号能解释什么”。若当前研究使用成熟仪器，已有校准与适用性信息可简写或放方法，不照搬整套传感器开发章节。

**不能照搬。** 台架重复应变的耐久与电池循环验证属于不同层级。原文应用展望比所展示的电池循环范围更宽；本技能不把该展望升级为已完成寿命验证。信号的松弛解释也不能替代独立机理测量。

**基于真实来源的英文重述练习（非引文、非新研究正文）。**

> Nazari et al. observed a contraction during constant-voltage charging, before discharge began. They interpreted this response as relaxation outweighing expansion associated with anode lithiation. The fibre and reference measurements sampled different positions, so their comparison should distinguish agreement in the progression of the response from agreement in absolute displacement.

前两句对应p.7 §2.1的观测和作者解释；第三句是依据pp.7–8位置说明与Fig.4图注作出的编辑判断，**不是源作者的结论引文**。改写把事件、解释身份与比较边界分别说清；不将测量信号写成直接测得锂含量。

## 如何用于下一篇稿件

按当前贡献选相应动作：描述量研究采用可区分的比较，测量方法研究建立能力到应用的桥梁。只迁移适用动作，不强迫每篇都有异常现象、模型或传感器校准段。段落完成后反提实际推进关系，全文完成后核对开篇的每项承诺由哪条结果线回答。若结果改变了原承诺，应同步收紧题名、摘要和结尾；单靠添加连接词不能弥补缺失证据。
