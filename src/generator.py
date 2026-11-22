"""Markdown profile generator combining structured models and clean typography without icon clutter."""

from src.models import ProfileConfig
from src.badges import social_badge


def generate_profile_markdown(cfg: ProfileConfig) -> str:
    """Compile ProfileConfig into a clean, concise, visually appealing GitHub profile README."""
    social_badges_html = " ".join(social_badge(s) for s in cfg.socials)

    # Tech Stack: clean category titles with centered Skillicons row below
    tech_stack_sections = []
    for cat in cfg.tech_categories:
        icons_str = ",".join(cat.icons)
        tech_stack_sections.append(
            f"#### {cat.title}\n\n"
            f'<p align="center">\n'
            f'  <img src="https://skillicons.dev/icons?i={icons_str}" alt="{cat.title}" />\n'
            f"</p>"
        )
    tech_stack_rendered = "\n\n".join(tech_stack_sections)

    # Featured project (clean title, no emoji)
    projects_rendered = []
    for p in cfg.featured_projects:
        tech_pills = " ".join(f"`{t}`" for t in p.tech_stack)
        bullets = "\n".join(f"- {h}" for h in p.highlights)
        projects_rendered.append(
            f"### [{p.title}]({p.repo_url})\n"
            f"> **Role:** {p.role}  \n"
            f"> **Tech Stack:** {tech_pills}\n\n"
            f"{bullets}"
        )
    projects_block = "\n\n".join(projects_rendered)

    # Honors & awards (clean bullets, no emoji)
    honors_rendered = "\n".join(f"- **{h}**" for h in cfg.honors)

    markdown = f"""<!--
  Automated profile README generated via Python.
-->

<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=1,12,24,30&height=180&section=header&text={cfg.name.replace(' ', '%20')}&fontSize=42&fontAlignY=38&desc=Third-Year%20Software%20Engineering%20Student%20@%20FPTU%20HCM&descFontSize=18&descAlignY=62&theme=dark" width="100%" alt="Header Banner" />

  <h1>Hi there, I'm {cfg.name}</h1>
  <p><b>{cfg.headline}</b></p>
</div>

<p align="center">
  {social_badges_html}
</p>

---

### About Me

{chr(10).join(f"- {b}" for b in cfg.bio_bullets)}
- **Location:** {cfg.location}

<details>
<summary><b>Honors & Professional Certifications</b></summary>

{honors_rendered}

</details>

---

### Tech Stack

{cfg.tech_intro}

{tech_stack_rendered}

---

### Featured Engineering Project

{projects_block}

---

### GitHub Activity & Insights

<div align="center">
  <a href="https://github.com/{cfg.username}">
    <img src="https://github-readme-stats.vercel.app/api?username={cfg.username}&show_icons=true&theme={cfg.stats_theme}&hide_border=true&count_private=true" alt="GitHub Stats" height="165" />
  </a>
  <a href="https://github.com/{cfg.username}">
    <img src="https://github-readme-stats.vercel.app/api/top-langs/?username={cfg.username}&layout=compact&theme={cfg.stats_theme}&hide_border=true&langs_count=6" alt="Top Languages" height="165" />
  </a>
</div>

<p align="center">
  <a href="https://github.com/{cfg.username}">
    <img src="https://streak-stats.demolab.com?user={cfg.username}&theme={cfg.stats_theme}&hide_border=true" alt="Streak Stats" />
  </a>
</p>

---

### Get In Touch

<p align="left">
  <a href="mailto:anh.nth1305@gmail.com">
    <img src="https://img.shields.io/badge/Email-anh.nth1305@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" />
  </a>
  <a href="https://linkedin.com/in/hong-anh-23a103448">
    <img src="https://img.shields.io/badge/LinkedIn-Nguyen_Thi_Hong_Anh-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" />
  </a>
  <a href="https://github.com/{cfg.username}">
    <img src="https://img.shields.io/badge/GitHub-@sweeti3--pie-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" />
  </a>
</p>

---

<p align="center">
  <i>"{cfg.quote}"</i>
</p>
"""
    return markdown
