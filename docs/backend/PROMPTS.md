# Backend Development Prompts - AA1-9 Invoice System

This document contains all the AI prompts used to generate the Django backend for the AA1-9 Automated Invoice Generation and Payment Tracking System.

## 🎯 Initial Project Setup Prompt

### Enhanced Development Prompt (Used for Backend Generation)

```
Create a comprehensive Django backend for an "Automated Invoice Generation and Payment Tracking System" with the following specifications:

**Core Requirements:**
1. **User Management & Authentication:**
   - Custom User model with roles (Admin, Accountant, Client, Viewer)
   - JWT authentication using djangorestframework-simplejwt
   - Role-based permissions and access control
   - User profiles with additional fields (phone, address, etc.)

2. **Client Management:**
   - Client model supporting both companies and individuals
   - Multiple contact persons per client
   - Client addresses and billing information
   - Client payment terms and credit limits

3. **Invoice Management:**
   - Comprehensive invoice system with line items
   - Invoice statuses (Draft, Sent, Paid, Overdue, Cancelled)
   - Automated invoice numbering
   - Tax calculations and discounts
   - Invoice templates and customization
   - PDF generation capabilities

4. **Payment Tracking:**
   - Payment model linked to invoices
   - Multiple payment methods support
   - Payment status tracking
   - Automated payment matching
   - Payment gateway integration preparation

**Technical Specifications:**
- Django 4.2 LTS with Django REST Framework
- PostgreSQL database with proper relationships
- Celery with Redis for background tasks
- Comprehensive API with proper serializers
- Environment-specific settings (development, production, testing)
- Docker containerization
- Pytest testing framework
- API documentation with drf-spectacular

**Project Structure:**
- Modular app architecture (users, clients, invoices, payments, core)
- Proper separation of concerns
- Scalable and maintainable codebase
- Following Django best practices

**Additional Features:**
- Email notifications system
- Audit logging for important actions
- API rate limiting
- Comprehensive error handling
- Data validation and security measures

Please create a complete project structure with all necessary files, configurations, and basic implementations ready for development.
```

## 🏗️ Architecture Design Prompts

### Database Schema Design Prompt

```
Design a comprehensive database schema for an invoice and payment tracking system with the following considerations:

1. **User Management:**
   - Extend AbstractUser for custom user model
   - Role-based access with proper permissions
   - User profiles with business-relevant fields

2. **Client Relationships:**
   - Support both individual and corporate clients
   - Multiple contacts per client organization
   - Flexible address system for billing and shipping

3. **Invoice Structure:**
   - Header information (client, dates, terms)
   - Line items with products/services
   - Tax calculations at line and invoice level
   - Discount applications
   - Status tracking throughout lifecycle

4. **Payment Integration:**
   - Link payments to specific invoices
   - Support partial payments
   - Multiple payment methods
   - Payment gateway transaction tracking

Ensure proper foreign key relationships, database constraints, and indexing for performance.
```

### API Design Prompt

```
Create a RESTful API design for the invoice system with the following endpoints:

**Authentication:**
- JWT token-based authentication
- Login, logout, refresh token endpoints
- Password reset functionality

**User Management:**
- CRUD operations with role-based access
- User profile management
- Permission checking

**Client Management:**
- Client CRUD with filtering and search
- Contact person management
- Client-specific invoice history

**Invoice Operations:**
- Invoice lifecycle management (create, update, send, pay)
- Line item management
- PDF generation endpoints
- Status updates and history

**Payment Processing:**
- Payment recording and tracking
- Payment method management
- Invoice-payment associations

Include proper HTTP status codes, error handling, pagination, and API versioning.
```

## 🔧 Implementation Prompts

### Models Implementation Prompt

```
Implement Django models for the invoice system with these specifications:

1. **User Model:**
   ```python
   class User(AbstractUser):
       # Add role field with choices
       # Additional profile fields
       # Proper string representation
   ```

2. **Client Model:**
   ```python
   class Client:
       # Company vs individual support
       # Contact information
       # Billing details
       # Payment terms
   ```

3. **Invoice Model:**
   ```python
   class Invoice:
       # Header information
       # Status tracking
       # Financial calculations
       # Audit fields
   ```

4. **Payment Model:**
   ```python
   class Payment:
       # Payment details
       # Gateway integration fields
       # Status tracking
   ```

Include proper model methods, managers, and validation.
```

### Serializers and Views Prompt

```
Create Django REST Framework serializers and viewsets for:

1. **Comprehensive Serializers:**
   - Nested serialization for related objects
   - Custom validation methods
   - Different serializers for list/detail views
   - Permission-based field filtering

2. **ViewSets with Proper Permissions:**
   - Role-based access control
   - Filtering and search capabilities
   - Custom actions for business logic
   - Proper error handling

3. **API Documentation:**
   - drf-spectacular integration
   - Comprehensive endpoint documentation
   - Example requests and responses

Ensure proper use of DRF best practices and security considerations.
```

## 🐳 Infrastructure Prompts

### Docker Configuration Prompt

```
Create comprehensive Docker configuration for the Django backend:

1. **Dockerfile:**
   - Multi-stage build for production
   - Proper Python dependencies management
   - Security best practices
   - Optimal image size

2. **Docker Compose:**
   - PostgreSQL service configuration
   - Redis for Celery tasks
   - Environment variable management
   - Volume mapping for development
   - Network configuration

3. **Development vs Production:**
   - Different configurations for each environment
   - Debug settings management
   - Static file serving
   - Database persistence

Include proper health checks and restart policies.
```

