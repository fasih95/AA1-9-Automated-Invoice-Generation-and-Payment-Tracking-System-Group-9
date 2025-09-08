# Database Schema - AA1-9 Invoice System

## Overview

The database schema is designed to support a comprehensive invoice generation and payment tracking system with the following key entities:

- **Users** - System users with role-based access
- **Clients** - Companies and individuals who receive invoices
- **Invoices** - Invoice records with line items
- **Payments** - Payment tracking and history
- **Audit** - System activity logging

## Entity Relationship Diagram

```
┌─────────────┐       ┌─────────────┐       ┌─────────────┐
│    Users    │       │   Clients   │       │  Invoices   │
│             │       │             │       │             │
│ id (PK)     │       │ id (PK)     │       │ id (PK)     │
│ email       │       │ client_type │   ┌───│ client_id   │
│ role        │   ┌───│ company_name│   │   │ created_by  │───┐
│ first_name  │   │   │ first_name  │   │   │ status      │   │
│ last_name   │   │   │ last_name   │   │   │ total_amount│   │
│ is_active   │   │   │ email       │   │   │ ...         │   │
│ ...         │   │   │ ...         │   │   └─────────────┘   │
└─────────────┘   │   └─────────────┘   │                     │
                  │            │        │                     │
                  │            └────────┘                     │
                  │                                           │
                  │   ┌─────────────┐       ┌─────────────┐   │
                  │   │ClientContact│       │InvoiceItems │   │
                  │   │             │       │             │   │
                  │   │ id (PK)     │       │ id (PK)     │   │
                  └───│ client_id   │   ┌───│ invoice_id  │   │
                      │ name        │   │   │ description │   │
                      │ email       │   │   │ quantity    │   │
                      │ position    │   │   │ rate        │   │
                      │ is_primary  │   │   │ amount      │   │
                      │ ...         │   │   │ ...         │   │
                      └─────────────┘   │   └─────────────┘   │
                                        │                     │
┌─────────────┐                         │                     │
│  Payments   │                         └─────────────────────┘
│             │
│ id (PK)     │
│ invoice_id  │───────────────────────────┘
│ amount      │
│ method      │
│ status      │
│ ...         │
└─────────────┘
```

## Table Definitions

### Users Table

```sql
CREATE TABLE users_user (
    id SERIAL PRIMARY KEY,
    password VARCHAR(128) NOT NULL,
    last_login TIMESTAMP WITH TIME ZONE,
    is_superuser BOOLEAN NOT NULL DEFAULT FALSE,
    username VARCHAR(150) NOT NULL UNIQUE,
    email VARCHAR(254) NOT NULL UNIQUE,
    first_name VARCHAR(150) NOT NULL,
    last_name VARCHAR(150) NOT NULL,
    is_staff BOOLEAN NOT NULL DEFAULT FALSE,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    date_joined TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    
    -- Custom fields
    role VARCHAR(20) NOT NULL DEFAULT 'VIEWER',
    phone VARCHAR(20),
    address TEXT,
    city VARCHAR(100),
    state VARCHAR(100),
    postal_code VARCHAR(20),
    country VARCHAR(100) DEFAULT 'USA',
    
    -- Timestamps
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW()
);

-- Indexes
CREATE INDEX idx_users_email ON users_user(email);
CREATE INDEX idx_users_role ON users_user(role);
CREATE INDEX idx_users_is_active ON users_user(is_active);
```

**Role Choices:**
- `ADMIN` - System administrator
- `ACCOUNTANT` - Accounting staff
- `CLIENT` - Client user
- `VIEWER` - Read-only user

### Clients Table

