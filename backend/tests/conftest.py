"""
Test configuration and fixtures.
"""
import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


@pytest.fixture
def api_client():
    """Provide API client for testing."""
    return APIClient()


@pytest.fixture
def user():
    """Create a test user."""
    return User.objects.create_user(
        username='testuser',
        email='test@example.com',
        password='testpass123',
        first_name='Test',
        last_name='User'
    )


@pytest.fixture
def admin_user():
    """Create an admin user."""
    return User.objects.create_user(
        username='admin',
        email='admin@example.com',
        password='adminpass123',
        first_name='Admin',
        last_name='User',
        role=User.Role.ADMIN,
        is_staff=True
    )


@pytest.fixture
def authenticated_client(api_client, user):
    """Provide authenticated API client."""
    refresh = RefreshToken.for_user(user)
    access_token = refresh.access_token
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
    return api_client


@pytest.fixture
def admin_client(api_client, admin_user):
    """Provide admin authenticated API client."""
    refresh = RefreshToken.for_user(admin_user)
    access_token = refresh.access_token
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
    return api_client