### Testing Framework Prompt

```
Set up comprehensive testing framework using pytest:

1. **Test Configuration:**
   - pytest.ini with proper settings
   - Test database configuration
   - Fixture definitions
   - Coverage reporting

2. **Test Categories:**
   - Unit tests for models and utilities
   - API endpoint tests
   - Authentication and permission tests
   - Integration tests for workflows

3. **Test Fixtures:**
   - User fixtures with different roles
   - Client and invoice test data
   - Authentication helpers

4. **Test Organization:**
   - Separate test files for each app
   - Proper test naming conventions
   - Test data cleanup

Ensure high test coverage and meaningful test scenarios.
```

## 🔄 Background Tasks Prompt

### Celery Configuration Prompt

```
Configure Celery for background task processing:

1. **Celery Setup:**
   - Proper Celery configuration in Django
   - Redis broker configuration
   - Task result backend setup
   - Worker and beat scheduling

2. **Task Definitions:**
   - Email notification tasks
   - Invoice PDF generation
   - Payment status updates
   - Scheduled reminder tasks

3. **Monitoring and Logging:**
   - Task status tracking
   - Error handling and retries
   - Performance monitoring
   - Logging configuration

4. **Production Considerations:**
   - Worker scaling
   - Resource management
   - Task prioritization

Include proper error handling and task monitoring.
```

## 📊 Additional Feature Prompts

### Email System Prompt

```
Implement email notification system:

1. **Email Configuration:**
   - SMTP settings for different environments
   - Template-based email system
   - HTML and text email support

2. **Notification Types:**
   - Invoice sent notifications
   - Payment confirmations
   - Overdue reminders
   - System alerts

3. **Email Queue:**
   - Celery-based email sending
   - Retry mechanisms for failed emails
   - Email tracking and logging

Include proper email templates and personalization.
```

### Security Implementation Prompt

```
Implement comprehensive security measures:

1. **Authentication Security:**
   - JWT token security
   - Password policies
   - Account lockout mechanisms
   - Two-factor authentication preparation

2. **API Security:**
   - Rate limiting
   - CORS configuration
   - Input validation
   - SQL injection protection

3. **Data Security:**
   - Sensitive data encryption
   - Audit logging
   - Data access controls
   - GDPR compliance preparation

4. **Infrastructure Security:**
   - Environment variable management
   - Secret key rotation
   - Database security
   - Network security

Include security testing and vulnerability assessment.
```

## 📝 Documentation Prompts

### API Documentation Prompt

```
Create comprehensive API documentation:

1. **OpenAPI/Swagger Integration:**
   - drf-spectacular configuration
   - Detailed endpoint documentation
   - Request/response examples
   - Authentication documentation

2. **Code Documentation:**
   - Docstrings for all functions and classes
   - Inline comments for complex logic
   - Architecture documentation
   - Setup and deployment guides

3. **User Guides:**
   - API usage examples
   - Authentication flow
   - Common use cases
   - Troubleshooting guides

Include interactive API documentation and code examples.
```

## 🚀 Deployment Prompts

### Production Deployment Prompt

```
Create production deployment configuration:

1. **Production Settings:**
   - Environment-specific Django settings
   - Security configurations
   - Performance optimizations
   - Logging configuration

2. **Infrastructure as Code:**
   - Docker production images
   - Database migration strategies
   - Static file serving
   - Load balancing preparation

3. **Monitoring and Logging:**
   - Application performance monitoring
   - Error tracking
   - Log aggregation
   - Health check endpoints

4. **CI/CD Pipeline:**
   - Automated testing
   - Deployment automation
   - Environment promotion
   - Rollback strategies

Include production checklist and monitoring setup.
```

## 🔄 Iteration and Enhancement Prompts

### Code Review and Optimization Prompt

```
Review and optimize the Django backend code:

1. **Performance Review:**
   - Database query optimization
   - N+1 query identification
   - Caching strategy implementation
   - API response time optimization

2. **Code Quality:**
   - PEP 8 compliance
   - Code complexity reduction
   - Refactoring opportunities
   - Documentation improvements

3. **Security Audit:**
   - Vulnerability assessment
   - Security best practices
   - Input validation review
   - Authentication flow security

4. **Scalability Considerations:**
   - Database scaling preparation
   - Caching strategy
   - Background task optimization
   - API rate limiting

Include specific recommendations and implementation guides.
```

## 📋 Usage Notes

### How to Use These Prompts

1. **Copy the relevant prompt** based on what you want to implement
2. **Customize the specifications** according to your specific requirements
3. **Provide context** about the existing codebase when iterating
4. **Break down complex prompts** into smaller, manageable parts
5. **Review and refine** the generated code according to your standards

### Best Practices

- Always provide clear context and requirements
- Include specific technology versions and constraints
- Mention coding standards and conventions to follow
- Specify testing requirements and coverage expectations
- Include security and performance considerations
- Request proper documentation and comments

### Prompt Evolution

These prompts were refined through multiple iterations to achieve the current backend implementation. Feel free to modify and enhance them based on your specific needs and lessons learned during development.

---

**Last Updated:** September 8, 2025  
**Version:** 1.0.0  
**Status:** Backend Implementation Complete
