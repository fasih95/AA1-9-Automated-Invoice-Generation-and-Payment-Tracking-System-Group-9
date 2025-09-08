"""
Sample tests for users app.
"""
import pytest
from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
class TestUserViews:
    """Test user views."""
    
    def test_user_registration(self, api_client):
        """Test user registration."""
        url = reverse('users:register')
        data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpass123',
            'password_confirm': 'newpass123',
            'first_name': 'New',
            'last_name': 'User'
        }
        response = api_client.post(url, data)
        assert response.status_code == status.HTTP_201_CREATED
    
    def test_user_login(self, api_client, user):
        """Test user login."""
        url = reverse('users:login')
        data = {
            'email': user.email,
            'password': 'testpass123'
        }
        response = api_client.post(url, data)
        assert response.status_code == status.HTTP_200_OK
        assert 'tokens' in response.data
    
    def test_current_user_profile(self, authenticated_client, user):
        """Test getting current user profile."""
        url = reverse('users:current-user')
        response = authenticated_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['email'] == user.email
