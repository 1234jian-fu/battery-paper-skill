"""Search and render the public reading catalog; no network or scientific grading."""
import argparse
import hashlib
import json
import os
import re
from collections import Counter
from datetime import date
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "references/corpus/catalog.json"


def doi_key(value):
    return re.sub(r"^https?://(?:dx\.)?doi\.org/|^doi:\s*", "", value.strip(), flags=re.I).lower()


def relative_file(base, value):
    path = Path(value)
    if path.is_absolute() or re.match(r"^[A-Za-z]:", value) or ".." in path.parts:
        raise ValueError(f"Not a safe relative path: {value}")
    target = (base / path).resolve()
    if not target.is_relative_to(base.resolve()):
        raise ValueError(f"Path escapes root: {value}")
    return target


def markdown_relative_link(source_dir, target):
    return quote(Path(os.path.relpath(target.resolve(), source_dir.resolve())).as_posix(), safe="/")


def validate(data, root=ROOT, archive=None):
    if data.get("schema_version") != 1 or not isinstance(data.get("records"), list):
        raise ValueError("Expected schema_version=1 and records list")
    ids, dois = set(), set()
    for r in data["records"]:
        for key in ("id", "doi", "title", "journal", "first_online", "article_url", "pdf_url",
                    "relative_pdf_path", "sha256", "topic", "read_scope", "card"):
            if not isinstance(r.get(key), str) or not r[key].strip():
                raise ValueError(f"Missing {key}: {r.get('id')}")
        sid, doi = r["id"], doi_key(r["doi"])
        if not re.fullmatch(r"B\d{2,}", sid) or sid in ids:
            raise ValueError(f"Invalid/duplicate ID: {sid}")
        if not re.fullmatch(r"10\.\d{4,9}/\S+", doi) or doi in dois:
            raise ValueError(f"Invalid/duplicate DOI: {doi}")
        if r.get("article_type") != "original_research":
            raise ValueError(f"Not original research: {sid}")
        if any(r.get(k) is not True for k in ("metadata_verified", "pdf_verified", "relevant_body_read")):
            raise ValueError(f"Unverified record cannot enter reading catalog: {sid}")
        date.fromisoformat(r["first_online"])
        date.fromisoformat(r["added_on"])
        if r["first_online"] > r["added_on"]:
            raise ValueError(f"Publication date is after reading date: {sid}")
        if not isinstance(r.get("structure_survey"), bool) or not isinstance(r.get("methods"), list):
            raise ValueError(f"Invalid reading scope fields: {sid}")
        if type(r.get("pages")) is not int or r["pages"] < 1 or not re.fullmatch(r"[0-9a-fA-F]{64}", r["sha256"]):
            raise ValueError(f"Invalid PDF evidence: {sid}")
        if not all(re.match(r"https?://", r[k]) for k in ("article_url", "pdf_url")):
            raise ValueError(f"Invalid source URL: {sid}")
        card = relative_file(root, r["card"])
        if not card.is_file() or doi not in card.read_text(encoding="utf-8").lower():
            raise ValueError(f"Card missing or DOI mismatch: {sid}")
        if not isinstance(r.get("si"), dict) or not r["si"].get("status"):
            raise ValueError(f"Missing SI status: {sid}")
        relative_file(root, r["relative_pdf_path"])
        if archive:
            pdf = relative_file(archive, r["relative_pdf_path"]).read_bytes()
            if not pdf.startswith(b"%PDF") or b"%%EOF" not in pdf[-4096:]:
                raise ValueError(f"Invalid archived PDF: {sid}")
            if hashlib.sha256(pdf).hexdigest() != r["sha256"].lower():
                raise ValueError(f"Archived hash mismatch: {sid}")
            for f in r["si"].get("files", []):
                content = relative_file(archive, f["path"]).read_bytes()
                if hashlib.sha256(content).hexdigest() != f["sha256"].lower():
                    raise ValueError(f"SI hash mismatch: {sid}")
        ids.add(sid); dois.add(doi)
    return sorted(data["records"], key=lambda r: int(r["id"][1:]))


def summary(records):
    return {"verified_reading_cards": len(records), "unique_dois": len({doi_key(r['doi']) for r in records}),
            "journal_counts": dict(sorted(Counter(r["journal"] for r in records).items())),
            "structure_survey_ids": [r["id"] for r in records if r["structure_survey"]],
            "si_status_counts": dict(sorted(Counter(r["si"]["status"] for r in records).items()))}


def search(records, query="", journal=None, structure_only=False, limit=10):
    terms = query.casefold().split()
    result = []
    for r in records:
        haystack = " ".join([r["title"], r["topic"], r["doi"], *r["methods"]]).casefold()
        if all(t in haystack for t in terms) and (not journal or journal.casefold() == r["journal"].casefold()) and (not structure_only or r["structure_survey"]):
            result.append(r)
    return result[:limit]


