# 项目记录、版本和辅助命令

Skill只保存方法，不自带用户研究的实验事实。每稿的工作目录用.paper-writing/保存状态；不复制其他项目事实，不移动原始图/PDF，不覆盖稿件。无记录时从可见对话恢复并注明未知，不声称恢复不可见历史。

## 文件与状态

| 文件 | 内容 |
|---|---|
| project.json | 研究方向、当前任务、语言、范围、锁定项、术语、阶段、政策、下一步 |
| evidence.json | 当前图和原始表、版本/哈希、对象/状态/构型、指标/单位、来源和支持范围 |
| sources.json | 本项目来源、身份/日期核验、实际阅读位置、中文义和借鉴动作 |
| decisions.md | 接受/拒绝、已确认结构和好句、修改原因、问题回答 |
| issues.md | 冲突来源、影响句/结论、回答与验证状态、下一步 |
| drafts/ | 候选/确认段落、图注、逐句报表和交付记录，按部分与版本保存 |

初始化仅新建缺失项，保留已有记录。默认corpus_policy为minimum=60,target=60,recent_years=5；旧项目不自动改写，明确报告needs_policy_update，由已授权的政策迁移同步并留下决定。作者明确改用其他数量/时窗时，另记录corpus_policy_override的authorized_by=user和非空decision_ref；脚本仅据记录采用自定政策，不验证用户授权真实性。

.paper-writing、必要记录文件和drafts经解析后须在显式PROJECT内，指向项目外的符号链接或目录联接会被拒绝；项目内链接仍可用。check要求必要记录为文件，不把同名目录当成有效记录。

阶段：scoped→evidence_mapped→sources_mapped→drafted→checked→author_accepted→assembled；新证据影响旧稿可标needs_recheck并保留旧接受记录。checked仅表示所记录检查范围完成，不等于实验证实、全文无误或作者接受。各小节状态独立。

锁定项按部分ID、原文/正文哈希、源版本、允许范围与作者依据记录；锁定引言不应使用整个docx哈希阻止修改讨论。

## 证据、术语与问题

证据卡至少记录evidence_id、图/子图、源文件与版本、材料名、状态、构型、电极角色、测试条件、物理量、数值/单位/精度、来源、支持/不支持什么、派生关系和核验状态。

来源身份区分raw_record、figure_label、author_reported、author_confirmed、author_memory、calculation_output。author_confirmed只表示作者明确确认，不代表已核验原始文件。value未知可空。派生值写公式、输入及基准；同一测量的派生量不当独立证据。云图记录实际场变量、色标、归一化和显示规则。

术语卡包含规范名、中文/英文、图标签、状态后缀、单位、别名及适用范围。连接符按已定义体系与期刊格式保持，不随润色换名。新项目不承袭旧项目命名。

问题用ID、来源冲突、影响结论、依赖级别、回答、核查结果、采用方式和状态。open/answered/resolved/deferred/superseded分开；回答但未验证不能标无争议实测。问已知上下文没有答案且影响当前工作的问题，其余继续推进。

## 来源与阅读记录

sources.json为对象，items是来源卡列表。计数最低字段见[近期政策](recent-corpus-policy.md)。每条有source_id；读过什么留read_scope、exact_locations、中文义、段落动作和数据表达；核验身份和日期另记。

read_scope可用metadata_only、secondary_record_only、abstract、relevant_body、full_main_text、full_main_and_SI、unknown。获取文件不等于阅读；只读旧卡标secondary_record_only，继承记录不冒称本轮亲读。可复用可追溯且仍有效的核读，不要求每图从头通读。

自己的观察、来源结构、文献事实和作者组织分开；方法或原稿来自作者提供/确认时可用author_provided/author_confirmed记录，不强行归为实测观察，也不等于原始数据已核验。正式引用与表达示范来源分栏。必要短摘连续、准确、定位明确，遵循来源使用限制。

### 全文与补充材料的存放

下载前检查作者指定位置和实际剩余空间；没有指定时，选择可用空间充足、适合长期保存的本地资料库，在独立的任务子目录下按DOI或稳定来源ID归档。位置是本机运行决定，不把某个盘符写成跨设备默认。原始文件不要放Skill安装目录或提交到技能Git仓库；项目内保留索引，来源文件可合法位于项目外，不能为此把受保护的.paper-writing目录链接到项目外。

每个获取文件记录source_id、下载入口、获取日期、实际路径、格式、文件大小、SHA256、许可/访问方式及下载状态。确认响应实际是PDF/XML/HTML，而非把登录页保存成PDF；PDF失败但XML全文可用时如实记录格式。全文、SI、Source Data分别标识，下载成功不等于已经核读。通过出版社、开放仓库或作者已授权的访问渠道获取；不能绕过付费墙、登录或安全拦截。复用有效副本避免重复下载；不移动或删除作者已有原件。

## 辅助命令

以下python表示已经可用的解释器，示例从Skill根目录（SKILL.md所在目录）执行。从其他目录调用时，把scripts/paper_workbench.py替换为该脚本的绝对路径并加引号；PROJECT仍指论文项目，不是Skill安装目录。所有项目命令显式指定PROJECT，日期相关命令显式传入客户端截止日；AS_OF格式YYYY-MM-DD，不靠执行主机的日期推断。

~~~text
python scripts/paper_workbench.py init --project-dir PROJECT --name NAME --domain DOMAIN
python scripts/paper_workbench.py status --project-dir PROJECT
python scripts/paper_workbench.py sources --project-dir PROJECT --query "KEYWORDS" --as-of AS_OF
python scripts/paper_workbench.py corpus --project-dir PROJECT --as-of AS_OF
python scripts/paper_workbench.py count --file DRAFT
python scripts/paper_workbench.py check --project-dir PROJECT
python scripts/paper_workbench.py delivery-check --project-dir PROJECT --file DELIVERY_JSON
~~~

count可按start-marker/end-marker限定正文；完整参数用相应命令--help查看。正文与图注分别计数，默认去空白字符数含英文/标点，另列汉字数；英文另列词数。分句程序不是科学质量评价。

所有辅助命令均不联网。sources只筛选本项目已有sources.json，不能检索或下载新论文，也不会自动建立60篇基底；需要新来源时另用可用检索工具并核读原文。

init不覆盖现有内容；status/check为记录结构检查；corpus按来源卡声明的核验与阅读字段统计，不能证明确实读懂、日期真实或研究相关；重复来源ID和无效结构不能被数量达标掩盖。delivery-check比较交付JSON内部的最终句表和段落及ID引用，不能验证语义，也不自动读取实际Markdown/Word交付，另存正文须再逐字核对。若旧项目政策不同，报告差异而不静默升级。

结束当前任务前保存当前源版本、确认稿、候选、未决问题、保护范围、下一步。下次从此继续，不重复全部检索和问答。
