# 本次安装与优化验证：2026-10-30

来源：`1234jian-fu/battery-paper-skill`，上游提交
`239299de2d28e6ce1dc2687f9de36e3dbfa93851`。以下结果对应在该提交上完成的修订。
运行环境为 Windows、Python 3.14.7；脚本与测试哈希见
[helper-test-summary.json](helper-test-summary.json)。

## 写作逻辑优化

新增[论证设计](../references/argument-design.md)，并接入S03、S04和S11：
先确定核心问题及有范围的主张，检查本研究证据、推理前提与限制，再安排图段和句子。
按作用分配正文、图注、方法与SI，最后从实际正文反查主张、证据和跨章节一致性。
保留原有每稿60篇默认、已确认结构、逐句追溯及局部任务范围，不引入新的强制审批步骤。

本轮进一步补齐句子—段落—文章三级审查：逐句核对来源、条件和判断强度；
每段写完后，对照实际核读的同功能论文段落，按需要实质修改并回填来源映射；
全文完成后用反向提纲检查主线、章节职责和跨章节一致性，再对照实际核读论文的篇级结构进行修改。
新增[表征写作指南](../references/characterization-writing.md)，区分直接观察、峰归属与拟合、
模型结果及机制解释，并用两篇真实论文分析表征如何服务于论证。
这些规则已纳入技能；下述局部正文评测不等于验证了整篇稿件的所有内部审查动作。

入口另明确已有合稿授权、用户指定交付格式、同源累计摘录限额、脚本路径和本地账本功能。

## 脚本修复与实际检查

- 修复外部记录路径链接越界、无效日期入口误计、无效首次在线日期回退、长别名链递归崩溃，以及目录冒充必要记录文件共5类问题。
- 原版50项测试通过；修复后59项测试通过（新增9项），无失败或跳过。
- 确定性黑盒评测通过8/8检查、115/115断言，`cases_without_checks=0`；手算预期与边界见[evals说明](../evals/README.md)。
- Skill结构校验、文档相对链接和`git diff --check`通过。

## 合成场景独立试用

两个未获知预期答案的独立代理使用修订后的Skill完成3个合成任务，主代理阅读实际产物：

1. 固态电池论证重组：将5 MPa下优势及1 MPa下反向表现共同纳入主线；区分2 MPa放空态形貌与5 MPa、50% SOC阻抗，未拼接成同状态演变；拒绝由二维信号和单一路径DFT宣称普遍三维网络机制。
2. 局部英文修改：把错误的“增加3.0”改为“为3.0、对照2.0”，保留25 °C与HC-X，删除未测的电子传输及普遍稳定性结论；按要求未检索或展开报表。
3. 已授权合稿：直接输出3段确认稿，段间仅空一行、锁定引言逐字保留，不纳入否决候选；实际文本与预期拼接逐字比较通过。

上述是定性、单次、合成场景验证，与下面的真实论文局部写作对照分别记录，不混算样本。

## 真实论文局部写作对照

已实际核读两篇原始研究的相关主文、方法、图注及实图：
Zhang等的锌电解液研究（Nature Communications，2025）和Pan等的固态微米硅负极研究
（Nature Communications，2024）。核读范围、事实包、实际正文、运行设置和原始评审记录见
[真实论文评测说明](../evals/real-paper/README.md)。这不表示已完整核读其全部补充信息或复现研究。

两案分别比较无技能、上游原版和优化版，共**6次有效运行、6份实际英文正文**，每组每案仅一次。
同一案例使用相同事实包和任务，模型及推理档位相同，并在新会话中运行。
初始以文件读取方式进行的6次运行均因环境策略阻止读取而失败，已全部排除，未作为低分样本。
有效运行改用显式文本注入：无技能组附事实，另两组附对应技能入口及references文本；
不附评测答案或其他组输出，也未放宽原审批策略。
因此本轮比较的是显式提供规则时的局部写作输出，不是技能自动触发或按需读取文件的能力。

两个独立模型评审会话在揭盲前只读取随机标签正文、统一事实与量表，并在独立判断后核对来源组织笔记。
标签在每个案例内分别打乱；两位评审各评价6份正文，形成4份按案例保存的评审记录。
这不是外部人类专家评审。五个维度分别为事实准确性、表征专业精度、段落论证、结论校准与学术可读性，
每维0–4分；下表总分仅便于描述本次样本，分项理由和分歧以评审记录为准。

| 案例 | 组别 | 评审一 | 评审二 |
|---|---|---:|---:|
| 锌电解液 | 无技能 | 20/20 | 20/20 |
| 锌电解液 | 上游原版 | 20/20 | 20/20 |
| 锌电解液 | 优化版 | 20/20 | 19/20 |
| 固态微米硅负极 | 无技能 | 18/20 | 19/20 |
| 固态微米硅负极 | 上游原版 | 19/20 | 19/20 |
| 固态微米硅负极 | 优化版 | 20/20 | 20/20 |

