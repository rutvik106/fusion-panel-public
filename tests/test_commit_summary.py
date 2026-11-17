
"""Automated tests for GitHub commit summary."""

import csv
import importlib.util
from pathlib import Path

import pytest


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "commit_summary.py"

spec = importlib.util.spec_from_file_location("commit_summary", SCRIPT)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def write_input(path, rows):
    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["Repository", "Branch", "Commit Hash"]
        )
        writer.writeheader()
        writer.writerows(rows)


def test_summary_groups_and_sorts(tmp_path):
    source = tmp_path / "all_commits.csv"

    write_input(source, [
        {"Repository": "app", "Branch": "main", "Commit Hash": "a"},
        {"Repository": "api", "Branch": "main", "Commit Hash": "b"},
        {"Repository": "app", "Branch": "main", "Commit Hash": "c"},
        {"Repository": "app", "Branch": "dev", "Commit Hash": "d"},
    ])

    output = module.generate_commit_summary(source)

    with output.open(newline="", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))

    assert rows == [
        {"Repository": "api", "Branch": "main", "Total Commits": "1"},
        {"Repository": "app", "Branch": "dev", "Total Commits": "1"},
        {"Repository": "app", "Branch": "main", "Total Commits": "2"},
    ]


def test_empty_csv_writes_header(tmp_path):
    source = tmp_path / "all_commits.csv"

    write_input(source, [])

    output = module.generate_commit_summary(source)

    assert output.read_text(encoding="utf-8").strip() == (
        "Repository,Branch,Total Commits"
    )


def test_missing_columns_is_rejected(tmp_path):
    source = tmp_path / "bad.csv"

    source.write_text("Commit Hash\na\n", encoding="utf-8")

    with pytest.raises(ValueError, match="Repository and Branch"):
        module.generate_commit_summary(source)


def test_refuses_to_overwrite_input(tmp_path):
    source = tmp_path / "all_commits.csv"

    write_input(source, [])

    with pytest.raises(ValueError, match="different"):
        module.generate_commit_summary(source, source)
