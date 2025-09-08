# Backend - Django REST API

This directory contains the Django backend for the Invoice System.

## Features

- **User Management**: Role-based authentication (Admin, Accountant, Client, Viewer)
- **Client Management**: Complete client information with contacts
- **Invoice Generation**: Automated invoice creation with PDF generation
- **Payment Tracking**: Payment processing and reconciliation
- **Real-time Notifications**: Email and SMS notifications
- **API Documentation**: Swagger/OpenAPI documentation
- **Background Tasks**: Celery for scheduled tasks

## Tech Stack

- **Backend**: Django 4.2, Django REST Framework
- **Database**: PostgreSQL
- **Cache/Queue**: Redis, Celery
- **Authentication**: JWT (Simple JWT)
- **Documentation**: drf-yasg (Swagger)

## Project Structure

```
backend/
├── invoice_system/        # Main Django project
│   ├── core/             # Project settings and utilities
│   ├── users/            # User management
│   ├── clients/          # Client management
│   ├── invoices/         # Invoice management
│   └── payments/         # Payment processing
├── tests/                # Test files
├── static/               # Static files
├── media/                # Media files
├── logs/                 # Log files
└── manage.py            # Django management script
```

## Quick Start

1. **Setup virtual environment**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Environment setup**
   ```bash
   cp ../.env.example ../.env
   # Edit .env with your configuration
   ```

4. **Database setup**
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

5. **Run the development server**
   ```bash
   python manage.py runserver
   ```

## API Endpoints

- **Authentication**: `/api/v1/auth/`
- **Users**: `/api/v1/auth/users/`
- **Clients**: `/api/v1/clients/`
- **Invoices**: `/api/v1/invoices/`
- **Payments**: `/api/v1/payments/`
- **Documentation**: `/swagger/` and `/redoc/`

## Testing

```bash
pytest
pytest --cov=.
```

Visit the main project README for more details.
