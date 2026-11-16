# DevOps Support Service

Small Flask service developed for the DevOps and System Administration team project.

## Team
- Ahmad Marzuq Alharbi
- Anas Marshud Alsuhaymi
- Amjad Yasser Bahakeem

## Technologies
- Ubuntu Linux
- Python Flask
- Docker
- Git and GitHub
- GitHub Actions
- Python unittest
- Ruff

## Prerequisites
- Python 3
- Docker
- Git
- curl

## Project Structure
- app/ : Flask application and Dockerfile
- tests/ : automated tests
- docs/ : operational documentation
- records/ : project and change records
- .github/workflows/ : CI workflow

## Run Tests

```bash
source app/.venv/bin/activate
python -m unittest discover -s tests -v
ruff check app/app.py tests/
