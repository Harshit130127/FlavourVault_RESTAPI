"""
Test cases for core models."""

from django.test import TestCase
from django.contrib.auth import get_user_model # get the fake user model

class ModelsTestCase(TestCase):
    """Test cases for core models."""

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful."""
        email='test@example.com'
        password='Testpassword@123'
        user=get_user_model().objects.create_user(
            email=email,password=password,
            )

        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))