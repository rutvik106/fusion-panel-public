
"""Generate a GitHub commit summary CSV."""

import argparse
import csv
from collections import Counter
from pathlib import Path


def generate_commit_summary(source_csv, destination_csv=None):
    """Count commits grouped by repository and branch."""

    source = Path(source_csv)

    destination = (
        Path(destination_csv)
        if destination_csv
        else source.with_name("commit_summary.csv")
    )

    if source.resolve() == destination.resolve():
        raise ValueError("Output file must be different from input file")

    counts = Counter()

    with source.open("r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)

        required = {"Repository", "Branch"}

        if not required.issubset(reader.fieldnames or []):
            raise ValueError(
                "CSV must have Repository and Branch columns"
            )

        for row in reader:
            repo = (row["Repository"] or "").strip()
            branch = (row["Branch"] or "default").strip() or "default"

            if not repo:
                raise ValueError("Each commit must contain a repository name")

            counts[(repo, branch)] += 1

    destination.parent.mkdir(parents=True, exist_ok=True)

    with destination.open("w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["Repository", "Branch", "Total Commits"])

        for (repo, branch), count in sorted(counts.items()):
            writer.writerow([repo, branch, count])

    return destination


def main():
    parser = argparse.ArgumentParser(
        description="Generate GitHub commit summary report"
    )

    parser.add_argument("source", help="Input commits CSV")
    parser.add_argument("--output", help="Output summary CSV")

    args = parser.parse_args()

    result = generate_commit_summary(args.source, args.output)

    print(f"Summary created: {result}")


if __name__ == "__main__":
    main()
