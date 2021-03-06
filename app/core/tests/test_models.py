from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successfull(self):
        # Test creating a new user with an email is successfull
        email = 'huyvo2581999@gmail.com'
        password = 'huy12345678'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        # Test the email for a new user is normalized"
        email = 'test@GMAIL.COM'
        user = get_user_model().objects.create_user(email, '12321')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        # Test creating user with no email raises error
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        email = 'huyvo2581999@gmail.com'
        password = 'sfsa'
        user = get_user_model().objects.create_superuser(email, password)

        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
