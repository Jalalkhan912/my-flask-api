# My Flask API — DevOps Learning Project

This repository is a **simple Flask API** built as a hands-on project to learn an industry-style backend workflow:

- Building a small API service
- Automating quality checks with **GitHub Actions (CI/CD)**
- Preparing for containerized deployment with **Docker**
- Learning cloud delivery concepts using **AWS ECR** and **EC2**
  - Separate environments for **staging** and **production**

Even though the app itself is intentionally small, the focus is on practicing real-world engineering workflows.

---

## Project Goals

This project was created to learn and practice:

1. **Clean API structure** with Flask
2. **Automated testing** with `pytest`
3. **Static checks/linting** with `flake8`
4. **CI pipeline execution** on each push/PR to `main`
5. DevOps deployment concepts around:
   - Docker image workflow
   - AWS Elastic Container Registry (ECR)
   - AWS EC2-based staging and production environments

---

## API Endpoints

### `GET /health`
Health-check endpoint used by monitoring/automation.

**Response example:**
```json
{
  "status": "ok",
  "version": "1.0.0"
}
```

### `GET /greet/<name>`
Simple greeting endpoint.

**Example:**
`/greet/Alice`

**Response example:**
```json
{
  "message": "Hello, Alice!"
}
```

---

## Local Setup

### 1) Clone repository
```bash
git clone <your-repo-url>
cd my-flask-api
```

### 2) Create virtual environment
```bash
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
# .venv\Scripts\activate    # Windows PowerShell
```

### 3) Install dependencies
```bash
pip install -r requirements.txt
```

### 4) Run application
```bash
python app.py
```

Application runs on:
- `http://localhost:5000`

---

## Run Tests & Lint Locally

```bash
pytest test_app.py -v
flake8 app.py --max-line-length=100
```

---

## CI/CD (GitHub Actions)

The workflow is defined in:
- `.github/workflows/cicd.yml`

It runs on:
- Push to `main`
- Pull requests targeting `main`

Pipeline stages:
1. Checkout code
2. Setup Python 3.13
3. Install dependencies
4. Lint with flake8
5. Run tests with pytest

---

## Tech Stack

- **Python 3.13**
- **Flask**
- **Pytest**
- **Flake8**
- **GitHub Actions**
- Learning track: **Docker + AWS ECR + AWS EC2 (staging/production)**

---

## Why this project?

This is a personal learning project to practice how modern backend services are developed and shipped using production-oriented workflows.

The API is deliberately small so the focus stays on:
- quality checks,
- automation,
- and deployment architecture thinking.

