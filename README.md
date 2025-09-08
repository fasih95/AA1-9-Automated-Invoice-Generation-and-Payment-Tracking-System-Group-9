# Invoice System - Automated Invoice Generation and Payment Tracking

A comprehensive invoice generation and payment tracking system with Django backend and Vue.js frontend.

## Project Structure

```
group-9/
├── backend/               # Django REST API
│   ├── invoice_system/    # Main Django project
│   │   ├── core/         # Project settings and utilities
│   │   ├── users/        # User management
│   │   ├── clients/      # Client management
│   │   ├── invoices/     # Invoice management
│   │   └── payments/     # Payment processing
│   ├── tests/            # Backend tests
│   ├── requirements.txt  # Python dependencies
│   └── manage.py        # Django management
├── frontend/             # Vue.js application (planned)
├── docker-compose.yml    # Multi-service Docker setup
├── .env.example         # Environment variables template
└── setup scripts       # Quick setup scripts
```

## Features

### Backend (Django REST API)
- **User Management**: Role-based authentication (Admin, Accountant, Client, Viewer)
- **Client Management**: Complete client information with contacts
- **Invoice Generation**: Automated invoice creation with PDF generation
- **Payment Tracking**: Payment processing and reconciliation
- **Real-time Notifications**: Email and SMS notifications
- **API Documentation**: Swagger/OpenAPI documentation
- **Background Tasks**: Celery for scheduled tasks

### Frontend (Vue.js - Planned)
- **Modern Vue.js 3** with Composition API
- **Responsive Design** for mobile and desktop
- **Real-time Updates** with WebSocket support
- **Interactive Dashboard** with charts and analytics
- **Print-ready Invoices** with PDF export
- **Client Portal** for invoice viewing and payment

## Tech Stack

### Backend
- **Framework**: Django 4.2, Django REST Framework
- **Database**: PostgreSQL
- **Cache/Queue**: Redis, Celery
- **Authentication**: JWT (Simple JWT)
- **Documentation**: drf-yasg (Swagger)
- **Containerization**: Docker, Docker Compose

### Frontend (Planned)
- **Framework**: Vue.js 3
- **State Management**: Pinia
- **Routing**: Vue Router
- **UI Components**: Tailwind CSS or Vuetify
- **HTTP Client**: Axios
- **Build Tool**: Vite

## Quick Start

### Option 1: Docker (Recommended)

1. **Clone and setup**
   ```bash
   git clone <repository-url>
   cd group-9
   cp .env.example .env
   # Edit .env with your configuration
   ```

2. **Run with Docker Compose**
   ```bash
   docker-compose up --build
   ```

3. **Setup database (in another terminal)**
   ```bash
   docker-compose exec backend python manage.py migrate
   docker-compose exec backend python manage.py createsuperuser
   ```

### Option 2: Local Development

1. **Run setup script**
   ```bash
   # Windows
   ./setup.bat
   
   # Linux/Mac
   ./setup.sh
   ```

2. **Backend setup**
   ```bash
   cd backend
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py runserver
   ```

## API Documentation

Once the backend is running, visit:
- **Swagger UI**: http://localhost:8000/swagger/
- **ReDoc**: http://localhost:8000/redoc/
- **Admin Panel**: http://localhost:8000/admin/

## API Endpoints

### Authentication
- `POST /api/v1/auth/register/` - User registration
- `POST /api/v1/auth/login/` - User login
- `POST /api/v1/auth/logout/` - User logout
- `POST /api/v1/auth/change-password/` - Change password

### Users
- `GET /api/v1/auth/users/` - List users
- `GET /api/v1/auth/users/{id}/` - User details
- `GET /api/v1/auth/profile/` - Current user profile

### Clients
- `GET /api/v1/clients/` - List clients
- `POST /api/v1/clients/` - Create client
- `GET /api/v1/clients/{id}/` - Client details
- `PUT /api/v1/clients/{id}/` - Update client
- `DELETE /api/v1/clients/{id}/` - Delete client

### Invoices
- `GET /api/v1/invoices/` - List invoices
- `POST /api/v1/invoices/` - Create invoice
- `GET /api/v1/invoices/{id}/` - Invoice details
- `GET /api/v1/invoices/{id}/pdf/` - Download invoice PDF

### Payments
- `GET /api/v1/payments/` - List payments
- `POST /api/v1/payments/` - Record payment
- `GET /api/v1/payments/{id}/` - Payment details

## Development Workflow

### Backend Development
```bash
cd backend
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Run tests
pytest

# Code formatting
black .
isort .
flake8

# Start development server
python manage.py runserver
```

### Celery (Background Tasks)
```bash
# Worker
celery -A core worker -l info

# Beat scheduler
celery -A core beat -l info
```

## Environment Variables

Key environment variables (see `.env.example`):

- `SECRET_KEY`: Django secret key
- `DEBUG`: Debug mode flag
- `DB_NAME`, `DB_USER`, `DB_PASSWORD`: Database credentials
- `REDIS_URL`: Redis connection URL
- `EMAIL_HOST`, `EMAIL_PORT`: Email server settings

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Run the test suite
6. Submit a pull request

## JIRA Integration

This project is tracked under **AA1-9** in the AZM Development JIRA instance:
- **Epic**: Automated Invoice Generation and Payment Tracking System - Group 9
- **JIRA URL**: https://azm-development.atlassian.net/browse/AA1-9

## License

This project is licensed under the MIT License.

## Support

For questions and support, please contact the development team.
