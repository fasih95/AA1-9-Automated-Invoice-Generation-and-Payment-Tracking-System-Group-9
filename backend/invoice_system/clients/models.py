"""
Models for clients app.
"""
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import EmailValidator, RegexValidator
from core.utils import generate_file_path


class Client(models.Model):
    """Client model for managing customer information."""
    
    class ClientType(models.TextChoices):
        INDIVIDUAL = 'individual', _('Individual')
        COMPANY = 'company', _('Company')
    
    # Basic Information
    name = models.CharField(
        max_length=200,
        help_text=_('Client name or company name')
    )
    client_type = models.CharField(
        max_length=20,
        choices=ClientType.choices,
        default=ClientType.INDIVIDUAL,
        help_text=_('Type of client')
    )
    client_code = models.CharField(
        max_length=20,
        unique=True,
        help_text=_('Unique client code for identification')
    )
    
    # Contact Information
    email = models.EmailField(
        validators=[EmailValidator()],
        help_text=_('Primary email address')
    )
    phone_number = models.CharField(
        max_length=20,
        validators=[RegexValidator(
            regex=r'^\+?1?\d{9,15}$',
            message=_('Phone number must be entered in the format: "+999999999". Up to 15 digits allowed.')
        )],
        blank=True,
        null=True,
        help_text=_('Primary phone number')
    )
    website = models.URLField(
        blank=True,
        null=True,
        help_text=_('Company website')
    )
    
    # Address Information
    address_line_1 = models.CharField(
        max_length=200,
        help_text=_('Street address')
    )
    address_line_2 = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        help_text=_('Apartment, suite, etc.')
    )
    city = models.CharField(
        max_length=100,
        help_text=_('City')
    )
    state_province = models.CharField(
        max_length=100,
        help_text=_('State or province')
    )
    postal_code = models.CharField(
        max_length=20,
        help_text=_('Postal or ZIP code')
    )
    country = models.CharField(
        max_length=100,
        default='USA',
        help_text=_('Country')
    )
    
    # Business Information
    tax_id = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text=_('Tax ID or VAT number')
    )
    registration_number = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text=_('Business registration number')
    )
    
    # Payment Information
    payment_terms = models.PositiveIntegerField(
        default=30,
        help_text=_('Default payment terms in days')
    )
    credit_limit = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0.00,
        help_text=_('Credit limit for the client')
    )
    currency = models.CharField(
        max_length=3,
        default='USD',
        help_text=_('Preferred currency (ISO code)')
    )
    
    # Status and Metadata
    is_active = models.BooleanField(
        default=True,
        help_text=_('Whether the client is active')
    )
    notes = models.TextField(
        blank=True,
        null=True,
        help_text=_('Additional notes about the client')
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        'users.User',
        on_delete=models.SET_NULL,
        null=True,
        related_name='created_clients',
        help_text=_('User who created this client')
    )
    
    class Meta:
        verbose_name = _('Client')
        verbose_name_plural = _('Clients')
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['client_code']),
            models.Index(fields=['email']),
            models.Index(fields=['is_active']),
        ]
    
    def __str__(self):
        return f"{self.name} ({self.client_code})"
    
    @property
    def full_address(self):
        """Return formatted full address."""
        address_parts = [self.address_line_1]
        if self.address_line_2:
            address_parts.append(self.address_line_2)
        address_parts.extend([
            f"{self.city}, {self.state_province} {self.postal_code}",
            self.country
        ])
        return '\n'.join(address_parts)
    
    def save(self, *args, **kwargs):
        """Override save to generate client code if not provided."""
        if not self.client_code:
            # Generate client code based on name initials and ID
            name_parts = self.name.split()
            initials = ''.join([part[0].upper() for part in name_parts[:2]])
            # Will be updated after save to include ID
            self.client_code = f"{initials}-TMP"
        
        super().save(*args, **kwargs)
        
        # Update client code with actual ID
        if self.client_code.endswith('-TMP'):
            self.client_code = f"{self.client_code[:-4]}-{self.id:04d}"
            super().save(update_fields=['client_code'])


class ClientContact(models.Model):
    """Additional contact persons for a client."""
    
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name='contacts',
        help_text=_('Client this contact belongs to')
    )
    first_name = models.CharField(
        max_length=50,
        help_text=_('Contact first name')
    )
    last_name = models.CharField(
        max_length=50,
        help_text=_('Contact last name')
    )
    title = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text=_('Job title or position')
    )
    email = models.EmailField(
        validators=[EmailValidator()],
        help_text=_('Contact email address')
    )
    phone_number = models.CharField(
        max_length=20,
        validators=[RegexValidator(
            regex=r'^\+?1?\d{9,15}$',
            message=_('Phone number must be entered in the format: "+999999999". Up to 15 digits allowed.')
        )],
        blank=True,
        null=True,
        help_text=_('Contact phone number')
    )
    is_primary = models.BooleanField(
        default=False,
        help_text=_('Whether this is the primary contact')
    )
    is_billing_contact = models.BooleanField(
        default=False,
        help_text=_('Whether this contact receives billing communications')
    )
    notes = models.TextField(
        blank=True,
        null=True,
        help_text=_('Additional notes about this contact')
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _('Client Contact')
        verbose_name_plural = _('Client Contacts')
        ordering = ['-is_primary', 'last_name', 'first_name']
        unique_together = ['client', 'email']
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.client.name})"
    
    @property
    def full_name(self):
        """Return full name."""
        return f"{self.first_name} {self.last_name}"
    
    def save(self, *args, **kwargs):
        """Override save to ensure only one primary contact per client."""
        if self.is_primary:
            # Set all other contacts for this client to non-primary
            ClientContact.objects.filter(
                client=self.client,
                is_primary=True
            ).exclude(pk=self.pk).update(is_primary=False)
        
        super().save(*args, **kwargs)
