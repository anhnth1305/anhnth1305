"""Data models and profile configuration based strictly on actual achievements."""

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
    headline: str = "Third-Year Software Engineering Student at FPTU HCM | Backend Engineer"
    location: str = "Ho Chi Minh City, Vietnam"
    university: str = "FPT University Ho Chi Minh City (FPTU HCM)"
    degree: str = "Third-year Software Engineering Student (GPA: 3.18/4.0)"
    honors: List[str] = field(default_factory=lambda: [
        "Honorable Student Award (Semester 3, Semester 4) – FPT University",
        "Coursera Specialization: Data Structures & Algorithms (UC San Diego)",
        "Coursera Specialization: Software Engineering (HKUST)",
        "Coursera Specialization: Object-Oriented Programming in Java (Duke University)",
        "IBM & Anthropic: Generative AI Fundamentals & Claude 101",
    ])

    bio_bullets: List[str] = field(default_factory=lambda: [
        "🎓 **Status:** Third-year Software Engineering student at **FPT University Ho Chi Minh City (FPTU HCM)** *(GPA: 3.18/4.0)*.",
        "🔭 **Core Focus:** Backend Engineering, Clean Architecture, high-concurrency systems, and resilient API design.",
        "⚡ **Key Strengths:** Sub-50ms security pipelines, atomic Redis caching (Lua scripts), and background worker orchestration.",
        "🌐 **Languages:** Vietnamese (Native) • English (Professional Working Proficiency) • Japanese (Elementary) • French (Basic).",
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

    # No duplicated mega-banner; icons are placed directly per title
    tech_categories: Dict[str, List[TechItem]] = field(default_factory=lambda: {
        "💻 Languages": [
            TechItem("C#", "239120", "c-sharp"),
            TechItem(".NET 8", "512BD4", "dotnet"),
            TechItem("Python", "3776AB", "python"),
            TechItem("SQL (T-SQL)", "CC292B", "microsoft-sql-server"),
        ],
        "⚙️ Frameworks & Libraries": [
            TechItem("ASP.NET Core Web API", "512BD4", "dotnet"),
            TechItem("Entity Framework Core 8", "512BD4", "dotnet"),
            TechItem("SignalR", "512BD4", "dotnet"),
            TechItem("Polly", "512BD4", "dotnet"),
            TechItem("Serilog", "007ACC", "windows-terminal"),
            TechItem("FluentValidation", "512BD4", "dotnet"),
        ],
        "🗄️ Databases & Caching": [
            TechItem("SQL Server 2022", "CC292B", "microsoft-sql-server"),
            TechItem("Redis 7 (Lua)", "DC382D", "redis"),
        ],
        "🚀 DevOps, Testing & Tooling": [
            TechItem("Docker", "2496ED", "docker"),
            TechItem("Git", "F05032", "git"),
            TechItem("GitHub Actions", "2088FF", "github-actions"),
            TechItem("Postman", "FF6C37", "postman"),
            TechItem("Swagger / OpenAPI", "85EA2D", "swagger", logo_color="black"),
            TechItem("xUnit", "512BD4", "dotnet"),
        ],
    })

    architecture_skills: List[str] = field(default_factory=lambda: [
        "Clean Architecture (3-Layer / N-Tier)",
        "RESTful API Design & Error Handling Envelopes",
        "Sub-50ms Instant Token Revocation (Redis Blacklist)",
        "JWT & Refresh Token Rotation",
        "Atomic Quotas with Redis Lua Scripting",
        "HMAC SHA-256 Webhook Verification & PayOS Integration",
        "IDOR Prevention & RBAC",
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
                "**Resilient Background Workers & Testing:** Authored async worker jobs with exponential backoff retries and maintained a repository suite of **1,200+ automated tests**.",
            ],
        ),
    ])

    quote: str = "Clean code always looks like it was written by someone who cares. — Robert C. Martin"
