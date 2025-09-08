"""
Admin configuration for users app.
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import User, UserProfile


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """Admin configuration for User model."""
    
    list_display = ['email', 'username', 'first_name', 'last_name', 'role', 'is_active', 'created_at']
    list_filter = ['role', 'is_active', 'is_staff', 'created_at']
    search_fields = ['email', 'username', 'first_name', 'last_name', 'company']
    ordering = ['-created_at']
    
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'phone_number')}),
        (_('Company info'), {'fields': ('company', 'address')}),
        (_('Permissions'), {
            'fields': ('role', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'first_name', 'last_name', 'role', 'password1', 'password2'),
        }),
    )


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """Admin configuration for UserProfile model."""
    
    list_display = ['user', 'timezone', 'language', 'receive_email_notifications', 'created_at']
    list_filter = ['timezone', 'language', 'receive_email_notifications', 'receive_sms_notifications']
    search_fields = ['user__email', 'user__username', 'user__first_name', 'user__last_name']
    ordering = ['-created_at']
    
    fieldsets = (
        (_('Profile Info'), {'fields': ('user', 'avatar', 'bio', 'website')}),
        (_('Preferences'), {'fields': ('timezone', 'language')}),
        (_('Notifications'), {'fields': ('receive_email_notifications', 'receive_sms_notifications')}),
    )
