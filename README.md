# Messaging System

A simple full-stack application to manage and track Email, SMS, and WhatsApp messages.

## Features

- Send and view email logs
- Send and view SMS logs
- Send and view WhatsApp message logs
- Input validation for all forms

## Tech Stack

**Frontend:** React, Tailwind CSS  
**Backend:** Django, Django REST Framework  
**Database:** SQLite

## Installation

### Backend Setup

```bash
cd backend
pip install django djangorestframework django-cors-headers
python manage.py migrate
python manage.py runserver
```

Backend runs at: `http://127.0.0.1:8000`

### Frontend Setup

```bash
cd frontend
npm install
npm start
```

Frontend runs at: `http://localhost:3000`

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/email/send` | Send email |
| GET | `/api/email/list` | Get all emails |
| POST | `/api/sms/send` | Send SMS |
| GET | `/api/sms/list` | Get all SMS |
| POST | `/api/whatsapp/send` | Send WhatsApp |
| GET | `/api/whatsapp/list` | Get all WhatsApp |

## Usage

### Send Email
```bash
curl -X POST http://127.0.0.1:8000/api/email/send \
  -H "Content-Type: application/json" \
  -d '{"emailTo": "test@example.com"}'
```

### Send SMS
```bash
curl -X POST http://127.0.0.1:8000/api/sms/send \
  -H "Content-Type: application/json" \
  -d '{"mobileNumber": "9876543210", "message": "Hello"}'
```

## Project Structure

```
messaging-system/
├── backend/          # Django backend
│   ├── api/         # API app
│   └── manage.py
└── frontend/        # React frontend
    └── src/
        └── App.js
```
