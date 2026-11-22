"""Data models and profile configuration."""

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
    tech_stack: List[str]
    repo_url: str
    highlights: List[str]


@dataclass
class ProfileConfig:
    name: str = "Nguyen Thi Hong Anh"
    username: str = "sweeti3-pie"
    headline: str = "Backend Software Engineer | Python, Cloud & High-Concurrency Systems"
    location: str = "Ho Chi Minh City, Vietnam"
    university: str = "FPT University Ho Chi Minh City"
    degree: str = "B.S. in Software Engineering (GPA: 3.18/4.0)"
    honors: List[str] = field(default_factory=lambda: [
        "Honorable Student Award (Semester 3, Semester 4)",
        "Top Academic Performer in Software Engineering Foundations",
    ])
    
    bio_bullets: List[str] = field(default_factory=lambda: [
        "🔭 Architecting **scalable microservices, high-throughput APIs**, and **event-driven distributed systems**.",
        "⚡ Focused on **Clean Architecture, asynchronous concurrency, atomic caching**, and **cloud-native resilience**.",
        "🎓 Foundations: **Data Structures & Algorithms (UC San Diego)**, **Software Engineering (HKUST)**, **GenAI Fundamentals (IBM)**.",
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

    skillicons: List[str] = field(default_factory=lambda: [
        "python", "fastapi", "django", "flask", "postgres", 
        "redis", "docker", "git", "githubactions", "linux", 
        "cs", "dotnet"
    ])

    tech_categories: Dict[str, List[TechItem]] = field(default_factory=lambda: {
        "Languages": [
            TechItem("Python", "3776AB", "python"),
            TechItem("C#", "239120", "c-sharp"),
            TechItem("SQL", "CC292B", "microsoft-sql-server"),
            TechItem("Bash", "4EAA25", "gnu-bash"),
        ],
        "Backend & Frameworks": [
            TechItem("FastAPI", "009688", "fastapi"),
            TechItem("Django", "092E20", "django"),
            TechItem("Flask", "000000", "flask"),
            TechItem(".NET 8", "512BD4", "dotnet"),
            TechItem("ASP.NET Core", "512BD4", "dotnet"),
            TechItem("Celery", "37814A", "celery"),
            TechItem("Pydantic", "E92063", "pydantic"),
        ],
        "Databases & Caching": [
            TechItem("PostgreSQL", "4169E1", "postgresql"),
            TechItem("Redis 7", "DC382D", "redis"),
            TechItem("SQL Server 2022", "CC292B", "microsoft-sql-server"),
            TechItem("SQLite", "003B57", "sqlite"),
        ],
        "Cloud, DevOps & Tools": [
            TechItem("Docker", "2496ED", "docker"),
            TechItem("Git", "F05032", "git"),
            TechItem("GitHub Actions", "2088FF", "github-actions"),
            TechItem("Linux", "FCC624", "linux", logo_color="black"),
            TechItem("Postman", "FF6C37", "postman"),
            TechItem("Swagger / OpenAPI", "85EA2D", "swagger", logo_color="black"),
            TechItem("Pytest", "0A9EDC", "pytest"),
        ],
    })

    featured_projects: List[ProjectItem] = field(default_factory=lambda: [
        ProjectItem(
            title="Async Distributed Task Engine",
            subtitle="High-Throughput Asynchronous Worker & Queue Pipeline",
            tech_stack=["Python", "FastAPI", "Redis", "Celery", "Docker", "Pytest"],
            repo_url="https://github.com/sweeti3-pie/async-task-engine",
            highlights=[
                "Engineered non-blocking worker pipeline handling **5,000+ jobs/min** with Redis stream brokers.",
                "Implemented exponential backoff retries, dead-letter queue (DLQ), and atomic task deduplication.",
                "Automated end-to-end integration testing and Dockerized multi-stage container deployment.",
            ],
        ),
        ProjectItem(
            title="VeggieLife – Plant-Based Nutrition Platform",
            subtitle="High-Concurrency Backend with Sub-50ms Token Revocation",
            tech_stack=["C#", ".NET 8", "EF Core", "SQL Server", "Redis 7", "SignalR", "Docker"],
            repo_url="https://github.com/fpt-semester5-organization/Backend",
            highlights=[
                "Architected 3-layer Clean Backend (39 SQL Server tables) with standardized RESTful API envelopes.",
                "Engineered sub-50ms instant token revocation via Redis Blacklist & real-time SignalR logout.",
                "Designed zero-DB guest trial pipeline with atomic Redis Lua scripts, eliminating DB write contention.",
            ],
        ),
        ProjectItem(
            title="GitHub Profile Dynamic Generator",
            subtitle="Automated CI/CD Profile Pipeline in Python",
            tech_stack=["Python 3.13", "GitHub Actions", "Pydantic", "Unit Testing"],
            repo_url="https://github.com/sweeti3-pie/sweeti3-pie",
            highlights=[
                "Self-updating profile engine maintaining live metrics, verified badges, and dynamic content.",
                "Strict test coverage validating markdown AST, link validity, and badge generation schemas.",
            ],
        ),
    ])

    quote: str = "Clean code always looks like it was written by someone who cares. — Robert C. Martin"
