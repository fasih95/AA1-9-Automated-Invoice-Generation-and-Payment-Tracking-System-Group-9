"""
Models for users app.
"""
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from core.utils import generate_file_path


class User(AbstractUser):
    """Custom user model with additional fields."""
    
    class Role(models.TextChoices):
        ADMIN = 'admin', _('Admin')
        ACCOUNTANT = 'accountant', _('Accountant')
        CLIENT = 'client', _('Client')
        VIEWER = 'viewer', _('Viewer')
    
    # Override email to be required and unique
    email = models.EmailField(_('email address'), unique=True)
    
    # Additional fields
    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.VIEWER,
        help_text=_('User role in the system')
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
    company = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        help_text=_('Company name')
    )
    address = models.TextField(
        blank=True,
        null=True,
        help_text=_('Address')
    )
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Use email as username field
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    
    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.get_full_name()} ({self.email})"
    
    def get_full_name(self):
        """Return the first_name plus the last_name, with a space in between."""
        full_name = f"{self.first_name} {self.last_name}"
        return full_name.strip()
    
    @property
    def is_admin(self):
        """Check if user is admin."""
        return self.role == self.Role.ADMIN or self.is_superuser
    
    @property
    def is_accountant(self):
        """Check if user is accountant."""
        return self.role == self.Role.ACCOUNTANT
    
    @property
    def is_client(self):
        """Check if user is client."""
        return self.role == self.Role.CLIENT
    
    @property
    def can_create_invoices(self):
        """Check if user can create invoices."""
        return self.is_admin or self.is_accountant
    
    @property
    def can_manage_payments(self):
        """Check if user can manage payments."""
        return self.is_admin or self.is_accountant


class UserProfile(models.Model):
    """Extended user profile with additional settings."""
    
    class Language(models.TextChoices):
        ENGLISH = 'en', _('English')
        SPANISH = 'es', _('Spanish')
        FRENCH = 'fr', _('French')
        GERMAN = 'de', _('German')
    
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile',
        help_text=_('User this profile belongs to')
    )
    avatar = models.ImageField(
        upload_to=generate_file_path,
        blank=True,
        null=True,
        help_text=_('User avatar image')
    )
    bio = models.TextField(
        max_length=500,
        blank=True,
        null=True,
        help_text=_('Short bio about the user')
    )
    website = models.URLField(
        blank=True,
        null=True,
        help_text=_('Personal or company website')
    )
    timezone = models.CharField(
        max_length=50,
        default='UTC',
        help_text=_('User timezone')
    )
    language = models.CharField(
        max_length=5,
        choices=Language.choices,
        default=Language.ENGLISH,
        help_text=_('Preferred language')
    )
    receive_email_notifications = models.BooleanField(
        default=True,
        help_text=_('Receive email notifications')
    )
    receive_sms_notifications = models.BooleanField(
        default=False,
        help_text=_('Receive SMS notifications')
    )
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _('User Profile')
        verbose_name_plural = _('User Profiles')
    
    def __str__(self):
        return f"{self.user.get_full_name()}'s Profile"
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """Custom user model with additional fields."""
    
    class Role(models.TextChoices):
        ADMIN = 'admin', _('Admin')
        ACCOUNTANT = 'accountant', _('Accountant')
        CLIENT = 'client', _('Client')
        VIEWER = 'viewer', _('Viewer')
    
    email = models.EmailField(_('email address'), unique=True)
    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.VIEWER,
        help_text=_('User role in the system')
    )
    phone_number = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        help_text=_('Contact phone number')
    )
    company = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text=_('Company name')
    )
    address = models.TextField(
        blank=True,
        null=True,
        help_text=_('Business address')
    )
    is_active = models.BooleanField(
        default=True,
        help_text=_('Designates whether this user should be treated as active.')
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    
    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.get_full_name()} ({self.email})"
    
    def get_full_name(self):
        """Return the first_name plus the last_name, with a space in between."""
        full_name = f"{self.first_name} {self.last_name}"
        return full_name.strip()
    
    @property
    def is_admin(self):
        """Check if user is an admin."""
        return self.role == self.Role.ADMIN
    
    @property
    def is_accountant(self):
        """Check if user is an accountant."""
        return self.role == self.Role.ACCOUNTANT
    
    @property
    def is_client(self):
        """Check if user is a client."""
        return self.role == self.Role.CLIENT


class UserProfile(models.Model):
    """Extended user profile information."""
    
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    avatar = models.ImageField(
        upload_to='avatars/',
        blank=True,
        null=True,
        help_text=_('User profile picture')
    )
    bio = models.TextField(
        blank=True,
        null=True,
        max_length=500,
        help_text=_('Short biography')
    )
    website = models.URLField(
        blank=True,
        null=True,
        help_text=_('Personal or company website')
    )
    timezone = models.CharField(
        max_length=50,
        default='UTC',
        help_text=_('User timezone')
    )
    language = models.CharField(
        max_length=10,
        default='en',
        help_text=_('Preferred language')
    )
    receive_email_notifications = models.BooleanField(
        default=True,
        help_text=_('Receive email notifications')
    )
    receive_sms_notifications = models.BooleanField(
        default=False,
        help_text=_('Receive SMS notifications')
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _('User Profile')
        verbose_name_plural = _('User Profiles')
    
    def __str__(self):
        return f"{self.user.get_full_name()}'s Profile"
