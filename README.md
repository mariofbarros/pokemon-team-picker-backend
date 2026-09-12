[![Status: Personal Project](https://img.shields.io/badge/Status-Personal_Project-orange)]()
[![Warning: Not for Production](https://img.shields.io/badge/Warning-Not_for_Production-red)]()

# Pokemon Team Picker API

A RESTful API built with **FastAPI** and **SQLAlchemy** to manage Pokémon teams. It supports CRUD operations for teams of exactly six Pokémon, validates payloads with Pydantic, and provides interactive API documentation via **Swagger/OpenAPI**. This backend connects directly to the [Pokemon Team Picker Frontend](https://github.com/mariofbarros/pokemon-team-picker-frontend).

## Features

- **CRUD Operations**: Create, Read, Update, and Delete Pokémon teams.
- **Validation**: Enforces exactly 6 Pokémon per team via Pydantic schemas.
- **Database**: Uses SQLite for lightweight, zero-configuration persistence.
- **Documentation**: Auto-generated Swagger UI via FastAPI's built-in OpenAPI support.
- **CORS enabled**: Ready to be consumed by the frontend during local development.
- **Containerized**: Dockerfile included for easy containerized deployment.

## Tech Stack

- **Language**: Python 3.x
- **Framework**: FastAPI 0.115
- **ORM**: SQLAlchemy 2.0
- **Server**: Uvicorn
- **Database**: SQLite

## Prerequisites

- **Python** (Version 3.8 or higher recommended)
- **Git**
- **Docker** (optional, for containerized runs)
- A code editor (e.g., VS Code)

## Setup Guide

1. Open your terminal and navigate to your desired directory:

```
# Create a project folder
mkdir Pokemon-Team-Picker
cd Pokemon-Team-Picker

# Clone the Backend
git clone https://github.com/mariofbarros/pokemon-team-picker-backend.git

# Clone the Frontend
git clone https://github.com/mariofbarros/pokemon-team-picker-frontend.git
```

Your directory structure should look like this:

```
Pokemon-Team-Picker/
├── pokemon-team-picker-backend/
│   ├── app/
│   ├── requirements.txt
│   └── ...
└── pokemon-team-picker-frontend/
    ├── src/
    ├── package.json
    └── ...
```

2. Navigate to the backend folder:

```
cd pokemon-team-picker-backend
```

3. Create a virtual environment:

```
python3 -m venv .venv
```

4. Activate the virtual environment:

- If you are on a Windows machine use the following command
```
.venv\Scripts\activate
```
- If you are on a Linux machine use the following command
```
source .venv/bin/activate
```

(You should see `(.venv)` appear at the start of your command prompt)

5. Install dependencies:

```
pip install -r requirements.txt
```

6. Start the server:

```
uvicorn app.main:app --reload
```

You should see output indicating the server is running on http://localhost:8000. Keep this terminal open. You can also go to http://localhost:8000/docs to open the Swagger UI and test all routes available.

Finally, follow the setup instructions in the [Pokemon Team Picker Frontend](https://github.com/mariofbarros/pokemon-team-picker-frontend) to run the client and start building teams.

### Run with Docker

Alternatively, skip the virtual environment and run the API in a container:

```
docker build -t pokemon-team-picker-backend .
docker run -p 8000:8000 pokemon-team-picker-backend
```

## ⚠️ Disclaimer

> **Personal Project Notice**
>
> This repository contains a **personal project** developed for portfolio and learning purposes, and as a **Proof of Concept (PoC)**. It is **not** intended for production use, commercial deployment, or handling sensitive data.
>
> **Key Limitations:**
> - **Security:** The application lacks robust security measures (e.g., authentication, authorization, input sanitization beyond basics, and secure data encryption) required for real-world environments.
> - **Scalability:** The architecture is designed for a single-user/local environment and does not support high traffic, concurrent users, or distributed systems.
> - **Features:** Several features are incomplete or simplified to focus on core learning objectives.
>
> **Future Roadmap:**
> This project is a work in progress. I intend to continue developing it to address these limitations, implement security best practices, and explore scalability solutions as part of my ongoing learning journey.
>
> **Usage:**
> Feel free to review the code for educational insights, but please do not deploy this in a live environment without significant refactoring and security auditing.
