from pathlib import Path
import unittest


ROOT = Path(__file__).parents[1]
HTML = (ROOT / "index.html").read_text(encoding="utf-8")


class FaviconContractTests(unittest.TestCase):
    def test_page_declares_the_user_supplied_png_favicon(self):
        self.assertIn('<link rel="icon" type="image/png" href="assets/favicon.png"', HTML)
        self.assertNotIn('assets/favicon.svg', HTML)

    def test_png_favicon_is_a_square_brand_image(self):
        icon = ROOT / "assets" / "favicon.png"
        self.assertTrue(icon.is_file())
        self.assertGreater(icon.stat().st_size, 10_000)
        header = icon.read_bytes()[:24]
        self.assertEqual(header[:8], b"\x89PNG\r\n\x1a\n")
        self.assertEqual(int.from_bytes(header[16:20], "big"), 512)
        self.assertEqual(int.from_bytes(header[20:24], "big"), 512)


if __name__ == "__main__":
    unittest.main()
