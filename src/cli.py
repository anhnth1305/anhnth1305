"""Command-line interface for generating the GitHub profile README."""

import argparse
from pathlib import Path
from src.models import ProfileConfig
from src.generator import generate_profile_markdown


def main():
    parser = argparse.ArgumentParser(
        description="Generate a modern, concise, icon-rich GitHub profile README."
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        default="README.md",
        help="Target output file path (default: README.md)",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Check if current output matches generated markdown without modifying",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print generated markdown to stdout without writing to disk",
    )

    args = parser.parse_args()
    config = ProfileConfig()
    rendered_md = generate_profile_markdown(config)

    if args.dry_run:
        print(rendered_md)
        return 0

    target_path = Path(args.output)

    if args.check:
        if not target_path.exists():
            print(f"Error: {target_path} does not exist.")
            return 1
        current_content = target_path.read_text(encoding="utf-8")
        if current_content != rendered_md:
            print(f"Drift detected in {target_path}. Run without --check to synchronize.")
            return 1
        print(f"Verification passed: {target_path} is up to date.")
        return 0

    target_path.write_text(rendered_md, encoding="utf-8")
    print(f" Successfully generated GitHub profile README at: {target_path.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
