"""
URL configuration for clients app.
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'clients'

# Create nested routes for client contacts
urlpatterns = [
    # Client management
    path('', views.ClientListCreateView.as_view(), name='client-list'),
    path('<int:pk>/', views.ClientDetailView.as_view(), name='client-detail'),
    path('<int:pk>/stats/', views.client_stats_view, name='client-stats'),
    path('<int:pk>/activate/', views.activate_client_view, name='client-activate'),
    path('<int:pk>/deactivate/', views.deactivate_client_view, name='client-deactivate'),
    
    # Client contacts
    path('<int:client_pk>/contacts/', views.ClientContactListCreateView.as_view(), name='client-contact-list'),
    path('<int:client_pk>/contacts/<int:pk>/', views.ClientContactDetailView.as_view(), name='client-contact-detail'),
]
