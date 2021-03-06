from django.contrib.auth import views as auth_views
from django.urls import reverse, resolve
from django.test import TestCase

class PasswordResetCompleteTests(TestCase):
    def setUp(self):
        url = reverse('password_reset_complete')
        self.response = self.client.get(url)

    def test_password_reset_done_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_password_reset_done_view_funtion(self):
        view = resolve('/accounts/reset/complete/')
        self.assertEquals(view.func.view_class, auth_views.PasswordResetCompleteView)
