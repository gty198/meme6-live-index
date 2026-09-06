from pathlib import Path
import unittest


ROOT = Path(__file__).parents[1]
HTML = (ROOT / "index.html").read_text(encoding="utf-8")
LOGOS = ("doge", "shib", "pepe", "bonk", "floki", "wif")


class ComponentLogoContractTests(unittest.TestCase):
    def test_each_index_component_declares_a_local_logo_asset(self):
        for symbol in ("DOGE", "SHIB", "PEPE", "BONK", "FLOKI", "WIF"):
            self.assertIn(f"symbol:'{symbol}',", HTML)
            self.assertRegex(HTML, rf"symbol:'{symbol}', pair:'{symbol}USDT', logo:'assets/logos/{symbol.lower()}.png'")

    def test_component_rows_render_images_not_letter_badges(self):
        self.assertIn('class="coin-logo"', HTML)
        self.assertIn('src="${a.logo}"', HTML)
        self.assertNotIn('coin-badge">${a.symbol.slice(0,2)}', HTML)

    def test_all_declared_logo_files_exist(self):
        for logo in LOGOS:
            path = ROOT / "assets" / "logos" / f"{logo}.png"
            self.assertTrue(path.is_file(), path)
            self.assertGreater(path.stat().st_size, 500, path)


if __name__ == "__main__":
    unittest.main()
