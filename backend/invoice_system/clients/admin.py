"""
Admin configuration for clients app.
"""
from django.contrib import admin
from .models import Client, ClientContact


class ClientContactInline(admin.TabularInline):
    """Inline admin for client contacts."""
    model = ClientContact
    extra = 0
    fields = ['first_name', 'last_name', 'title', 'email', 'phone_number', 'is_primary', 'is_billing_contact']


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    """Admin configuration for Client model."""
    
    list_display = [
        'name', 'client_code', 'email', 'client_type', 
        'city', 'country', 'is_active', 'created_at'
    ]
    list_filter = [
        'client_type', 'is_active', 'country', 'currency', 'created_at'
    ]
    search_fields = [
        'name', 'client_code', 'email', 'city', 'tax_id'
    ]
    ordering = ['-created_at']
    readonly_fields = ['client_code', 'created_at', 'updated_at']
    inlines = [ClientContactInline]
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'client_type', 'client_code', 'is_active')
        }),
        ('Contact Information', {
            'fields': ('email', 'phone_number', 'website')
        }),
        ('Address', {
            'fields': (
                'address_line_1', 'address_line_2', 'city',
                'state_province', 'postal_code', 'country'
            )
        }),
        ('Business Information', {
            'fields': ('tax_id', 'registration_number')
        }),
        ('Payment Terms', {
            'fields': ('payment_terms', 'credit_limit', 'currency')
        }),
        ('Additional Information', {
            'fields': ('notes', 'created_by')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def save_model(self, request, obj, form, change):
        """Set created_by field when creating new client."""
        if not change:  # Creating new object
            obj.created_by = request.user
        super().save_model(request, obj, form, change)


@admin.register(ClientContact)
class ClientContactAdmin(admin.ModelAdmin):
    """Admin configuration for ClientContact model."""
    
    list_display = [
        'full_name', 'client', 'email', 'title', 
        'is_primary', 'is_billing_contact', 'created_at'
    ]
    list_filter = [
        'is_primary', 'is_billing_contact', 'created_at',
        'client__client_type', 'client__is_active'
    ]
    search_fields = [
        'first_name', 'last_name', 'email', 'client__name'
    ]
    ordering = ['-created_at']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Contact Information', {
            'fields': ('client', 'first_name', 'last_name', 'title')
        }),
        ('Communication', {
            'fields': ('email', 'phone_number')
        }),
        ('Settings', {
            'fields': ('is_primary', 'is_billing_contact')
        }),
        ('Notes', {
            'fields': ('notes',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
