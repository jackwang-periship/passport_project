import re

from django.contrib.auth.models import User
from django.core import mail
from django.test import TestCase
from django.urls import reverse
from passport_project.settings import LOGIN_REDIRECT_URL



class LoginTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('someone', 'someone@example.com', 'password')

    def test_email_login(self):
        response = self.client.post(reverse('account_login'), {'login': self.user.email, 'password': 'password'})
        self.assertRedirects(response, LOGIN_REDIRECT_URL, fetch_redirect_response=False)

    def test_request_password_reset_email(self):
        response = self.client.post(reverse('account_reset_password'), {'email': self.user.email})
        self.assertRedirects(response, reverse('account_reset_password_done'), fetch_redirect_response=False)
        self.assertEqual(len(mail.outbox), 1)
        reset_url_regex = re.compile(r'https?:\/\/.*\/accounts\/password\/reset\/key\/.+\/')
        self.assertTrue(reset_url_regex.search(mail.outbox[0].body))
