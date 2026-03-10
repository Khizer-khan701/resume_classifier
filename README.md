---
title: Resume Classifier
emoji: 🏎️
colorFrom: indigo
colorTo: purple
sdk: docker
pinned: false
---

# Resume Classifier SaaS

A production-ready, AI-powered resume analysis SaaS built with Django, Firestore, Celery, Redis, and LangChain.

## Features
- **Firebase Authentication:** Secure user signup, login, and profile management stored in Firestore.
- **Resume Parsing & AI Analysis:** Upload PDF/DOCX resumes. Celery workers extract text and use LangChain + OpenAI to generate ATS scores, skill extraction, role matching, and actionable feedback.
- **Job Tailored Tools:** Generate custom Cover Letters and Mock Interview Questions based on target job descriptions and analyzed resumes.
- **Reporting:** Export detailed Resume Analysis results as clean, print-ready PDF-style reports.
- **Scalable Architecture:** Firestore for NoSQL document storage, Celery + Redis for asynchronous background task processing of heavy LLM pipelines.

## Tech Stack
- Django 5.0+
- Firebase Admin SDK (Firestore Database)
- Docker & docker-compose
- Celery & Redis
- LangChain, OpenAI (gpt-4o-mini)
- Tailwind CSS

## Getting Started

### 1. Prerequisites
- Docker and docker-compose installed.
- A Firebase project with Firestore and Authentication explicitly enabled.
- An OpenAI API Key.

### 2. Environment Setup
1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd resume_classifier
   ```
2. Copy the template `.env` and fill it out:
   ```bash
   cp .env.example .env
   ```
3. Add your `firebase-key.json` (Service Account JSON from Firebase Console) into the root project directory so that the path in `.env` resolves correctly.

### 3. Running with Docker Compose
The easiest way to stand up the entire stack locally (Django App, Redis, Celery Worker) is using Docker Compose.

```bash
docker-compose up --build
```
The application will be available at `http://localhost:8000`.

### 4. Running Manually (Development)
If you prefer running without docker-compose:

1. Setup virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: .\env\Scripts\activate
   pip install -r requirements.txt
   ```
2. Run Redis locally (or point `REDIS_URL` in `.env` to a remote instance).
3. Start the Celery worker in one terminal:
   ```bash
   celery -A resume_classifier_project worker -l INFO --pool=solo
   ```
4. Start the Django server in another terminal:
   ```bash
   python manage.py runserver
   ```

## Architecture Details
This project deliberately bypasses heavily reliant Django relational ORM models for standard app data. Instead, it uses the **Repository Pattern** located in `common/repositories.py` to interface exclusively with Google Cloud Firestore via the Firebase Admin SDK. All components are decoupled into standard service layers mapping perfectly to a scalable NoSQL backend.
