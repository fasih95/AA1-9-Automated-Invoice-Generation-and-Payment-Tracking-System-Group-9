"""
Core utilities and shared functions for the invoice system.
"""
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import datetime, timedelta
import uuid
import os


def generate_invoice_number():
    """Generate a unique invoice number."""
    timestamp = timezone.now().strftime('%Y%m%d')
    random_part = str(uuid.uuid4().hex)[:8].upper()
    return f"INV-{timestamp}-{random_part}"


def generate_file_path(instance, filename):
    """Generate a unique file path for uploads."""
    ext = filename.split('.')[-1]
    filename = f"{uuid.uuid4().hex}.{ext}"
    return os.path.join('uploads', instance.__class__.__name__.lower(), filename)


def validate_positive_amount(value):
    """Validate that an amount is positive."""
    if value <= 0:
        raise ValidationError('Amount must be positive.')


def calculate_due_date(created_date, payment_terms_days=30):
    """Calculate due date based on payment terms."""
    return created_date + timedelta(days=payment_terms_days)


class StatusChoices:
    """Common status choices for various models."""
    DRAFT = 'draft'
    PENDING = 'pending'
    SENT = 'sent'
    PAID = 'paid'
    OVERDUE = 'overdue'
    CANCELLED = 'cancelled'
    
    INVOICE_CHOICES = [
        (DRAFT, 'Draft'),
        (SENT, 'Sent'),
        (PAID, 'Paid'),
        (OVERDUE, 'Overdue'),
        (CANCELLED, 'Cancelled'),
    ]
    
    PAYMENT_CHOICES = [
        (PENDING, 'Pending'),
        (PAID, 'Paid'),
        (CANCELLED, 'Cancelled'),
    ]


class PriorityChoices:
    """Priority levels for various models."""
    LOW = 'low'
    MEDIUM = 'medium'
    HIGH = 'high'
    URGENT = 'urgent'
    
    CHOICES = [
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High'),
        (URGENT, 'Urgent'),
    ]
