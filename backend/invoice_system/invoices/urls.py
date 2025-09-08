"""
URL configuration for invoices app.
"""
from django.urls import path
from . import views

app_name = 'invoices'

urlpatterns = [
    # Invoice management endpoints will be added here
    path('', views.InvoiceListCreateView.as_view(), name='invoice-list'),
    path('<int:pk>/', views.InvoiceDetailView.as_view(), name='invoice-detail'),
    # More URLs will be added as the app develops
]
