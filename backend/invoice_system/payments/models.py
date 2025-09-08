"""
Models for payments app.
"""
from django.db import models
from django.utils.translation import gettext_lazy as _
from core.utils import StatusChoices, validate_positive_amount


class Payment(models.Model):
    """Payment model for tracking payments."""
    
    class PaymentMethod(models.TextChoices):
        CASH = 'cash', _('Cash')
        CHECK = 'check', _('Check')
        BANK_TRANSFER = 'bank_transfer', _('Bank Transfer')
        CREDIT_CARD = 'credit_card', _('Credit Card')
        ONLINE = 'online', _('Online Payment')
    
    # Basic Information
    invoice = models.ForeignKey(
        'invoices.Invoice',
        on_delete=models.CASCADE,
        related_name='payments',
        help_text=_('Invoice this payment is for')
    )
    payment_reference = models.CharField(
        max_length=100,
        help_text=_('Payment reference number')
    )
    
    # Payment Details
    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        validators=[validate_positive_amount],
        help_text=_('Payment amount')
    )
    payment_date = models.DateField(
        help_text=_('Date when payment was made')
    )
    payment_method = models.CharField(
        max_length=20,
        choices=PaymentMethod.choices,
        help_text=_('Payment method used')
    )
    status = models.CharField(
        max_length=20,
        choices=StatusChoices.PAYMENT_CHOICES,
        default=StatusChoices.PENDING,
        help_text=_('Payment status')
    )
    
    # Additional Information
    notes = models.TextField(
        blank=True,
        null=True,
        help_text=_('Additional notes about the payment')
    )
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        'users.User',
        on_delete=models.SET_NULL,
        null=True,
        related_name='recorded_payments',
        help_text=_('User who recorded this payment')
    )
    
    class Meta:
        verbose_name = _('Payment')
        verbose_name_plural = _('Payments')
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Payment {self.payment_reference} - {self.amount}"