def render(records, root=ROOT):
    stats = summary(records)
    ref = root / "references"
    page_links = []
    for start in range(0, len(records), 50):
        chunk = records[start:start + 50]
        name = f"index-{start // 50 + 1:03}.md"
        page_links.append(f"- [{chunk[0]['id']}–{chunk[-1]['id']}](corpus/{name})")
        lines = [f"# 语料目录 · {chunk[0]['id']}–{chunk[-1]['id']}", "", "[返回总索引](../literature-corpus.md)", "",
                 "| 阅读卡 | 期刊 / 首次在线 | 写作任务与方法 | 阅读层级 |", "|---|---|---|---|"]
        for r in chunk:
            clean = lambda s: str(s).replace("|", "\\|").replace("\n", " ")
            card_link = markdown_relative_link(ref / "corpus", relative_file(root, r["card"]))
            lines.append(f"| [{r['id']} · {clean(r['title'])}]({card_link}) | {r['journal']} / {r['first_online']} | {clean(r['topic'])}；{clean(' / '.join(r['methods']))} | {'局部＋篇级通览' if r['structure_survey'] else '相关正文'} |")
        (ref / "corpus" / name).write_text("\n".join(lines) + "\n", encoding="utf-8")
    macro = "、".join(
        f"[{r['id']}]({markdown_relative_link(ref, relative_file(root, r['card']))})"
        for r in records if r["structure_survey"])
    lines = ["# 真实论文语料索引", "", f"当前已收录 **{len(records)} 篇唯一原始研究**；持续扩库目标为 **1000 篇**。计入论文均有正式元数据、正文 PDF 校验及相关正文核读记录。来源和所读副本版本分别保留；阅读卡不等于本轮亲读原文。", "",
             "## 按任务查找", "", "先按研究对象、测量方法和写作任务筛选少量最相关卡片，再核读原文及必要上下文。可使用本地工具，避免将整库加载到上下文：", "", "```text", "python scripts/corpus_catalog.py search --query XAS --limit 5", 'python scripts/corpus_catalog.py search --journal "Nature" --structure-only', "python scripts/corpus_catalog.py check", "```", "", "查询词以空格分隔时须同时匹配；这是本地索引检索，不联网，不判断科学真实性或当前稿件适配性。", "",
             "## 分页目录", "", *page_links, "", "## 期刊分布", "", "| 期刊 | 篇数 |", "|---|---:|"]
    lines += [f"| {j} | {n} |" for j,n in stats["journal_counts"].items()]
    lines += ["", "## 句子、段落与全文的使用范围", "", "- **句子：** 按同一测量对象和证据功能选择，学习对象、条件、观察、比较与限定的组织，用自己的数据重建。", "- **段落：** 核读同功能段及上下文，比较主信息、证据顺序和推断边界；按[审查协议](review-protocol.md)实际修改并回填映射。", f"- **全文：** 已有篇级组织通览记录共 {len(stats['structure_survey_ids'])} 篇：{macro}。当前任务仍须读足够正文；通览不等于 SI 全读或实验复现。", "", "## 存储、补充材料与维护", "", "全文与 SI 独立归档在作者指定的外部资料库，公共仓库只存元数据、阅读卡、定位和独立概括。SI 的下载与核读分开记录；历史来源的 SI 尚待补齐时不冒称已完成。", "", "通用库不自动计为新稿至少60篇滚动近五年的专属基底；仍须检查日期、相关性和当前表达任务。局部修改不先重建文献库。", "", "[机器可读目录](corpus/catalog.json) · [持续升级与验收](../docs/corpus-growth.md) · [结构化字段](../docs/corpus-catalog.md) · [历史验证范围](../docs/validation.md)"]
    (ref / "literature-corpus.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    readme = root / "README.md"
    body = readme.read_text(encoding="utf-8")
    body = re.sub(r"Corpus-\d+_original_papers", f"Corpus-{len(records)}_original_papers", body)
    body = re.sub(r"Corpus: \d+ original papers", f"Corpus: {len(records)} original papers", body)
    body = re.sub(r"\*\*\d+ 篇真实原始研究 · \d+ 种期刊 · 按写作任务选读\*\*", f"**{len(records)} 篇已核读原始研究 · 目标 1000 篇 · 按写作任务选读**", body)
    body = re.sub(r"\*\*\d+ 篇已核读原始研究 · 目标 1000 篇 · 按写作任务选读\*\*", f"**{len(records)} 篇已核读原始研究 · 目标 1000 篇 · 按写作任务选读**", body)
    body = re.sub(r"(<strong>([^<]+)</strong><br>)\d+ 篇",
                  lambda m: f"{m[1]}{stats['journal_counts'].get(m[2], 0)} 篇", body)
    body = re.sub(r"<strong>\d+ 篇来源</strong>", f"<strong>{len(records)} 篇来源</strong>", body)
    body = re.sub(r"\*\*\d+ 篇均有相关正文阅读记录，其中 \d+ 篇另有主文组织通览\*\*", f"**{len(records)} 篇均有相关正文阅读记录，其中 {len(stats['structure_survey_ids'])} 篇另有主文组织通览**", body)
    body = re.sub(r"literature-corpus.md( +)\d+ 篇真实论文索引", r"literature-corpus.md\1真实论文分页索引", body)
    readme.write_text(body, encoding="utf-8")


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("command", choices=["check", "search", "render"])
    p.add_argument("--catalog", type=Path, default=DEFAULT)
    p.add_argument("--archive-root", type=Path)
    p.add_argument("--query", default="")
    p.add_argument("--journal")
    p.add_argument("--structure-only", action="store_true")
    p.add_argument("--limit", type=int, default=10)
    args = p.parse_args()
    if args.limit < 1:
        p.error("--limit must be positive")
    records = validate(json.loads(args.catalog.read_text(encoding="utf-8-sig")), archive=args.archive_root)
    if args.command == "render":
        render(records)
    result = search(records, args.query, args.journal, args.structure_only, args.limit) if args.command == "search" else summary(records)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