```sql
CREATE TABLE clients_client (
    id SERIAL PRIMARY KEY,
    client_type VARCHAR(20) NOT NULL DEFAULT 'COMPANY',
    
    -- Company fields
    company_name VARCHAR(200),
    tax_id VARCHAR(50),
    
    -- Individual fields
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    
    -- Common fields
    email VARCHAR(254) NOT NULL,
    phone VARCHAR(20),
    website VARCHAR(200),
    
    -- Address
    address TEXT,
    city VARCHAR(100),
    state VARCHAR(100),
    postal_code VARCHAR(20),
    country VARCHAR(100) DEFAULT 'USA',
    
    -- Business details
    payment_terms VARCHAR(50) DEFAULT 'Net 30',
    credit_limit DECIMAL(10,2),
    currency VARCHAR(3) DEFAULT 'USD',
    
    -- Status
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    
    -- Timestamps
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    created_by INTEGER REFERENCES users_user(id) ON DELETE SET NULL
);

-- Indexes
CREATE INDEX idx_clients_type ON clients_client(client_type);
CREATE INDEX idx_clients_email ON clients_client(email);
CREATE INDEX idx_clients_active ON clients_client(is_active);
CREATE INDEX idx_clients_company ON clients_client(company_name);
```

**Client Type Choices:**
- `COMPANY` - Business client
- `INDIVIDUAL` - Individual client

### Client Contacts Table

```sql
CREATE TABLE clients_clientcontact (
    id SERIAL PRIMARY KEY,
    client_id INTEGER NOT NULL REFERENCES clients_client(id) ON DELETE CASCADE,
    name VARCHAR(200) NOT NULL,
    email VARCHAR(254),
    phone VARCHAR(20),
    position VARCHAR(100),
    is_primary BOOLEAN NOT NULL DEFAULT FALSE,
    notes TEXT,
    
    -- Timestamps
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW()
);

-- Indexes
CREATE INDEX idx_clientcontacts_client ON clients_clientcontact(client_id);
CREATE INDEX idx_clientcontacts_primary ON clients_clientcontact(is_primary);
```

### Invoices Table

```sql
CREATE TABLE invoices_invoice (
    id SERIAL PRIMARY KEY,
    invoice_number VARCHAR(50) NOT NULL UNIQUE,
    client_id INTEGER NOT NULL REFERENCES clients_client(id) ON DELETE PROTECT,
    
    -- Dates
    issue_date DATE NOT NULL,
    due_date DATE NOT NULL,
    
    -- Status
    status VARCHAR(20) NOT NULL DEFAULT 'DRAFT',
    
    -- Financial details
    subtotal DECIMAL(10,2) NOT NULL DEFAULT 0.00,
    tax_rate DECIMAL(5,2) NOT NULL DEFAULT 0.00,
    tax_amount DECIMAL(10,2) NOT NULL DEFAULT 0.00,
    discount_amount DECIMAL(10,2) NOT NULL DEFAULT 0.00,
    total_amount DECIMAL(10,2) NOT NULL DEFAULT 0.00,
    amount_paid DECIMAL(10,2) NOT NULL DEFAULT 0.00,
    
    -- Terms and notes
    payment_terms VARCHAR(100) DEFAULT 'Net 30',
    notes TEXT,
    internal_notes TEXT,
    
    -- Timestamps
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    sent_at TIMESTAMP WITH TIME ZONE,
    created_by INTEGER REFERENCES users_user(id) ON DELETE SET NULL
);

-- Indexes
CREATE INDEX idx_invoices_client ON invoices_invoice(client_id);
CREATE INDEX idx_invoices_status ON invoices_invoice(status);
CREATE INDEX idx_invoices_number ON invoices_invoice(invoice_number);
CREATE INDEX idx_invoices_dates ON invoices_invoice(issue_date, due_date);
CREATE INDEX idx_invoices_amount ON invoices_invoice(total_amount);
```

**Status Choices:**
- `DRAFT` - Draft invoice
- `SENT` - Sent to client
- `PAID` - Fully paid
- `PARTIALLY_PAID` - Partially paid
- `OVERDUE` - Past due date
- `CANCELLED` - Cancelled invoice

