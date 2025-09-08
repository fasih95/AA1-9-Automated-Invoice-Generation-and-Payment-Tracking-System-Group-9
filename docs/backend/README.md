# Backend Documentation - AA1-9 Invoice System

## Django Backend Overview

The backend is built using Django 4.2 LTS with Django REST Framework, providing a robust API for the invoice generation and payment tracking system.

## 🏗️ Architecture

### Project Structure
```
backend/
├── invoice_system/              # Main Django project
│   ├── core/                   # Core settings and configuration
│   │   ├── settings/           # Environment-specific settings
│   │   ├── celery.py          # Celery configuration
│   │   └── utils.py           # Shared utilities
│   ├── users/                  # User management and authentication
│   ├── clients/                # Client management
│   ├── invoices/               # Invoice management
│   ├── payments/               # Payment tracking
│   └── static/                 # Static files
├── tests/                      # Test suite
├── requirements.txt            # Python dependencies
├── manage.py                   # Django management script
└── Dockerfile                  # Docker configuration
```

## 🔧 Technology Stack

- **Framework:** Django 4.2 LTS
- **API:** Django REST Framework 3.14
- **Authentication:** JWT (djangorestframework-simplejwt)
- **Database:** PostgreSQL 15
- **Cache/Queue:** Redis + Celery
- **Testing:** Pytest + pytest-django
- **Documentation:** drf-spectacular (OpenAPI/Swagger)

## 🚀 Getting Started

### Prerequisites
- Python 3.11+
- PostgreSQL 15+
- Redis (for Celery tasks)
- Docker & Docker Compose (optional)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/fasih95/AA1-9-Automated-Invoice-Generation-and-Payment-Tracking-System-Group-9.git
   cd AA1-9-Automated-Invoice-Generation-and-Payment-Tracking-System-Group-9
   ```

2. **Set up environment:**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Configure environment variables:**
   ```bash
   cp ../.env.example .env
   # Edit .env with your database and Redis settings
   ```

4. **Run migrations:**
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

5. **Start development server:**
   ```bash
   python manage.py runserver
   ```

### Docker Setup

```bash
# From project root
docker-compose up -d
```

## 📊 Database Models

### User Model
- Custom user model extending AbstractUser
- Role-based permissions (Admin, Accountant, Client, Viewer)
- User profiles with additional fields

### Client Model
- Company and individual client support
- Multiple contact persons per client
- Address and billing information

### Invoice Model
- Comprehensive invoice management
- Status tracking (Draft, Sent, Paid, Overdue)
- Line items with products/services
- Tax calculations and discounts

### Payment Model
- Payment tracking and gateway integration
- Payment methods and status
- Automated matching with invoices

## 🔐 Authentication & Permissions

### JWT Authentication
- Access and refresh token system
- Token expiration and rotation
- Role-based access control

### Permission Classes
- `IsAuthenticated` - Requires valid JWT token
- `IsAdminUser` - Admin-only access
- `IsAccountantOrAdmin` - Accounting staff access
- `IsClientOwner` - Client can only access their data

## 🛠️ API Endpoints

### Authentication
- `POST /api/v1/auth/login/` - User login
- `POST /api/v1/auth/refresh/` - Token refresh
- `POST /api/v1/auth/logout/` - User logout

### Users
- `GET /api/v1/users/` - List users
- `POST /api/v1/users/` - Create user
- `GET /api/v1/users/{id}/` - User details
- `PUT /api/v1/users/{id}/` - Update user

### Clients
- `GET /api/v1/clients/` - List clients
- `POST /api/v1/clients/` - Create client
- `GET /api/v1/clients/{id}/` - Client details

### Invoices
- `GET /api/v1/invoices/` - List invoices
- `POST /api/v1/invoices/` - Create invoice
- `GET /api/v1/invoices/{id}/` - Invoice details
- `PUT /api/v1/invoices/{id}/` - Update invoice

### Payments
- `GET /api/v1/payments/` - List payments
- `POST /api/v1/payments/` - Record payment

## 🧪 Testing

### Running Tests
```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_users.py

# Run with coverage
pytest --cov=invoice_system
```

### Test Structure
- Unit tests for models and utilities
- API endpoint tests
- Authentication and permission tests
- Integration tests for complex workflows

## 📈 Performance Considerations

### Database Optimization
- Proper indexing on frequently queried fields
- Database connection pooling
- Query optimization with select_related and prefetch_related

### Caching Strategy
- Redis for session storage
- API response caching for read-heavy endpoints
- Celery for background tasks

### Security Features
- CORS configuration
- SQL injection protection
- XSS protection
- CSRF protection
- Rate limiting

## 🔄 Background Tasks (Celery)

### Scheduled Tasks
- Invoice reminder emails
- Payment status updates
- Report generation
- Data cleanup tasks

### Task Queue
- Email notifications
- PDF generation
- External API calls
- Bulk operations

## 📝 Development Guidelines

### Code Style
- Follow PEP 8 guidelines
- Use Black for code formatting
- Type hints for function parameters
- Comprehensive docstrings

### Git Workflow
- Feature branch development
- Pull request reviews
- Automated testing on CI/CD
- Semantic commit messages

## 🚀 Deployment

### Production Environment
- Gunicorn WSGI server
- Nginx reverse proxy
- PostgreSQL database
- Redis for caching and queues
- Docker containerization

### Environment Variables
```bash
DJANGO_SETTINGS_MODULE=core.settings.production
DATABASE_URL=postgresql://user:pass@host:port/dbname
REDIS_URL=redis://host:port/0
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=your-domain.com
```

## 📋 TODO / Future Enhancements

- [ ] Advanced reporting and analytics
- [ ] Multi-tenant support
- [ ] Advanced PDF customization
- [ ] Integration with accounting software
- [ ] Mobile API optimizations
- [ ] Advanced search and filtering
- [ ] Automated testing for payment gateways

## 🐛 Troubleshooting

### Common Issues
1. **Database connection errors:** Check PostgreSQL service and credentials
2. **Celery tasks not running:** Ensure Redis is running and accessible
3. **JWT token issues:** Verify token expiration settings
4. **Migration conflicts:** Use `python manage.py migrate --fake-initial`

### Debug Mode
Set `DEBUG=True` in development environment for detailed error messages and Django debug toolbar.

## 📞 Support

For technical support or questions about the backend implementation, please refer to the development team or create an issue in the GitHub repository.
