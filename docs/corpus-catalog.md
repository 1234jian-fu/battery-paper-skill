# 通用语料目录

`references/corpus/catalog.json` 保存已核验并核读的原始研究，`records` 是唯一公开计数来源。它独立于具体论文项目的 `sources.json`：进入通用库不等于满足任意新稿的相关性和近五年要求。

## 字段

根对象含 `schema_version: 1` 和 `records`。每条记录：

| 字段 | 含义 |
|---|---|
| `id`, `doi`, `title`, `journal`, `first_online` | 稳定 ID、唯一 DOI 与已核对的正式元数据 |
| `article_type` | 当前入库值为 `original_research` |
| `article_url`, `pdf_url` | 官方论文入口与合法正文来源 |
| `relative_pdf_path`, `sha256`, `pages` | 外部资料库相对路径、正文哈希、实际 PDF 页数 |
| `metadata_verified`, `pdf_verified`, `relevant_body_read` | 三个独立布尔记录，入库时均须为真；布尔值不能替代其对应证据 |
| `topic`, `methods`, `read_scope`, `structure_survey` | 任务标签、方法列表、实际阅读定位、是否做了篇级组织通览 |
| `added_on`, `card` | 本地入库日期与仓库内阅读卡相对路径 |
| `si` | `status` 为摘要；`files` 仅列完整下载并验证的文件及 `path` / `sha256`；待补来源另记 `pending` |
| `source_note`（可选） | 更正、版本和来源限制，不静默消除冲突 |

SI 状态示例：`downloaded`、`partial`、`pending_access`、`legacy_not_audited`。下载与核读分开；具体阅读范围在卡片和附件记录中声明。候选、仅摘要和下载失败记录留在外部批次清单，不放进已核读目录。

## 命令

在技能根目录执行：

```text
python scripts/corpus_catalog.py check
python scripts/corpus_catalog.py search --query XAS --limit 5
python scripts/corpus_catalog.py search --journal "Nature" --structure-only
python scripts/corpus_catalog.py render
```

`check` 检查 DOI/ID 唯一性、必要字段、状态类型、日期和阅读卡位置；加 `--archive-root` 并传入本机资料库根目录时，还核对正文文件头/结束标记与正文、已下载 SI 的哈希。该检查不联网，不验证科学真实性、不替代 PDF 解析或实际阅读，也不保证附件列表穷尽。

`search` 按标题、任务、DOI 和方法做本地文本匹配；多个空格分隔词须同时匹配。`--journal` 精确匹配期刊名，`--structure-only` 限制到已记录篇级通览的卡。默认返回10条；不自动宣称它们适合当前稿件。

`render` 更新总索引、每页最多50条的分页目录，以及 README 的当前数量、既有期刊卡统计和篇级通览数量。新增期刊须人工补充 README 的期刊展示；完整期刊分布总是以总索引为准。历史评测报告和扩库批次报告不会被重写。缩小目录时需人工审阅并处理不再使用的旧分页，不自动删除文件。

脚本只使用标准库，已验证环境为 Python 3.14.7。维护者先保存实际获取与核读证据，再录入目录；不得靠将状态改为真来代替实际工作。
