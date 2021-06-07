from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.test.utils import override_settings
from djet import assertions
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from .common import create_user

from djoser.conf import settings as default_settings

import djoser.utils
import djoser.views


class PasswordResetConfirmViewTest(
    APITestCase, assertions.EmailAssertionsMixin, assertions.StatusCodeAssertionsMixin
):
    def setUp(self):
        self.base_url = reverse("user-reset-password-confirm")

    
    def test_post_set_new_password_email_confirm(self):
        user = create_user()
        data = {
            "uid": djoser.utils.encode_uid(user.pk),
            "token": default_token_generator.make_token(user),
            "new_password": "6ecret@$123",
            "re_new_password": "6ecret@$123",
        }

        response = self.client.post(self.base_url, data)

        self.assert_status_equal(response, status.HTTP_204_NO_CONTENT)
        user.refresh_from_db()
        self.assertTrue(user.check_password(data["new_password"]))
        self.assert_emails_in_mailbox(1)
        self.assert_email_exists(to=[user.email])

    def test_post_not_set_new_password_if_broken_uid(self):
        user = create_user()
        data = {
            "uid": "x",
            "token": default_token_generator.make_token(user),
            "new_password": "6ecret@$123",
            "re_new_password": "6ecret@$123",
        }

        response = self.client.post(self.base_url, data)

        self.assert_status_equal(response, status.HTTP_400_BAD_REQUEST)
        self.assertIn("uid", response.data)
        user.refresh_from_db()
        self.assertFalse(user.check_password(data["new_password"]))


    def test_post_not_set_new_password_if_user_does_not_exist(self):
        user = create_user()
        data = {
            "uid": djoser.utils.encode_uid(user.pk + 1),
            "token": default_token_generator.make_token(user),
            "new_password": "6ecret@$123",
            "re_new_password": "6ecret@$123",
        }

        response = self.client.post(self.base_url, data)

        self.assert_status_equal(response, status.HTTP_400_BAD_REQUEST)
        self.assertIn("uid", response.data)
        user.refresh_from_db()
        self.assertFalse(user.check_password(data["new_password"]))



    def test_post_not_set_new_password_if_wrong_token(self):
        user = create_user()
        data = {
            "uid": djoser.utils.encode_uid(user.pk),
            "token": "wrong-token",
            "new_password": "6ecret@$123",
            "re_new_password": "6ecret@$123",
        }

        response = self.client.post(self.base_url, data)

        self.assert_status_equal(response, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data["token"],
            [default_settings.CONSTANTS.messages.INVALID_TOKEN_ERROR],
        )
        user.refresh_from_db()
        self.assertFalse(user.check_password(data["new_password"]))


    def test_post_not_set_new_password_if_password_mismatch(self):
        user = create_user()
        data = {
            "uid": djoser.utils.encode_uid(user.pk),
            "token": default_token_generator.make_token(user),
            "new_password": "6ecret@$123",
            "re_new_password": "wrong",
        }

        response = self.client.post(self.base_url, data)

        self.assert_status_equal(response, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data["non_field_errors"],
            [default_settings.CONSTANTS.messages.PASSWORD_MISMATCH_ERROR],
        )


    def test_post_not_set_new_password_if_mismatch(self):
        user = create_user()
        data = {
            "uid": djoser.utils.encode_uid(user.pk),
            "token": default_token_generator.make_token(user),
            "new_password": "6ecret@$123",
            "re_new_password": "wrong",
        }

        response = self.client.post(self.base_url, data)

        self.assert_status_equal(response, status.HTTP_400_BAD_REQUEST)
        user.refresh_from_db()
        self.assertFalse(user.check_password(data["new_password"]))


    def test_post_not_reset_if_fails_password_validation(self):
        user = create_user()
        data = {
            "uid": djoser.utils.encode_uid(user.pk),
            "token": default_token_generator.make_token(user),
            "new_password": "666",
            "re_new_password": "666",
        }

        response = self.client.post(self.base_url, data)
        self.assert_status_equal(response, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            str(response.data["new_password"][0]), "This password is too short. It must contain at least 8 characters."
        )

    