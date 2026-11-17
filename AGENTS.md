# Fusion Panel — AI Agent Instructions

## Project Overview
Fusion Panel is a Python application that tracks GitHub repository activity, generates reports, and supports AI-assisted analysis.

## Technology Stack
- Python
- Flask web framework
- SQLite database
- GitHub API
- CSV reporting
- Pytest for automated testing

## Project Structure
- gui/ — Flask application and web interface
- src/ — Core application functionality
- scripts/ — Utility scripts
- tests/ — Automated tests
- docs/ — Project documentation
- data/ — Local application data

## Development Guidelines
1. Understand existing code before making modifications.
2. Preserve existing application functionality.
3. Make small, focused changes.
4. Never expose API keys or credentials.
5. Do not commit local database files or secrets.
6. Add automated tests for new features.
7. Follow existing Python coding conventions.
8. Work on a separate Git branch.
9. Do not deploy to production or merge assessment PRs.

## Local Setup
1. Create a virtual environment:
   python -m venv .venv

2. Activate it on Windows:
   .venv\Scripts\Activate.ps1

3. Install dependencies:
   python -m pip install -r requirements.txt

4. Run the Flask application:
   python gui/app.py

## Testing
Run feature tests:
python -m pytest tests/test_commit_summary.py -v

Run all tests:
python -m pytest -v

## Added Feature
Commit Summary Report

File: scripts/commit_summary.py

Purpose:
Generate CSV summaries containing total commit counts
grouped by GitHub repository and branch.

Example:
python scripts/commit_summary.py path/to/all_commits.csv

## Assessment Rules
All code changes must be AI-generated.
Review AI-generated code before accepting changes.
Use terminal commands for execution, testing and Git.
Do not merge the Pull Request.