### Invoice Line Items Table

```sql
CREATE TABLE invoices_invoicelineitem (
    id SERIAL PRIMARY KEY,
    invoice_id INTEGER NOT NULL REFERENCES invoices_invoice(id) ON DELETE CASCADE,
    line_number INTEGER NOT NULL DEFAULT 1,
    
    -- Item details
    description TEXT NOT NULL,
    quantity DECIMAL(10,2) NOT NULL DEFAULT 1.00,
    rate DECIMAL(10,2) NOT NULL DEFAULT 0.00,
    amount DECIMAL(10,2) NOT NULL DEFAULT 0.00,
    
    -- Tax
    tax_rate DECIMAL(5,2) NOT NULL DEFAULT 0.00,
    tax_amount DECIMAL(10,2) NOT NULL DEFAULT 0.00,
    
    -- Product reference (optional)
    product_code VARCHAR(50),
    
    -- Timestamps
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW()
);

-- Indexes
CREATE INDEX idx_invoiceitems_invoice ON invoices_invoicelineitem(invoice_id);
CREATE INDEX idx_invoiceitems_line_number ON invoices_invoicelineitem(invoice_id, line_number);
```

### Payments Table

```sql
CREATE TABLE payments_payment (
    id SERIAL PRIMARY KEY,
    invoice_id INTEGER NOT NULL REFERENCES invoices_invoice(id) ON DELETE PROTECT,
    
    -- Payment details
    amount DECIMAL(10,2) NOT NULL,
    payment_method VARCHAR(50) NOT NULL,
    payment_date DATE NOT NULL,
    
    -- Transaction details
    reference_number VARCHAR(100),
    transaction_id VARCHAR(100),
    gateway_response TEXT,
    
    -- Status
    status VARCHAR(20) NOT NULL DEFAULT 'COMPLETED',
    
    -- Notes
    notes TEXT,
    internal_notes TEXT,
    
    -- Timestamps
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    created_by INTEGER REFERENCES users_user(id) ON DELETE SET NULL
);

-- Indexes
CREATE INDEX idx_payments_invoice ON payments_payment(invoice_id);
CREATE INDEX idx_payments_method ON payments_payment(payment_method);
CREATE INDEX idx_payments_date ON payments_payment(payment_date);
CREATE INDEX idx_payments_status ON payments_payment(status);
CREATE INDEX idx_payments_reference ON payments_payment(reference_number);
```

**Payment Method Choices:**
- `CASH` - Cash payment
- `CHECK` - Check payment
- `BANK_TRANSFER` - Bank transfer
- `CREDIT_CARD` - Credit card
- `DEBIT_CARD` - Debit card
- `PAYPAL` - PayPal
- `STRIPE` - Stripe
- `OTHER` - Other method

**Status Choices:**
- `PENDING` - Payment pending
- `COMPLETED` - Payment completed
- `FAILED` - Payment failed
- `REFUNDED` - Payment refunded

## Database Constraints

### Foreign Key Constraints

```sql
-- Invoice must have a valid client
ALTER TABLE invoices_invoice 
ADD CONSTRAINT fk_invoice_client 
FOREIGN KEY (client_id) REFERENCES clients_client(id) ON DELETE PROTECT;

-- Payment must have a valid invoice
ALTER TABLE payments_payment 
ADD CONSTRAINT fk_payment_invoice 
FOREIGN KEY (invoice_id) REFERENCES invoices_invoice(id) ON DELETE PROTECT;

-- Line items must have a valid invoice
ALTER TABLE invoices_invoicelineitem 
ADD CONSTRAINT fk_lineitem_invoice 
FOREIGN KEY (invoice_id) REFERENCES invoices_invoice(id) ON DELETE CASCADE;
```

### Check Constraints

