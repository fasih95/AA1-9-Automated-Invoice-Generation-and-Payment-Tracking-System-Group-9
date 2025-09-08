"""
Views for payments app.
"""
from rest_framework import generics, permissions

# Placeholder views - will be implemented in detail later
class PaymentListCreateView(generics.ListCreateAPIView):
    """List all payments or create a new payment."""
    permission_classes = [permissions.IsAuthenticated]
    pass

class PaymentDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update, or delete a payment."""
    permission_classes = [permissions.IsAuthenticated]
    pass
