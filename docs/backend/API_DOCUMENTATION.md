# API Documentation - AA1-9 Invoice System

## Base URL
```
Development: http://localhost:8000/api/v1/
Production: https://your-domain.com/api/v1/
```

## Authentication

All API endpoints (except login and password reset) require JWT authentication.

### Headers
```
Authorization: Bearer <access_token>
Content-Type: application/json
```

### Token Endpoints

#### Login
```http
POST /auth/login/
```

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "password123"
}
```

**Response:**
```json
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "user": {
    "id": 1,
    "email": "user@example.com",
    "first_name": "John",
    "last_name": "Doe",
    "role": "ACCOUNTANT"
  }
}
```

#### Refresh Token
```http
POST /auth/refresh/
```

#### Logout
```http
POST /auth/logout/
```

## User Management

### List Users
```http
GET /users/
```

**Query Parameters:**
- `role`: Filter by user role
- `is_active`: Filter by active status
- `search`: Search by name or email

### Create User
```http
POST /users/
```

### User Detail
```http
GET /users/{id}/
PUT /users/{id}/
PATCH /users/{id}/
DELETE /users/{id}/
```

## Client Management

### List Clients
```http
GET /clients/
```

**Query Parameters:**
- `client_type`: COMPANY or INDIVIDUAL
- `search`: Search by name or email
- `is_active`: Filter by active status

**Response:**
```json
{
  "count": 150,
  "next": "http://localhost:8000/api/v1/clients/?page=2",
  "previous": null,
  "results": [
    {
      "id": 1,
      "client_type": "COMPANY",
      "company_name": "ABC Corp",
      "first_name": null,
      "last_name": null,
      "email": "contact@abccorp.com",
      "phone": "+1-555-0123",
      "address": "123 Business St",
      "city": "New York",
      "state": "NY",
      "postal_code": "10001",
      "country": "USA",
      "is_active": true,
      "created_at": "2025-09-01T10:00:00Z",
      "contacts": [
        {
          "id": 1,
          "name": "John Smith",
          "email": "john@abccorp.com",
          "phone": "+1-555-0124",
          "position": "CFO",
          "is_primary": true
        }
      ]
    }
  ]
}
```

### Create Client
```http
POST /clients/
```

**Request Body:**
```json
{
  "client_type": "COMPANY",
  "company_name": "XYZ Inc",
  "email": "contact@xyzinc.com",
  "phone": "+1-555-0199",
  "address": "456 Corporate Ave",
  "city": "Los Angeles",
  "state": "CA",
  "postal_code": "90210",
  "country": "USA",
  "contacts": [
    {
      "name": "Jane Doe",
      "email": "jane@xyzinc.com",
      "phone": "+1-555-0200",
      "position": "CEO",
      "is_primary": true
    }
  ]
}
```

### Client Detail
```http
GET /clients/{id}/
PUT /clients/{id}/
PATCH /clients/{id}/
DELETE /clients/{id}/
```

### Client Invoices
```http
GET /clients/{id}/invoices/
```

## Invoice Management

### List Invoices
```http
GET /invoices/
```

**Query Parameters:**
- `status`: DRAFT, SENT, PAID, OVERDUE, CANCELLED
- `client`: Client ID
- `date_from`: Start date (YYYY-MM-DD)
- `date_to`: End date (YYYY-MM-DD)
- `amount_min`: Minimum amount
- `amount_max`: Maximum amount
- `search`: Search by invoice number

**Response:**
```json
{
  "count": 50,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "invoice_number": "INV-2025-001",
      "client": {
        "id": 1,
        "name": "ABC Corp",
        "email": "contact@abccorp.com"
      },
      "issue_date": "2025-09-01",
      "due_date": "2025-09-31",
      "status": "SENT",
      "subtotal": "1000.00",
      "tax_amount": "100.00",
      "total_amount": "1100.00",
      "amount_paid": "0.00",
      "balance_due": "1100.00",
      "created_at": "2025-09-01T10:00:00Z",
      "updated_at": "2025-09-01T10:00:00Z"
    }
  ]
}
```

### Create Invoice
```http
POST /invoices/
```

**Request Body:**
```json
{
  "client": 1,
  "issue_date": "2025-09-08",
  "due_date": "2025-10-08",
  "payment_terms": "Net 30",
  "notes": "Thank you for your business",
  "line_items": [
    {
      "description": "Web Development Services",
      "quantity": 40,
      "rate": "100.00",
      "tax_rate": "10.00"
    },
    {
      "description": "Hosting Setup",
      "quantity": 1,
      "rate": "200.00",
      "tax_rate": "10.00"
    }
  ]
}
```

### Invoice Detail
```http
GET /invoices/{id}/
PUT /invoices/{id}/
PATCH /invoices/{id}/
DELETE /invoices/{id}/
```

### Invoice Actions

#### Send Invoice
```http
POST /invoices/{id}/send/
```

**Request Body:**
```json
{
  "to_email": "client@example.com",
  "cc_emails": ["manager@company.com"],
  "subject": "Invoice INV-2025-001",
  "message": "Please find attached your invoice."
}
```

#### Generate PDF
```http
GET /invoices/{id}/pdf/
```

**Response:** PDF file download

#### Duplicate Invoice
```http
POST /invoices/{id}/duplicate/
```

### Line Items
```http
GET /invoices/{id}/line-items/
POST /invoices/{id}/line-items/
PUT /invoices/{id}/line-items/{item_id}/
DELETE /invoices/{id}/line-items/{item_id}/
```

## Payment Management

### List Payments
```http
GET /payments/
```

**Query Parameters:**
- `invoice`: Invoice ID
- `payment_method`: Payment method
- `date_from`: Start date
- `date_to`: End date
- `amount_min`: Minimum amount
- `amount_max`: Maximum amount

**Response:**
```json
{
  "count": 25,
  "results": [
    {
      "id": 1,
      "invoice": {
        "id": 1,
        "invoice_number": "INV-2025-001",
        "total_amount": "1100.00"
      },
      "amount": "1100.00",
      "payment_method": "BANK_TRANSFER",
      "payment_date": "2025-09-15",
      "reference_number": "TXN123456",
      "notes": "Payment received via bank transfer",
      "created_at": "2025-09-15T14:30:00Z"
    }
  ]
}
```

### Record Payment
```http
POST /payments/
```

**Request Body:**
```json
{
  "invoice": 1,
  "amount": "1100.00",
  "payment_method": "BANK_TRANSFER",
  "payment_date": "2025-09-15",
  "reference_number": "TXN123456",
  "notes": "Full payment received"
}
```

### Payment Detail
```http
GET /payments/{id}/
PUT /payments/{id}/
PATCH /payments/{id}/
DELETE /payments/{id}/
```

## Reporting

### Financial Summary
```http
GET /reports/financial-summary/
```

**Query Parameters:**
- `period`: MONTHLY, QUARTERLY, YEARLY
- `year`: Year (YYYY)
- `month`: Month (MM)

### Aging Report
```http
GET /reports/aging/
```

### Client Report
```http
GET /reports/clients/{client_id}/
```

## Error Responses

### Error Format
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid input data",
    "details": {
      "email": ["This field is required."],
      "amount": ["Ensure this value is greater than 0."]
    }
  }
}
```

