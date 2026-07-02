# Job Application Tracker API

A RESTful API built with FastAPI, PostgreSQL, SQLAlchemy, Docker, and JWT Authentication for managing and tracking job applications throughout the job search process.

This project allows users to securely create, update, view, and manage job applications while demonstrating backend engineering concepts such as authentication, database design, CRUD operations, filtering, sorting, pagination, and containerized deployment.

## Live Demo

API Base URL:

https://job-application-tracker-api-rl3a.onrender.com

Swagger Documentation:

https://job-application-tracker-api-rl3a.onrender.com/docs

---

## Features

### Authentication

* User registration
* User login
* JWT-based authentication
* Protected routes
* Retrieve authenticated user information

### Job Application Management

* Create job applications
* View all job applications
* View individual applications
* Update applications
* Delete applications

### Productivity Features

* Filtering
* Sorting
* Pagination

### Security

* Password hashing
* JWT Authentication
* Protected endpoints

---

## Tech Stack

* Python
* FastAPI
* PostgreSQL
* SQLAlchemy
* JWT Authentication
* Docker
* Render

---

## API Endpoints

### Authentication

| Method | Endpoint       | Description            |
| ------ | -------------- | ---------------------- |
| POST   | /auth/register | Register user          |
| POST   | /auth/login    | Login user             |
| GET    | /auth/me       | Get authenticated user |

### Applications

| Method | Endpoint                       | Description          |
| ------ | ------------------------------ | -------------------- |
| GET    | /applications                  | Get all applications |
| POST   | /applications                  | Create application   |
| GET    | /applications/{application_id} | Get application      |
| PUT    | /applications/{application_id} | Update application   |
| DELETE | /applications/{application_id} | Delete application   |

### Root

| Method | Endpoint | Description |
| ------ | -------- | ----------- |
| GET    | /        | API status  |

---

## Project Structure

```text
app/
├── api/
├── core/
├── models/
├── schemas/
├── main.py

Dockerfile
docker-compose.yml
requirements.txt
.env
```

---

## Environment Variables

Create a `.env` file:

```env
DATABASE_URL=postgresql://postgres:password@localhost/jobtracker

SECRET_KEY=your_secret_key

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=60
```

---

## Local Installation

Clone the repository:

```bash
git clone https://github.com/rivondave/Job-Application-Tracker-API.git

cd Job-Application-Tracker-API
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
uvicorn app.main:app --reload
```

Access Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Docker Setup

Build and run containers:

```bash
docker compose up --build
```

Access API:

```text
http://localhost:8000
```

Swagger Documentation:

```text
http://localhost:8000/docs
```

---

## Example Use Cases

* Track job applications from multiple companies.
* Monitor application progress through different stages.
* Organize interview opportunities.
* Maintain a centralized job search workflow.

---

## What I Learned

* REST API Design
* JWT Authentication and Authorization
* Database Modeling with SQLAlchemy
* CRUD Operations
* Filtering, Sorting, and Pagination
* PostgreSQL Integration
* Docker Containerization
* API Deployment with Render
* Backend Project Architecture

---

## Future Improvements

* Application status analytics
* Email notifications
* Resume and cover letter uploads
* Application reminders
* Advanced search capabilities
* Automated testing with Pytest

```
```
