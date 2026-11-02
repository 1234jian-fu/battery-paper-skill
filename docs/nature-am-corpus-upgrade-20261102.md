# 2026-11-02：新增真实 Nature / AM 来源与写作升级

本批新增2篇、2个唯一DOI，总库53篇；不是一次完成200篇，也不把下载或摘要阅读计为正文核读。

| 卡片 | 来源 | 完整保存 |
|---|---|---|
| [B53](../references/corpus/b53.md) | Nature：Marcus kinetics control singlet and triplet oxygen evolving from superoxide；10.1038/s41586-025-09587-7 | 18页正文（含Extended Data）；4件XLSX Source Data；38页Peer Review File |
| [B54](../references/corpus/b54.md) | Advanced Materials：Solid Polymer Electrolyte with Compatible Cathode-Electrolyte Interfacial Design…；10.1002/adma.202501659 | 12页正文；SI DOCX；3段补充视频 |

原文与9件独立附件保存在外部资料库 `E:/ResearchLibrary/battery-paper-skill-benchmark` 的DOI目录，不提交Git。来源为出版社附件列表与NIH/NLM的PMC开放云数据；记录源URL、版本元数据、官方MD5以及本地SHA256。PDF验证文件头、EOF、解析页数；Office附件验证ZIP CRC与核心XML；MP4验证完整顶层容器结构。视频未观看，源数据未重算；实际核读范围以卡片为准。审稿文件只核对身份，不冒充科学SI；Nature的扩展数据在主PDF内。

## 本批实际改动

- 新增[原文对照分析](../references/nature-am-evidence-study.md)，明确定位、组织动作和两段独立英文重述，与合成教学示例分开。
- 分部指南补入引言缺口到判别实验、方法条件到结果解释、摘要与结论的对象一致性。
- 句子指南加强信号、推算量和机制判断的区分，以及比较方向和条件归属。
- 段落指南加强“前一项证据留下什么问题、下一项证据回答什么”的推进。
- 表征与审查指南加入真实主文—SI冲突：B54 §2.1蓝移措辞与SI Fig.S5红移说明不一致，该判断不作为无争议表达来源。

## 对既有记录的校正

本轮工作前已有B35附件补全草稿。保留其新增文件，经全库哈希校验及SI物理页5、25、31、35–36重新核读，修正印刷页和物理页混用；4件附件状态改为完整。B34仍有2件视频待补，恢复为partial，不把其他论文补全误计到它。旧工作区文件先另存备份。

另一个候选 `10.1038/s41586-025-09565-z` 仅取得57页SI，正文获取受阻，已存外部pending记录；不入库、不计篇数、不据其SI生成写作规则。

## 验证范围

目录/DOI去重、全部已登记正文与附件哈希、技能结构和现有自动测试用于检查记录与工具一致性；不证明论文科学结论全部正确，也不代表生成稿件自动达到期刊录用水平。本批没有复现实验、拟合或原始数据处理。

实际结果：全库53篇目录及归档哈希检查通过；技能结构校验通过；68项现有测试全部通过（21.305秒）。
