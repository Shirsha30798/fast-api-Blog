# FastAPI Blog API

A RESTful Blog API built with FastAPI and PostgreSQL. This project was developed to learn backend development fundamentals including authentication, database design, migrations, deployment, and secure password recovery.

## Features

- User Registration
- JWT Authentication
- Password Hashing with bcrypt
- Protected Routes
- CRUD Operations for Blog Posts
- PostgreSQL Database
- SQLAlchemy ORM
- Alembic Database Migrations
- Environment Variable Configuration
- Password Reset via Email
- One-Time Password Reset Tokens
- Token Expiration Validation
- Deployed Backend

---

## Tech Stack

- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- Pydantic
- JWT Authentication
- Passlib (bcrypt)
- FastAPI-Mail
- Render (Deployment)

---

## Project Structure

```
app/
│
├── routers/
├── models.py
├── schemas.py
├── oauth2.py
├── database.py
├── config.py
├── utils.py
├── main.py
│
alembic/
│
requirements.txt
```

---

## Authentication

Authentication is implemented using JSON Web Tokens (JWT).

Workflow:

1. Register a new user
2. Login
3. Receive JWT access token
4. Include the Bearer Token in protected requests

---

## Password Reset Workflow

1. User requests password reset using their email.
2. A secure random token is generated using Python's `secrets` module.
3. The token is stored in the database with an expiration time.
4. A password reset email containing the token is sent.
5. User submits the token along with a new password.
6. Backend validates:
   - Token exists
   - Token has not expired
   - Token has not already been used

7. Password is hashed and updated.
8. Reset token is marked as used.

---

## Environment Variables

Example `.env`

```
DATABASE_HOSTNAME=
DATABASE_PORT=
DATABASE_NAME=
DATABASE_USERNAME=
DATABASE_PASSWORD=

SECRET_KEY=
ALGORITHM=
ACCESS_TOKEN_EXPIRE_MINUTES=

MAIL_USERNAME=
MAIL_PASSWORD=
MAIL_FROM=
MAIL_SERVER=
MAIL_PORT=
```

---

## Running Locally

Clone the repository

```
git clone https://github.com/<your-username>/<repo-name>.git
```

Install dependencies

```
pip install -r requirements.txt
```

Run database migrations

```
alembic upgrade head
```

Start the application

```
uvicorn app.main:app --reload
```

Swagger UI

```
http://localhost:8000/docs
```

---

## Future Improvements

- Refresh Tokens
- Role-Based Authorization
- Docker Support
- Unit & Integration Tests
- Rate Limiting
- Email Templates
- CI/CD Pipeline

---

## Learning Objectives

This project helped reinforce:

- REST API design
- Authentication & Authorization
- ORM relationships
- Database migrations
- Password hashing
- Secure token generation
- Email integration
- Environment configuration
- Backend deployment
- Secure password recovery workflow