三组均保留关键事实与证据边界。固态案例中，优化版的结构—力学解释—循环功能连接获得两位评审较高评价；
锌案例接近评分上限，其中一位评审认为优化版仍有局部可读性问题。
这些小样本结果不支持“写作质量显著提升”或所有任务均优于原版/无技能的结论，
也不应把可选事实未被采用当作错误。结果对应已记录的固定技能快照，不能自动覆盖后续修改。

随后针对锌段落概括笼统的问题，表征指南补充了定量总结须说明具体趋势的规则，
仅重跑优化组一次。新正文已具体区分离子对与聚集体的变化方向，主代理核对数字及方向与事实包一致。
这是非盲的开发反馈复测，没有重新打分，也未替换六份原始正文；不能由一次生成归因规则效果。
实际文本和执行记录见评测说明中的“评审反馈后的单次针对性复测”。

## 目标期刊句子表达复核

随后按作者要求对目标期刊表达作了专项复核：补读Nature和Advanced Materials的原始研究相关段落、图注及方法上下文，逐句检查两段既有输出共34句。定位及实际版本、逐句编辑判断、保义改写示范见[句子表达复核](../evals/style-audit/README.md)。Nature副本为高校公开排版稿，首页在线日期仍为占位符，未与最终版逐字比对。该复核由主代理在非盲状态下完成；新增表达规则未进行新一轮生成对照，原六份输出与分数保持不变。

## 尚未验证的范围

- 已准备20条正负触发查询并完成命令dry-run，但未运行多轮自动触发测试，不报告触发准确率。
- 两个案例参与了规则开发，事实包也明确了多项风险；没有未见论文上的泛化验证、重复采样或统计显著性分析。
- 本轮只生成300–400词的局部结果讨论，没有建设60篇新稿语料，也没有完整真实稿件从文献核读到Word合稿的端到端验证。
- 最终正文未展示内部审查表，不能据此确认句级映射、每段写后修改和全文审查的每一步均已执行。
- 未进行新实验、模拟复现、外部人类专家评审或期刊评审；脚本通过和模型评分均不证明科学真实性。

# 上游验证记录（历史）

以下内容保留自上述上游提交，所述50项测试和旧行为试用是上游历史记录，
不应与本轮新增试用混算；其中历史发布检查未在本轮重新执行。

## Validation scope

This package is a generalized battery-paper writing skill. It contains no user manuscript, experimental dataset, literature PDFs, credentials, or local project snapshot.

## Structure and helper checks

- The installed skill passed the available skill-creator structural validator.
- The portable repository helper tests were actually executed: **50 tests (22 original plus 28 logic regressions), zero failures or errors**.
- The tests cover the recorded 60-work threshold, date boundaries and precision, duplicate-source counting, non-overwriting initialization, legacy-policy warnings, ID resolution, and exact sentence-to-paragraph consistency.
- Internal documentation links and UTF-8 files were checked.
- The public package was checked for local absolute paths, credential-like tokens, and unintended manuscript/data files; no such content was selected for publication.

All test records are **synthetic**. Record assertions do not establish actual source reading, scientific relevance, or scientific validity. A passed delivery check establishes exact text/ID structure, not faithful meaning.

## Independent behavioral trials

Two agents independently read and used the skill in isolated synthetic workspaces. They were given only a realistic task and its raw input files, not an intended answer.

1. **Sulfide solid-state battery outline:** with only four figure-group descriptions, produced scoped figure/paragraph duties, preserved the requested contact-evolution → impedance → device-performance thread, and retained the introduction lock. It did not invent figures, numbers, source quotations, or completed literature reading.
2. **Hard-carbon English evidence correction:** corrected a direction error against a supplied table, retained the defined material name and hyphen, and removed unsupported electronic-conductivity and all-operating-condition conclusions. The sentence table, final paragraph, JSON, and separate prose file were actually checked for consistency; delivery-check returned exact_match=true.

These trials exercise task scoping, transfer to different battery directions, evidence boundaries, and final delivery consistency. They are not external expert peer review, experimental validation, a 60-paper corpus, or a test of journal acceptance. Full literature retrieval and manuscript-to-Word assembly were not exercised in these trials.

## Reproduce helper checks

From the repository root:

~~~text
python -X utf8 -m unittest discover -s tests -p "test_*.py" -v
~~~

No external Python packages or network are needed for the helper tests. Source-paper research and document operations use whichever authorized tools are available in the host environment.

## Subsequent logic audit

A third independent usage scenario exercised author-confirmed experimental methods with intentionally missing parameters. It exposed a basis-classification gap; the gap was corrected and its unchanged delivery records were rechecked successfully. The expanded record probes, fixes and check boundaries are documented in [logic-audit.md](logic-audit.md).
