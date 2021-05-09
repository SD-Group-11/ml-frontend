from django.test import SimpleTestCase
from django.urls import reverse, resolve
from users.views import registration_view, login_view, forgot_password_view

class TestUrls(SimpleTestCase):
    # These tests make sure that each Url call resolves to the correct view. e.g requesting /users/register brings one to the registrtion_view
    def test_register_url_resolves(self):
        url = reverse('users:register')
        self.assertEquals(resolve(url).func, registration_view)
    def test_login_url_resolves(self):
        url = reverse('users:login')
        self.assertEquals(resolve(url).func, login_view)
    def test_forgot_password_url_resolves(self):
        url = reverse('users:forgot_password')
        self.assertEquals(resolve(url).func, forgot_password_view)
   