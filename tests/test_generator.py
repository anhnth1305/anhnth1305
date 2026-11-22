"""Unit tests for the profile generator package."""

import unittest
from pathlib import Path
import tempfile

from src.models import ProfileConfig, SocialLink, TechCategory
from src.badges import social_badge
from src.generator import generate_profile_markdown


class TestProfileGenerator(unittest.TestCase):
    def setUp(self):
        self.config = ProfileConfig()

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
        self.assertIn("Third-Year", md)
        self.assertIn("Tech Stack", md)
        self.assertIn("Languages", md)
        self.assertIn("Frontend", md)
        self.assertIn("Backend & Frameworks", md)
        self.assertIn("Database - Vector Database", md)
        self.assertIn("DevOps & Tools", md)
        self.assertIn("skillicons.dev/icons?i=js,ts,java,py,cs,c", md)
        self.assertIn("VeggieLife", md)
        self.assertNotIn("Async Distributed Task Engine", md)

    def test_file_output(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            out_file = Path(tmpdir) / "TEST_README.md"
            md = generate_profile_markdown(self.config)
            out_file.write_text(md, encoding="utf-8")
            self.assertTrue(out_file.exists())
            self.assertEqual(out_file.read_text(encoding="utf-8"), md)


if __name__ == "__main__":
    unittest.main()
