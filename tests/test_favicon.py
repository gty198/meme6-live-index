from pathlib import Path
import unittest


ROOT = Path(__file__).parents[1]
HTML = (ROOT / "index.html").read_text(encoding="utf-8")


class FaviconContractTests(unittest.TestCase):
    def test_page_declares_a_local_svg_favicon(self):
        self.assertIn('<link rel="icon" type="image/svg+xml" href="assets/favicon.svg"', HTML)

    def test_favicon_is_a_valid_meme6_svg_asset(self):
        icon = ROOT / "assets" / "favicon.svg"
        self.assertTrue(icon.is_file())
        source = icon.read_text(encoding="utf-8")
        self.assertIn('<svg', source)
        self.assertIn('aria-label="MEME6 Index"', source)
        self.assertIn('>M6</text>', source)
        self.assertNotIn('<path', source)
        self.assertIn('viewBox="0 0 64 64"', source)


if __name__ == "__main__":
    unittest.main()
