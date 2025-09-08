"""
Serializers for clients app.
"""
from rest_framework import serializers
from .models import Client, ClientContact


class ClientContactSerializer(serializers.ModelSerializer):
    """Serializer for client contacts."""
    
    full_name = serializers.CharField(source='full_name', read_only=True)
    
    class Meta:
        model = ClientContact
        fields = [
            'id', 'first_name', 'last_name', 'full_name', 'title',
            'email', 'phone_number', 'is_primary', 'is_billing_contact',
            'notes', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class ClientSerializer(serializers.ModelSerializer):
    """Serializer for client model."""
    
    contacts = ClientContactSerializer(many=True, read_only=True)
    full_address = serializers.CharField(source='full_address', read_only=True)
    
    class Meta:
        model = Client
        fields = [
            'id', 'name', 'client_type', 'client_code', 'email',
            'phone_number', 'website', 'address_line_1', 'address_line_2',
            'city', 'state_province', 'postal_code', 'country',
            'tax_id', 'registration_number', 'payment_terms',
            'credit_limit', 'currency', 'is_active', 'notes',
            'contacts', 'full_address', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'client_code', 'created_at', 'updated_at']
    
    def create(self, validated_data):
        """Create client with current user as creator."""
        validated_data['created_by'] = self.context['request'].user
        return super().create(validated_data)


class ClientListSerializer(serializers.ModelSerializer):
    """Simplified serializer for client lists."""
    
    primary_contact = serializers.SerializerMethodField()
    total_invoices = serializers.SerializerMethodField()
    
    class Meta:
        model = Client
        fields = [
            'id', 'name', 'client_code', 'email', 'phone_number',
            'city', 'country', 'is_active', 'primary_contact',
            'total_invoices', 'created_at'
        ]
    
    def get_primary_contact(self, obj):
        """Get primary contact for the client."""
        primary_contact = obj.contacts.filter(is_primary=True).first()
        if primary_contact:
            return {
                'name': primary_contact.full_name,
                'email': primary_contact.email,
                'phone': primary_contact.phone_number
            }
        return None
    
    def get_total_invoices(self, obj):
        """Get total number of invoices for the client."""
        return obj.invoices.count() if hasattr(obj, 'invoices') else 0


class ClientCreateContactSerializer(serializers.ModelSerializer):
    """Serializer for creating client contacts."""
    
    class Meta:
        model = ClientContact
        fields = [
            'first_name', 'last_name', 'title', 'email',
            'phone_number', 'is_primary', 'is_billing_contact', 'notes'
        ]
    
    def create(self, validated_data):
        """Create contact for specific client."""
        client_id = self.context['view'].kwargs['client_pk']
        client = Client.objects.get(pk=client_id)
        validated_data['client'] = client
        return super().create(validated_data)
