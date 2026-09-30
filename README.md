# PocketSmart AI

PocketSmart AI is an AI-powered personal finance assistant built with FastAPI.

## Features

- User registration
- User login
- Secure password hashing
- JWT authentication
- Expense tracking
- Expense categories
- Expense deletion
- Total spending calculation
- AI finance assistant
- SQLite database
- Responsive web interface

## Project Structure

```text
pocketSmart AI/
│
├── app/
│   ├── services/
│   │   ├── ai_service.py
│   │   ├── auth_service.py
│   │   └── expense_service.py
│   │
│   ├── static/
│   │   ├── script.js
│   │   └── style.css
│   │
│   ├── templates/
│   │   ├── dashboard.html
│   │   ├── index.html
│   │   └── login.html
│   │
│   ├── __init__.py
│   ├── auth.py
│   ├── config.py
│   ├── database.py
│   ├── main.py
│   └── schemas.py
│
├── .env
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt