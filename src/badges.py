"""Badge and icon rendering utilities."""

from urllib.parse import quote
from src.models import TechItem, SocialLink


def shield_badge(item: TechItem) -> str:
    """Generate a Shields.io badge URL for a tech item."""
    encoded_name = quote(item.name.replace("-", "--"))
    return (
        f'<img src="https://img.shields.io/badge/{encoded_name}-{item.color}'
        f'?style=for-the-badge&logo={item.logo}&logoColor={item.logo_color}" '
        f'alt="{item.name}" />'
    )


def social_badge(link: SocialLink) -> str:
    """Generate a clickable social badge."""
    encoded_label = quote(link.badge_label.replace("-", "--"))
    return (
        f'<a href="{link.url}" target="_blank">\n'
        f'  <img src="https://img.shields.io/badge/{encoded_label}-{link.color}'
        f'?style=for-the-badge&logo={link.logo}&logoColor=white" alt="{link.name}" />\n'
        f'</a>'
    )


def skillicons_url(icons: list[str], per_line: int = 15, theme: str = "dark") -> str:
    """Generate a unified Skillicons banner URL."""
    icons_str = ",".join(icons)
    return f"https://skillicons.dev/icons?i={icons_str}&perline={per_line}&theme={theme}"
