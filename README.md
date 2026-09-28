# AWS Cloud DevOps Lab

Cloud and DevOps project focused on deploying a containerized API to AWS using Docker, Terraform and GitHub Actions.

## Architecture

```text
GitHub
  ↓
GitHub Actions
  ↓
Docker
  ↓
Amazon ECR
  ↓
Amazon ECS / Fargate
  ↓
Application Load Balancer
```

Infrastructure is managed with Terraform and monitored with Amazon CloudWatch.

## Tech Stack

- Python
- FastAPI
- pytest
- Docker
- AWS
- Terraform
- GitHub Actions

## Local Setup

Create the virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Run the API:

```bash
python -m uvicorn app.main:app --reload
```

Run tests:

```bash
python -m pytest
```

## API

Current endpoints:

```text
GET /
GET /health
```

Interactive documentation:

```text
http://127.0.0.1:8000/docs
```

## Project Scope

The project covers:

- Containerization with Docker
- AWS deployment with ECS and Fargate
- Infrastructure as Code with Terraform
- CI/CD with GitHub Actions
- Monitoring with CloudWatch
- Basic Cloud security practices