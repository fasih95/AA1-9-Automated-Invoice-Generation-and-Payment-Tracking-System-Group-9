"""
Views for clients app.
"""
from rest_framework import generics, status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Client, ClientContact
from .serializers import (
    ClientSerializer, ClientListSerializer, ClientContactSerializer,
    ClientCreateContactSerializer
)


class ClientListCreateView(generics.ListCreateAPIView):
    """List all clients or create a new client."""
    
    queryset = Client.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['client_type', 'is_active', 'country', 'currency']
    search_fields = ['name', 'email', 'client_code', 'city']
    ordering_fields = ['name', 'created_at', 'client_code']
    ordering = ['-created_at']
    
    def get_serializer_class(self):
        """Return appropriate serializer based on action."""
        if self.request.method == 'POST':
            return ClientSerializer
        return ClientListSerializer


class ClientDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update, or delete a client."""
    
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_destroy(self, instance):
        """Soft delete by marking as inactive instead of hard delete."""
        instance.is_active = False
        instance.save()


class ClientContactListCreateView(generics.ListCreateAPIView):
    """List contacts for a client or create a new contact."""
    
    serializer_class = ClientContactSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        """Filter contacts by client."""
        client_pk = self.kwargs['client_pk']
        return ClientContact.objects.filter(client_id=client_pk)
    
    def get_serializer_class(self):
        """Return appropriate serializer based on action."""
        if self.request.method == 'POST':
            return ClientCreateContactSerializer
        return ClientContactSerializer


class ClientContactDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update, or delete a client contact."""
    
    serializer_class = ClientContactSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        """Filter contacts by client."""
        client_pk = self.kwargs['client_pk']
        return ClientContact.objects.filter(client_id=client_pk)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def client_stats_view(request, pk):
    """Get statistics for a specific client."""
    try:
        client = Client.objects.get(pk=pk)
    except Client.DoesNotExist:
        return Response(
            {'error': 'Client not found'}, 
            status=status.HTTP_404_NOT_FOUND
        )
    
    # Calculate statistics (will be more detailed when invoices app is complete)
    stats = {
        'total_contacts': client.contacts.count(),
        'primary_contacts': client.contacts.filter(is_primary=True).count(),
        'billing_contacts': client.contacts.filter(is_billing_contact=True).count(),
        'total_invoices': 0,  # Will be updated when invoices app is ready
        'total_amount': 0.00,  # Will be updated when invoices app is ready
        'paid_amount': 0.00,  # Will be updated when invoices app is ready
        'outstanding_amount': 0.00,  # Will be updated when invoices app is ready
    }
    
    return Response(stats, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def activate_client_view(request, pk):
    """Activate a client."""
    try:
        client = Client.objects.get(pk=pk)
        client.is_active = True
        client.save()
        return Response(
            {'message': 'Client activated successfully'}, 
            status=status.HTTP_200_OK
        )
    except Client.DoesNotExist:
        return Response(
            {'error': 'Client not found'}, 
            status=status.HTTP_404_NOT_FOUND
        )


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def deactivate_client_view(request, pk):
    """Deactivate a client."""
    try:
        client = Client.objects.get(pk=pk)
        client.is_active = False
        client.save()
        return Response(
            {'message': 'Client deactivated successfully'}, 
            status=status.HTTP_200_OK
        )
    except Client.DoesNotExist:
        return Response(
            {'error': 'Client not found'}, 
            status=status.HTTP_404_NOT_FOUND
        )
