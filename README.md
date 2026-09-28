# AWS Cloud DevOps Lab

AWS Cloud DevOps Lab is a portfolio project focused on designing, deploying, and operating a containerized API on Amazon Web Services using modern Cloud and DevOps practices.

The project combines application development, containerization, Infrastructure as Code, CI/CD, monitoring, and basic security into a single end-to-end deployment workflow.

## Architecture

```text
Developer
    │
    │ git push
    ▼
GitHub
    │
    ▼
GitHub Actions
    │
    ├── Automated Tests
    ├── Docker Build
    └── Security Checks
            │
            ▼
        Amazon ECR
            │
            ▼
        Amazon ECS
        AWS Fargate
            │
            ▼
Application Load Balancer
            │
            ▼
         Internet
```

Infrastructure is provisioned and managed using Terraform.

```text
Terraform
    │
    ▼
AWS Infrastructure
```

Application logs, metrics, and health information are monitored through Amazon CloudWatch.

## Tech Stack

- Python
- FastAPI
- Uvicorn
- pytest
- Docker
- Amazon Web Services
- Amazon ECR
- Amazon ECS
- AWS Fargate
- Application Load Balancer
- Amazon CloudWatch
- AWS IAM
- Amazon VPC
- Terraform
- GitHub Actions

## Local Setup

Create a virtual environment:

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

Run the API locally:

```bash
python -m uvicorn app.main:app --reload
```

Run the test suite:

```bash
python -m pytest
```

## Project Scope

The project covers:

- REST API development
- Automated testing
- Application containerization
- Container image management
- AWS cloud deployment
- Infrastructure as Code
- CI/CD automation
- Cloud networking
- Monitoring and logging
- IAM and access control
- Basic DevSecOps practices