"""Unit tests for the profile generator package."""

import unittest
from pathlib import Path
import tempfile

from src.models import ProfileConfig, TechItem, SocialLink
from src.badges import shield_badge, social_badge
from src.generator import generate_profile_markdown


class TestProfileGenerator(unittest.TestCase):
    def setUp(self):
        self.config = ProfileConfig()

    def test_shield_badge_format(self):
        item = TechItem(name="Python", color="3776AB", logo="python")
        badge = shield_badge(item)
        self.assertIn("img.shields.io/badge/Python-3776AB", badge)
        self.assertIn('logo=python', badge)
        self.assertIn('alt="Python"', badge)

    def test_social_badge_format(self):
        link = SocialLink(
            name="LinkedIn",
            url="https://linkedin.com/in/test",
            badge_label="LinkedIn",
            color="0077B5",
            logo="linkedin",
        )
        badge = social_badge(link)
        self.assertIn('href="https://linkedin.com/in/test"', badge)
        self.assertIn('img.shields.io/badge/LinkedIn-0077B5', badge)

    def test_markdown_generation_sections(self):
        md = generate_profile_markdown(self.config)
        self.assertIn("Nguyen Thi Hong Anh", md)
        self.assertIn("FPT University Ho Chi Minh City (FPTU HCM)", md)
        self.assertIn("Third-year", md)
        self.assertIn("About Me", md)
        self.assertIn("Technical Stack", md)
        self.assertIn("VeggieLife", md)
        self.assertNotIn("Async Distributed Task Engine", md)
        self.assertNotIn("GitHub Profile Dynamic Generator", md)
        self.assertIn("GitHub Activity & Insights", md)
        self.assertIn("Get In Touch", md)

    def test_file_output(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            out_file = Path(tmpdir) / "TEST_README.md"
            md = generate_profile_markdown(self.config)
            out_file.write_text(md, encoding="utf-8")
            self.assertTrue(out_file.exists())
            self.assertEqual(out_file.read_text(encoding="utf-8"), md)


if __name__ == "__main__":
    unittest.main()