### HTTP Status Codes

- `200 OK` - Successful GET, PUT, PATCH
- `201 Created` - Successful POST
- `204 No Content` - Successful DELETE
- `400 Bad Request` - Validation errors
- `401 Unauthorized` - Authentication required
- `403 Forbidden` - Permission denied
- `404 Not Found` - Resource not found
- `429 Too Many Requests` - Rate limit exceeded
- `500 Internal Server Error` - Server error

## Rate Limiting

- **Authenticated users:** 100 requests per minute
- **Anonymous users:** 20 requests per minute

Rate limit headers:
```
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 95
X-RateLimit-Reset: 1620000000
```

## Pagination

List endpoints use cursor-based pagination:

```json
{
  "count": 150,
  "next": "http://localhost:8000/api/v1/invoices/?cursor=xyz",
  "previous": null,
  "results": [...]
}
```

## Filtering and Search

Most list endpoints support:
- **Filtering:** Use query parameters for exact matches
- **Search:** Use `search` parameter for text search
- **Ordering:** Use `ordering` parameter (prefix with `-` for descending)

Example:
```
GET /invoices/?status=SENT&client=1&ordering=-created_at
```

## Webhooks (Future)

Webhook endpoints will be available for:
- Invoice status changes
- Payment received
- Client updates
- System events

## API Versioning

- Current version: `v1`
- Version specified in URL: `/api/v1/`
- Backward compatibility maintained for major versions
- Deprecation notices provided 6 months in advance
