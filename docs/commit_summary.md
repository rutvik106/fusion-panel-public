# Commit Summary Report

## Overview
This feature generates a CSV summary of GitHub commits grouped by repository and branch.

## New Files
- scripts/commit_summary.py — Generates the summary.
- tests/test_commit_summary.py — Contains four automated tests.

## How to Use

Run the following command from the project root:

python scripts/commit_summary.py path/to/all_commits.csv

The script creates commit_summary.csv in the same directory as the input file.

## Output Format
Repository,Branch,Total Commits

## Automated Testing

Run:

python -m pytest tests/test_commit_summary.py -v

## Test Results
Four automated tests passed during local development.

## Safety
- Does not modify the original commit CSV.
- Does not require GitHub API credentials.
- Does not change existing Flask functionality.
