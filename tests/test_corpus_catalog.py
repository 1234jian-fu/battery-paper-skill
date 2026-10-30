"""Synthetic cases for catalog admission; not scientific validation."""
import importlib.util
import tempfile
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location("corpus_catalog", Path(__file__).parents[1] / "scripts/corpus_catalog.py")
c = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c)


class CatalogTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "card.md").write_text("10.1234/synthetic", encoding="utf-8")
        self.record = dict(id="B01", doi="10.1234/synthetic", title="Synthetic XAS study", journal="Synthetic Journal",
            first_online="2025-01-01", added_on="2026-10-30", article_type="original_research",
            article_url="https://example.org/article", pdf_url="https://example.org/article.pdf",
            relative_pdf_path="synthetic/article.pdf", sha256="0"*64, pages=1, topic="local structure",
            methods=["XAS"], read_scope="SYNTHETIC fixture only, p.1", structure_survey=False,
            metadata_verified=True, pdf_verified=True, relevant_body_read=True, card="card.md",
            si={"status":"pending_access", "files":[]})

    def tearDown(self):
        self.tmp.cleanup()

    def check(self, records):
        return c.validate({"schema_version":1,"records":records}, self.root)

    def test_duplicate_doi_url_case_rejected(self):
        other = dict(self.record, id="B02", doi="https://doi.org/10.1234/SYNTHETIC")
        with self.assertRaisesRegex(ValueError,"duplicate DOI"):
            self.check([self.record,other])

    def test_download_only_and_string_truth_rejected(self):
        for value in (False, "true"):
            with self.assertRaisesRegex(ValueError,"Unverified record"):
                self.check([dict(self.record,relevant_body_read=value)])

    def test_wrong_card_doi_rejected(self):
        with self.assertRaisesRegex(ValueError,"DOI mismatch"):
            self.check([dict(self.record,doi="10.1234/other")])

    def test_path_escape_rejected(self):
        with self.assertRaisesRegex(ValueError,"relative path"):
            self.check([dict(self.record,card="../card.md")])

    def test_counts_do_not_infer_si_or_macro_from_body_read(self):
        stats = c.summary(self.check([self.record]))
        self.assertEqual(stats["verified_reading_cards"],1)
        self.assertEqual(stats["structure_survey_ids"],[])
        self.assertEqual(stats["si_status_counts"],{"pending_access":1})

    def test_search_requires_requested_scope(self):
        rows = self.check([self.record])
        self.assertEqual(len(c.search(rows,"XAS structure")),1)
        self.assertEqual(c.search(rows,"XAS",structure_only=True),[])
        self.assertEqual(c.search(rows,"XAS",journal="Other"),[])

    def test_archive_mismatch_rejected(self):
        folder=self.root/"synthetic";folder.mkdir()
        (folder/"article.pdf").write_bytes(b"%PDF-1.7 synthetic\n%%EOF")
        with self.assertRaisesRegex(ValueError,"hash mismatch"):
            c.validate({"schema_version":1,"records":[self.record]},self.root,self.root)

    def test_render_links_follow_card_path_in_both_indexes(self):
        (self.root / "references/corpus").mkdir(parents=True)
        (self.root / "references/custom").mkdir()
        card = "references/custom/paper (1)#x.md"
        (self.root / card).write_text(self.record["doi"], encoding="utf-8")
        (self.root / "README.md").write_text("", encoding="utf-8")
        rows = self.check([dict(self.record, card=card, structure_survey=True)])
        c.render(rows, self.root)
        page = (self.root / "references/corpus/index-001.md").read_text(encoding="utf-8")
        index = (self.root / "references/literature-corpus.md").read_text(encoding="utf-8")
        self.assertIn("](../custom/paper%20%281%29%23x.md)", page)
        self.assertIn("[B01](custom/paper%20%281%29%23x.md)", index)
        self.assertNotIn("corpus/b01.md", index)

    def test_render_zeroes_absent_journals_in_existing_readme_cards(self):
        journals = ["Nature", "Nature Energy", "Nature Communications",
                    "Advanced Materials", "Advanced Energy Materials"]
        (self.root / "references/corpus").mkdir(parents=True)
        (self.root / "README.md").write_text(
            "\n".join(f"<strong>{j}</strong><br>9 篇" for j in journals), encoding="utf-8")
        c.render(self.check([dict(self.record, journal="Nature")]), self.root)
        readme = (self.root / "README.md").read_text(encoding="utf-8")
        for journal in journals:
            count = 1 if journal == "Nature" else 0
            self.assertIn(f"<strong>{journal}</strong><br>{count} 篇", readme)


if __name__ == "__main__":
    unittest.main()
