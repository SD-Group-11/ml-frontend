from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse,resolve
from users.views import registration_view,login_view,forgot_password_view

# Create your tests here.
class TestUrls(SimpleTestCase):
    def test_basic(self):
        assert 1 == 1