```sql
-- Ensure positive amounts
ALTER TABLE invoices_invoice 
ADD CONSTRAINT chk_invoice_amounts_positive 
CHECK (subtotal >= 0 AND tax_amount >= 0 AND total_amount >= 0 AND amount_paid >= 0);

ALTER TABLE payments_payment 
ADD CONSTRAINT chk_payment_amount_positive 
CHECK (amount > 0);

ALTER TABLE invoices_invoicelineitem 
ADD CONSTRAINT chk_lineitem_amounts_positive 
CHECK (quantity > 0 AND rate >= 0 AND amount >= 0);

-- Ensure due date is after issue date
ALTER TABLE invoices_invoice 
ADD CONSTRAINT chk_invoice_dates 
CHECK (due_date >= issue_date);

-- Ensure tax rates are reasonable
ALTER TABLE invoices_invoice 
ADD CONSTRAINT chk_invoice_tax_rate 
CHECK (tax_rate >= 0 AND tax_rate <= 100);
```

### Unique Constraints

```sql
-- Invoice numbers must be unique
ALTER TABLE invoices_invoice 
ADD CONSTRAINT uk_invoice_number 
UNIQUE (invoice_number);

-- User emails must be unique
ALTER TABLE users_user 
ADD CONSTRAINT uk_user_email 
UNIQUE (email);

-- Only one primary contact per client
CREATE UNIQUE INDEX uk_client_primary_contact 
ON clients_clientcontact(client_id) 
WHERE is_primary = TRUE;
```

## Triggers and Functions

### Auto-update timestamps

```sql
-- Function to update the updated_at timestamp
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ language 'plpgsql';

-- Triggers for all tables
CREATE TRIGGER update_users_updated_at 
    BEFORE UPDATE ON users_user 
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_clients_updated_at 
    BEFORE UPDATE ON clients_client 
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_invoices_updated_at 
    BEFORE UPDATE ON invoices_invoice 
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();
```

### Invoice number generation

```sql
-- Function to generate invoice numbers
CREATE OR REPLACE FUNCTION generate_invoice_number()
RETURNS TRIGGER AS $$
DECLARE
    year_part TEXT;
    sequence_num INTEGER;
BEGIN
    IF NEW.invoice_number IS NULL OR NEW.invoice_number = '' THEN
        year_part := EXTRACT(YEAR FROM NEW.issue_date)::TEXT;
        
        SELECT COALESCE(MAX(
            CAST(SPLIT_PART(invoice_number, '-', 3) AS INTEGER)
        ), 0) + 1
        INTO sequence_num
        FROM invoices_invoice
        WHERE invoice_number LIKE 'INV-' || year_part || '-%';
        
        NEW.invoice_number := 'INV-' || year_part || '-' || LPAD(sequence_num::TEXT, 3, '0');
    END IF;
    
    RETURN NEW;
END;
$$ language 'plpgsql';

CREATE TRIGGER generate_invoice_number_trigger
    BEFORE INSERT ON invoices_invoice
    FOR EACH ROW EXECUTE FUNCTION generate_invoice_number();
```

### Calculate invoice totals

```sql
-- Function to calculate invoice totals
CREATE OR REPLACE FUNCTION calculate_invoice_totals()
RETURNS TRIGGER AS $$
DECLARE
    invoice_record RECORD;
BEGIN
    -- Get the invoice ID
    IF TG_OP = 'DELETE' THEN
        invoice_record.id := OLD.invoice_id;
    ELSE
        invoice_record.id := NEW.invoice_id;
    END IF;
    
    -- Update invoice totals
    UPDATE invoices_invoice SET
        subtotal = COALESCE((
            SELECT SUM(amount)
            FROM invoices_invoicelineitem
            WHERE invoice_id = invoice_record.id
        ), 0),
        tax_amount = COALESCE((
            SELECT SUM(tax_amount)
            FROM invoices_invoicelineitem
            WHERE invoice_id = invoice_record.id
        ), 0)
    WHERE id = invoice_record.id;
    
    -- Calculate total amount
    UPDATE invoices_invoice SET
        total_amount = subtotal + tax_amount - discount_amount
    WHERE id = invoice_record.id;
    
    RETURN COALESCE(NEW, OLD);
END;
$$ language 'plpgsql';

CREATE TRIGGER calculate_invoice_totals_trigger
    AFTER INSERT OR UPDATE OR DELETE ON invoices_invoicelineitem
    FOR EACH ROW EXECUTE FUNCTION calculate_invoice_totals();
```

