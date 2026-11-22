"""Data models and profile configuration matching the friend's modern blue aesthetic."""

from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class SocialLink:
    name: str
    url: str
    badge_label: str
    color: str
    logo: str


@dataclass
class TechItem:
    name: str
    color: str
    logo: str
    logo_color: str = "white"


@dataclass
class TechCategory:
    title: str
    icons: List[str]  # skillicons IDs, e.g. ["cs", "dotnet", "java", "c", "js", "html", "css"]


@dataclass
class ProjectItem:
    title: str
    subtitle: str
    role: str
    tech_stack: List[str]
    repo_url: str
    highlights: List[str]


@dataclass
class ProfileConfig:
    name: str = "Nguyen Thi Hong Anh"
    username: str = "sweeti3-pie"
    headline: str = "Backend Software Engineer | Distributed Systems"
    location: str = "Ho Chi Minh City, Vietnam"
    university: str = "FPT University Ho Chi Minh City (FPTU HCM)"
    degree: str = "Third-year Software Engineering Student (GPA: 3.18/4.0)"
    
    # Friend-inspired header branding
    banner_motto: str = "Architect. Optimize. Scale."
    banner_sub: str = "ASP.NET Core | Clean Architecture | Distributed Systems"
    tagline: str = "Focused on architecting resilient, high-throughput systems."
    banner_color: str = "0:0b1d3a,100:1e40af"  # Deep navy to royal blue gradient

    bio_bullets: List[str] = field(default_factory=lambda: [
        "**Education:** Third-year Software Engineering student at **FPT University Ho Chi Minh City (FPTU HCM)** *(GPA: 3.18/4.0 • Two-time Honorable Student Award recipient)*.",
        "**Focus:** Backend Engineering, Clean Architecture, distributed caching, and resilient API design.",
        "**Core Expertise:** Sub-50ms instant security revocation (Redis Blacklist), atomic Redis Lua scripting, and background workers.",
        "**Languages:** Vietnamese (Native) • English (Professional Working Proficiency) • Japanese (Elementary) • French (Basic).",
    ])

    socials: List[SocialLink] = field(default_factory=lambda: [
        SocialLink(
            name="LinkedIn",
            url="https://linkedin.com/in/hong-anh-23a103448",
            badge_label="LinkedIn",
            color="0077B5",
            logo="linkedin",
        ),
        SocialLink(
            name="Gmail",
            url="mailto:anh.nth1305@gmail.com",
            badge_label="Gmail",
            color="D14836",
            logo="gmail",
        ),
        SocialLink(
            name="GitHub",
            url="https://github.com/sweeti3-pie",
            badge_label="GitHub",
            color="181717",
            logo="github",
        ),
    ])

    # Verified actual skills from CV & FPTU coursework
    tech_intro: str = "The tools I use most while building toward stronger backend depth, resilient architectures, and safer delivery."
    tech_categories: List[TechCategory] = field(default_factory=lambda: [
        TechCategory(
            title="Languages",
            icons=["cs", "dotnet", "java", "c", "js", "html", "css"],
        ),
        TechCategory(
            title="Backend & Frameworks",
            icons=["dotnet"],
        ),
        TechCategory(
            title="Databases & Caching",
            icons=["redis", "postgres", "mysql"],
        ),
        TechCategory(
            title="DevOps & Tools",
            icons=["docker", "git", "github", "githubactions", "postman", "vscode", "figma"],
        ),
    ])

    featured_projects: List[ProjectItem] = field(default_factory=lambda: [
        ProjectItem(
            title="VeggieLife – Plant-Based Nutrition & Community Platform",
            subtitle="AI-Powered High-Concurrency Backend Architecture",
            role="Backend Architect & Core Engineer",
            tech_stack=[
                "C#", ".NET 8", "EF Core 8", "SQL Server 2022", 
                "Redis 7", "SignalR", "PayOS", "Docker", "xUnit"
            ],
            repo_url="https://github.com/fpt-semester5-organization/Backend",
            highlights=[
                "**Modular 3-Layer Architecture:** Engineered scalable backend on ASP.NET Core 8 with 39 SQL Server tables, standardized error envelopes, and pagination.",
                "**Real-Time Security & Instant Revocation:** Built JWT/Refresh token rotation with sub-50ms revocation via Redis Blacklist and SignalR real-time logout.",
                "**Zero-DB Guest Pipeline:** Formulated atomic quota tracking using Redis Lua scripts, eliminating cold database write load for AI trial queries.",
                "**Fintech Payment Gateway:** Integrated PayOS (VietQR) with HMAC SHA-256 webhook reconciliation, dynamic client-origin routing, and IDOR protection.",
                "**Resilient Background Workers & Testing:** Authored async worker jobs with exponential backoff retries and maintained an enterprise suite of **1,200+ automated tests**.",
            ],
        ),
    ])

    # Toggle optional visual widgets
    show_github_stats: bool = False
    stats_theme: str = "tokyonight"

    quote: str = "Clean code always looks like it was written by someone who cares. — Robert C. Martin"
