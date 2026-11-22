"""Markdown profile generator combining structured models and the friend's clean header aesthetic."""

from urllib.parse import quote
from src.models import ProfileConfig


def generate_profile_markdown(cfg: ProfileConfig) -> str:
    """Compile ProfileConfig into a clean, concise, visually appealing GitHub profile README."""

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

    # Optional stats section
    stats_block = ""
    if cfg.show_github_stats:
        stats_block = f"""---

### GitHub Activity & Insights

<div align="center">
  <a href="https://github.com/{cfg.username}">
    <img src="https://github-readme-stats.vercel.app/api?username={cfg.username}&show_icons=true&theme={cfg.stats_theme}&hide_border=true&count_private=true" alt="GitHub Stats" />
  </a>
</div>

<p align="center">
  <a href="https://github.com/{cfg.username}">
    <img src="https://streak-stats.demolab.com?user={cfg.username}&theme={cfg.stats_theme}&hide_border=true" alt="Streak Stats" />
  </a>
</p>
"""

    banner_text_enc = quote(cfg.banner_motto)
    banner_desc_enc = quote(cfg.banner_sub)
    typing_lines_enc = ";".join(quote(line) for line in cfg.typing_lines)

    markdown = f"""<!--
  Automated profile README generated via Python.
-->

<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color={cfg.banner_color}&height=220&section=header&text={banner_text_enc}&fontSize=44&fontAlignY=38&desc={banner_desc_enc}&descFontSize=20&descAlignY=62&theme=dark" width="100%" alt="Header Banner" />

  <h1>{cfg.name}</h1>
  <p><b>{cfg.headline}</b></p>
  
  <p align="center">
    <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=18&duration=3200&pause=1000&color={cfg.typing_color}&center=true&vCenter=true&width=700&height=45&lines={typing_lines_enc}" alt="Typing SVG" />
  </p>

  <p>
    <a href="mailto:anh.nth1305@gmail.com"><img src="https://img.shields.io/badge/Email-anh.nth1305@gmail.com-black?style=flat-square&logo=gmail&logoColor=white" alt="Email" /></a>
    <img src="https://img.shields.io/badge/Focus-ASP.NET_Core_Backend-475569?style=flat-square" alt="Focus" />
    <img src="https://img.shields.io/badge/Path-Fullstack_Developer-1E293B?style=flat-square" alt="Path" />
    <img src="https://img.shields.io/badge/Open_To-Internship-475569?style=flat-square" alt="Open To" />
  </p>
  <p>
    <img src="https://img.shields.io/badge/Honors-Two--time_Honorable_Student-1E293B?style=flat-square" alt="Honors" />
    <img src="https://img.shields.io/badge/Education-FPT_University_HCMC-475569?style=flat-square" alt="Education" />
    <a href="https://linkedin.com/in/hong-anh-23a103448" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-Nguyen_Thi_Hong_Anh-0077B5?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
  </p>
</div>

---

### About Me

{chr(10).join(f"- {b}" for b in cfg.bio_bullets)}
- **Location:** {cfg.location}

---

### Tech Stack

{cfg.tech_intro}

{tech_stack_rendered}

---

### Featured Engineering Project

{projects_block}

{stats_block}---

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

<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color={cfg.banner_color}&height=120&section=footer&theme=dark" width="100%" alt="Footer Banner" />
</div>
"""
    return markdown