## Views

### Invoice Summary View

```sql
CREATE VIEW vw_invoice_summary AS
SELECT 
    i.id,
    i.invoice_number,
    i.issue_date,
    i.due_date,
    i.status,
    i.total_amount,
    i.amount_paid,
    (i.total_amount - i.amount_paid) AS balance_due,
    c.company_name,
    c.first_name,
    c.last_name,
    CASE 
        WHEN c.client_type = 'COMPANY' THEN c.company_name
        ELSE c.first_name || ' ' || c.last_name
    END AS client_name,
    c.email AS client_email,
    CASE 
        WHEN i.status = 'SENT' AND i.due_date < CURRENT_DATE THEN 'OVERDUE'
        ELSE i.status
    END AS computed_status,
    (i.due_date - CURRENT_DATE) AS days_to_due
FROM invoices_invoice i
JOIN clients_client c ON i.client_id = c.id;
```

### Payment Summary View

```sql
CREATE VIEW vw_payment_summary AS
SELECT 
    p.id,
    p.amount,
    p.payment_method,
    p.payment_date,
    p.status,
    i.invoice_number,
    i.total_amount AS invoice_total,
    c.company_name,
    c.first_name,
    c.last_name,
    CASE 
        WHEN c.client_type = 'COMPANY' THEN c.company_name
        ELSE c.first_name || ' ' || c.last_name
    END AS client_name
FROM payments_payment p
JOIN invoices_invoice i ON p.invoice_id = i.id
JOIN clients_client c ON i.client_id = c.id;
```

## Indexes for Performance

```sql
-- Composite indexes for common queries
CREATE INDEX idx_invoices_client_status ON invoices_invoice(client_id, status);
CREATE INDEX idx_invoices_status_date ON invoices_invoice(status, due_date);
CREATE INDEX idx_payments_invoice_status ON payments_payment(invoice_id, status);
CREATE INDEX idx_invoices_created_by_date ON invoices_invoice(created_by, created_at);

-- Full-text search indexes (PostgreSQL specific)
CREATE INDEX idx_clients_search ON clients_client USING gin(
    to_tsvector('english', 
        COALESCE(company_name, '') || ' ' || 
        COALESCE(first_name, '') || ' ' || 
        COALESCE(last_name, '') || ' ' || 
        COALESCE(email, '')
    )
);
```

## Database Maintenance

### Regular Maintenance Tasks

1. **Update Statistics:**
   ```sql
   ANALYZE;
   ```

2. **Vacuum Tables:**
   ```sql
   VACUUM ANALYZE;
   ```

3. **Reindex:**
   ```sql
   REINDEX DATABASE invoice_system;
   ```

### Backup Strategy

- **Daily backups** of the entire database
- **Point-in-time recovery** capability
- **Weekly full backups** with compression
- **Monthly archive backups** for long-term storage

### Monitoring Queries

```sql
-- Check database size
SELECT 
    schemaname,
    tablename,
    pg_size_pretty(pg_total_relation_size(schemaname||'.'||tablename)) as size
FROM pg_tables 
WHERE schemaname = 'public'
ORDER BY pg_total_relation_size(schemaname||'.'||tablename) DESC;

-- Check slow queries
SELECT query, mean_time, calls, total_time
FROM pg_stat_statements
ORDER BY mean_time DESC
LIMIT 10;
```

This database schema provides a solid foundation for the invoice management system with proper relationships, constraints, and performance optimizations.
