# 真实论文语料索引

当前已收录 **31 篇唯一原始研究**；持续扩库目标为 **1000 篇**。计入论文均有正式元数据、正文 PDF 校验及相关正文核读记录。来源和所读副本版本分别保留；阅读卡不等于本轮亲读原文。

## 按任务查找

先按研究对象、测量方法和写作任务筛选少量最相关卡片，再核读原文及必要上下文。可使用本地工具，避免将整库加载到上下文：

```text
python scripts/corpus_catalog.py search --query XAS --limit 5
python scripts/corpus_catalog.py search --journal "Nature" --structure-only
python scripts/corpus_catalog.py check
```

查询词以空格分隔时须同时匹配；这是本地索引检索，不联网，不判断科学真实性或当前稿件适配性。

## 分页目录

- [B01–B32](corpus/index-001.md)

## 期刊分布

| 期刊 | 篇数 |
|---|---:|
| Advanced Energy Materials | 6 |
| Advanced Materials | 4 |
| Nature | 7 |
| Nature Communications | 10 |
| Nature Energy | 4 |

## 句子、段落与全文的使用范围

- **句子：** 按同一测量对象和证据功能选择，学习对象、条件、观察、比较与限定的组织，用自己的数据重建。
- **段落：** 核读同功能段及上下文，比较主信息、证据顺序和推断边界；按[审查协议](review-protocol.md)实际修改并回填映射。
- **全文：** 已有篇级组织通览记录共 16 篇：[B05](corpus/b05.md)、[B09](corpus/b09.md)、[B14](corpus/b14.md)、[B16](corpus/b16.md)、[B17](corpus/b17.md)、[B19](corpus/b19.md)、[B21](corpus/b21.md)、[B22](corpus/b22.md)、[B23](corpus/b23.md)、[B24](corpus/b24.md)、[B25](corpus/b25.md)、[B26](corpus/b26.md)、[B27](corpus/b27.md)、[B29](corpus/b29.md)、[B30](corpus/b30.md)、[B32](corpus/b32.md)。当前任务仍须读足够正文；通览不等于 SI 全读或实验复现。

## 存储、补充材料与维护

全文与 SI 独立归档在作者指定的外部资料库，公共仓库只存元数据、阅读卡、定位和独立概括。SI 的下载与核读分开记录；历史来源的 SI 尚待补齐时不冒称已完成。

通用库不自动计为新稿至少60篇滚动近五年的专属基底；仍须检查日期、相关性和当前表达任务。局部修改不先重建文献库。

[机器可读目录](corpus/catalog.json) · [持续升级与验收](../docs/corpus-growth.md) · [结构化字段](../docs/corpus-catalog.md) · [历史验证范围](../docs/validation.md)
