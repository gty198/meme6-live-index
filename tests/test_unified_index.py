from pathlib import Path
import re
import unittest


HTML = Path(__file__).parents[1] / "index.html"


class UnifiedUtcIndexContractTests(unittest.TestCase):
    def setUp(self):
        self.source = HTML.read_text(encoding="utf-8")

    def test_uses_one_immutable_utc_base_for_every_interval(self):
        """Period selection must not set component bases from its first candle."""
        self.assertRegex(
            self.source,
            r"const INDEX_BASE_UTC\s*=\s*'\d{4}-\d{2}-\d{2}T00:00:00Z'",
        )
        self.assertIn("const INDEX_BASE_MS = Date.parse(INDEX_BASE_UTC)", self.source)
        self.assertIn("const INDEX_BASES = new Map(", self.source)
        self.assertNotIn("maps[i].get(common[0]).c", self.source)

    def test_headline_uses_live_prices_against_the_utc_base(self):
        """The displayed current index must not come from the selected K-line interval."""
        self.assertIn("livePrices:new Map()", self.source)
        self.assertRegex(
            self.source,
            r"const prices=ASSETS\.map\(a=>state\.livePrices\.get\(a\.pair\)\)",
        )
        self.assertIn("connectLivePrices();", self.source)


if __name__ == "__main__":
    unittest.main()
