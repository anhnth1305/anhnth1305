"""Tests for badge rendering and markdown generator."""

import unittest
from pathlib import Path
import tempfile

from src.models import ProfileConfig, TechItem, SocialLink
from src.badges import shield_badge, social_badge, skillicons_url
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

    def test_skillicons_url(self):
        url = skillicons_url(["python", "docker"], per_line=10)
        self.assertEqual(url, "https://skillicons.dev/icons?i=python,docker&perline=10&theme=dark")

    def test_markdown_generation_sections(self):
        md = generate_profile_markdown(self.config)
        self.assertIn("Nguyen Thi Hong Anh", md)
        self.assertIn("Quick Overview", md)
        self.assertIn("Tech Stack & Tooling", md)
        self.assertIn("Featured Engineering Projects", md)
        self.assertIn("GitHub Activity & Insights", md)
        self.assertIn("Connect With Me", md)
        self.assertIn("skillicons.dev/icons", md)
        self.assertIn("Python", md)
        self.assertIn("FastAPI", md)
        self.assertIn("sweeti3-pie", md)

    def test_file_output(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            out_file = Path(tmpdir) / "TEST_README.md"
            md = generate_profile_markdown(self.config)
            out_file.write_text(md, encoding="utf-8")
            self.assertTrue(out_file.exists())
            self.assertEqual(out_file.read_text(encoding="utf-8"), md)


if __name__ == "__main__":
    unittest.main()
