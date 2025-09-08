"""
Models for invoices app.
"""
from django.db import models
from django.utils.translation import gettext_lazy as _
from core.utils import generate_invoice_number, StatusChoices, validate_positive_amount


class Invoice(models.Model):
    """Invoice model for managing invoices."""
    
    # Basic Information
    invoice_number = models.CharField(
        max_length=50,
        unique=True,
        default=generate_invoice_number,
        help_text=_('Unique invoice number')
    )
    client = models.ForeignKey(
        'clients.Client',
        on_delete=models.CASCADE,
        related_name='invoices',
        help_text=_('Client for this invoice')
    )
    
    # Status and Dates
    status = models.CharField(
        max_length=20,
        choices=StatusChoices.INVOICE_CHOICES,
        default=StatusChoices.DRAFT,
        help_text=_('Invoice status')
    )
    issue_date = models.DateField(
        help_text=_('Date when invoice was issued')
    )
    due_date = models.DateField(
        help_text=_('Payment due date')
    )
    
    # Financial Information
    subtotal = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0.00,
        validators=[validate_positive_amount],
        help_text=_('Subtotal amount before taxes')
    )
    tax_rate = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0.00,
        help_text=_('Tax rate percentage')
    )
    tax_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0.00,
        help_text=_('Tax amount')
    )
    total_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0.00,
        validators=[validate_positive_amount],
        help_text=_('Total invoice amount')
    )
    
    # Additional Information
    notes = models.TextField(
        blank=True,
        null=True,
        help_text=_('Additional notes for the invoice')
    )
    terms_and_conditions = models.TextField(
        blank=True,
        null=True,
        help_text=_('Terms and conditions')
    )
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        'users.User',
        on_delete=models.SET_NULL,
        null=True,
        related_name='created_invoices',
        help_text=_('User who created this invoice')
    )
    
    class Meta:
        verbose_name = _('Invoice')
        verbose_name_plural = _('Invoices')
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['invoice_number']),
            models.Index(fields=['status']),
            models.Index(fields=['due_date']),
        ]
    
    def __str__(self):
        return f"Invoice {self.invoice_number} - {self.client.name}"


# Placeholder views for now
class InvoiceListCreateView:
    pass

class InvoiceDetailView:
    pass
