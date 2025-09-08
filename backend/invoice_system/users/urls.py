"""
URL configuration for users app.
"""
from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    # Authentication
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # User management
    path('users/', views.UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetailView.as_view(), name='user-detail'),
    path('profile/', views.CurrentUserView.as_view(), name='current-user'),
    path('profile/edit/', views.UserProfileView.as_view(), name='user-profile'),
    
    # Password management
    path('change-password/', views.change_password_view, name='change-password'),
]
