"""
Views for invoices app.
"""
from rest_framework import generics, permissions

# Placeholder views - will be implemented in detail later
class InvoiceListCreateView(generics.ListCreateAPIView):
    """List all invoices or create a new invoice."""
    permission_classes = [permissions.IsAuthenticated]
    pass

class InvoiceDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update, or delete an invoice."""
    permission_classes = [permissions.IsAuthenticated]
    pass
