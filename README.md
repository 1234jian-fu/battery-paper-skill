# Battery Paper Skill

面向电池论文的图文逻辑、近期原文映射、中英文写作与可追溯审校技能。

从作者已有图、数据和稿件出发，保留已确认的结构和好句，根据实际材料、体系和测试选择写作路径。适用于电池材料、界面、电解液、固态体系、电极工程、器件与计算；不预设某一种导电剂、配方、固定六图或机制。

## 核心功能

- 从核心问题、有限主张与证据关系安排图段顺序，再组织句子；反查论证跳步和跨章节主张一致性。
- 句子—段落—文章三级闭环：逐句核据、每段写完立即对照实际核读的同功能论文段落并修改、全文完成后再审主线与章节衔接，修改后回填映射。
- 表征描述对标真实原始研究，区分直接观察、峰归属/拟合、模型与解释；学习证据组织方式，保留本研究条件和边界。
- 按作用分配正文、图注、方法与SI，保留改变结论的限制，减少重复测试罗列。
- 新稿默认按整篇累计至少60篇滚动近五年相关原始研究，按图和表达任务定向核读。
- 原文英文→中文含义→本稿表达的多对多映射，区分表达示范与正式引用。
- 机理解释M、技术描述/证据T、衔接组织L分类（方法与结果分子类），说明每句用途、前后关系及改写操作。
- 中文审阅和英文重构，保护材料状态、物理量、条件、比较方向及判断强度。
- 最后一次学术自然化后回填报表，最终句表与正文逐字一致。
- 项目接续、确认/候选版本、作者取舍和锁定范围；局部修改不重跑全流程。

默认交付：**报表包→简短逻辑总结→干净正文**。图注任务另附图注并分别计数。

## 安装到Codex

仓库根目录就是完整Skill。将它放在Codex的技能目录下，文件夹名为battery-paper-skill。

PowerShell示例（已设置CODEX_HOME时使用该目录，否则使用用户目录下.codex）：

~~~powershell
$skillBase = if ($env:CODEX_HOME) { Join-Path $env:CODEX_HOME 'skills' } else { Join-Path $env:USERPROFILE '.codex/skills' }
git clone https://github.com/1234jian-fu/battery-paper-skill.git (Join-Path $skillBase 'battery-paper-skill')
~~~

克隆目标已存在时，先检查其内容，避免覆盖本地修改。自动发现行为由宿主环境决定，也可在对话中显式指明SKILL.md路径。

## 使用

在对话中调用：

~~~text
使用 $battery-paper-skill。
先读取我的当前稿和图，保留已确认结构，一幅图一幅图写。
先给图间/图内逻辑及逐句原文映射，再给正文和图注。
~~~

也可以只要求“检查这一段”“翻译这部分”“修改图注”或“按确认稿合稿”。只有实际进行新稿/实质重构时才建立完整近期基底；单句纠错不要求重读60篇。

## 目录

~~~text
SKILL.md                        入口、模式、S01–S12、保护与交付
agents/openai.yaml              显示名称与默认提示
references/
  argument-design.md            科学问题、主张证据、图段顺序、正文取舍与反向审查
  characterization-writing.md   表征专业表达、真实论文组织动作与证据边界
  workflow.md                   执行交接和各部分职责
  field-routing.md              电池体系与研究部件路由
  battery-language-library.md   常见测试的语言动作和证据边界
  recent-corpus-policy.md       60篇资格、日期、去重和核读状态
  context-and-mappings.md       项目记录与接续
  output-contract.md            九项逐句报表与最终交付
  english-workflow.md           英文重构与保义
  skill-integration.md          规则借鉴、可选调用及自建功能
scripts/paper_workbench.py       标准库辅助检查
tests/test_paper_workbench.py   可搬运的合成测试
evals/real-paper/              两案三组真实论文局部写作对照与匿名评审记录
docs/                           schema、验证范围与设计说明
~~~

## 辅助命令

Python仅使用标准库，不安装额外依赖。以下命令从Skill根目录（SKILL.md所在目录）执行；在其他目录调用时，使用加引号的脚本绝对路径。PROJECT为已存在的论文项目目录，AS_OF为客户端日期或作者指定的截止日，格式YYYY-MM-DD。

~~~text
python scripts/paper_workbench.py init --project-dir PROJECT --name NAME --domain DOMAIN
python scripts/paper_workbench.py status --project-dir PROJECT
python scripts/paper_workbench.py sources --project-dir PROJECT --query "KEYWORDS" --as-of AS_OF
python scripts/paper_workbench.py corpus --project-dir PROJECT --as-of AS_OF
python scripts/paper_workbench.py count --file DRAFT
python scripts/paper_workbench.py check --project-dir PROJECT
python scripts/paper_workbench.py delivery-check --project-dir PROJECT --file DELIVERY_JSON
python -X utf8 -m unittest discover -s tests -p "test_*.py" -v
~~~

所有辅助命令均不联网；sources仅筛选本项目已有sources.json，不搜索、下载论文或自动建立60篇文献库。实际检索和核读由当前环境可用工具完成。

初始化只补缺，不覆盖已有记录。无明确作者变更依据的旧政策会被报告为needs_policy_update，不静默改成新政策；作者自定数量或时窗须记录明确决定，脚本分别报告默认与实际有效政策。按对应命令--help查看参数；完整示例见[helper schema](docs/helper-schema-and-tests.md)。

## 依赖与边界

Skill内置领域规则与流程。Nature、ARS、SciPilot、humanizer等技能可用时按任务调用，不要求全部安装；缺失时记录范围并使用内置适用规则。实际调用、借鉴规则和新组织分开报告。

本仓库**没有捆绑60篇已核读论文或任何用户实验数据**。通用中英结构示意明确为自拟，不是文献原句。表征指南另列两篇真实论文的独立组织分析，注明来源和实际核读范围；不捆绑论文全文或原图。实际文献和图数据在每个项目中另行建立；脚本测试夹具均为synthetic，不代表真实研究。

下载文献时先检查可用空间，在作者指定位置或空间充足的本地资料库保存全文与SI；项目账本只记录路径和来源，不把大文件塞入Skill安装目录。获取、格式验证和实际阅读分别记录。

记录完整性、数字守恒或句表一致性检查不能证明科学正确、实际阅读或语义保留。语言风格、科学贡献与期刊接收分别判断，不承诺顶刊录用或AI检测结果。

## 设计与验证

见[设计与规则分工](references/skill-integration.md)、[验证范围](docs/validation.md)和[辅助测试结果](docs/helper-test-summary.json)及[逻辑审查与修复](docs/logic-audit.md)。

本轮补齐句子—段落—文章三级审查及表征写作指南，并完成[真实论文局部写作对照](evals/real-paper/README.md)：
实际核读两篇论文的相关主文、方法、图注与实图，比较无技能、上游原版和优化版，取得6份有效正文及两位独立模型评审的盲评记录。
最初6次文件读取运行因环境策略失败，已排除；有效比较采用显式文本注入，不代表已验证自动触发或按需读文件。

三组均保留关键事实与证据边界，优化版在固态案例的论证连接上表现较好，锌案例则接近评分上限并存在局部可读性分歧。
这是两个开发案例、每组每案一次的局部验证，不保证显著质量提升；尚无未见样本泛化、完整真实稿件端到端或多轮自动触发验证。

另已补读Nature正刊和Advanced Materials原始研究，完成两段试写的[34句表达复核与改写示范](evals/style-audit/README.md)。英文规则据此强化信息落点、主题连接及限定去重；这是非盲编辑审读，未替换原对照分数，也不等于已证明稳定达到目标期刊发表水准。
