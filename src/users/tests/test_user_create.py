from django.conf import settings
from django.contrib.auth import get_user_model
from django.test.utils import override_settings
from djet import assertions
from pkg_resources import parse_version
from rest_framework import __version__ as drf_version
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from users.models import User
from .common import create_user, mock, perform_create_mock

from djoser.conf import settings as default_settings

User = get_user_model()

class UserCreateViewTest(
    APITestCase,
    assertions.StatusCodeAssertionsMixin,
    assertions.EmailAssertionsMixin,
    assertions.InstanceAssertionsMixin,
):
    def setUp(self):
        self.base_url = reverse("user-list") 


    @mock.patch("users.serializers.UserSerializer", User)
    @mock.patch("users.serializers.UserCreateSerializer.Meta.model", User)
    @mock.patch(
        "users.serializers.UserCreateSerializer.Meta.fields",
        tuple(User.REQUIRED_FIELDS)
        + (User.USERNAME_FIELD, User._meta.pk.name, "password"),
    )
    @mock.patch("djoser.views.User", User)

    def test_user_create_with_retype_password(self):
        data = {"first_name": "Johnny","last_name":"Test","username": "jt", "password": "secret", "re_password": "secret", "email": "john@test.com"}
        response = self.client.post(self.base_url, data)

        self.assert_status_equal(response, status.HTTP_201_CREATED)
        self.assertTrue("password" not in response.data)
        self.assert_instance_exists(User, email=data["email"])
        user = User.objects.get(email=data["email"])
        self.assertTrue(user.check_password(data["password"]))



    def test_post_not_create_new_user_if_email_exists(self):
        create_user(email="john@test.com")
        data = {"first_name": "Johnny","last_name":"Test","username": "jt", "password": "secret","re_password": "secret", "email": "john@test.com"}
        response = self.client.post(self.base_url, data)
        self.assert_status_equal(response, status.HTTP_400_BAD_REQUEST)

    def test_post_not_register_if_fails_password_validation(self):
        data = {"first_name": "Johnny","last_name":"Test","username": "jt", "password": "666","re_password": "666", "email": "john@test.com"}
        response = self.client.post(self.base_url, data)
        self.assert_status_equal(response, status.HTTP_400_BAD_REQUEST)
        response.render()
        self.assertEqual(
            str(response.data["password"][0]), "Password 666 is not allowed."
        )
        if parse_version(drf_version) >= parse_version("3.9.0"):
            self.assertEqual(response.data["password"][0].code, "no666")


    def test_post_not_register_if_password_mismatch(self):
        data = {"first_name": "Johnny","last_name":"Test","username": "jt", "password": "secret","re_password": "lies", "email": "john@test.com"}

        response = self.client.post(self.base_url, data)

        self.assert_status_equal(response, status.HTTP_400_BAD_REQUEST)
        response.render()
        self.assertEqual(
            str(response.data["non_field_errors"][0]),
            default_settings.CONSTANTS.messages.PASSWORD_MISMATCH_ERROR,
        )

    @mock.patch(
        "users.serializers.UserCreateSerializer.perform_create",
        side_effect=perform_create_mock,
    )
    def test_post_return_400_for_integrity_error(self, perform_create):
        data = {"first_name": "Johnny","last_name":"Test","username": "jt", "password": "secret","re_password": "secret", "email": "john@test.com"}
        response = self.client.post(self.base_url, data)

        self.assert_status_equal(response, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data,
            [default_settings.CONSTANTS.messages.CANNOT_CREATE_USER_ERROR],
        )
    

    @mock.patch("users.serializers.UserSerializer", User)
    @mock.patch("users.serializers.UserCreateSerializer.Meta.model", User)
    @mock.patch(
        "users.serializers.UserCreateSerializer.Meta.fields",
        tuple(User.REQUIRED_FIELDS)
        + (User.USERNAME_FIELD, User._meta.pk.name, "password"),
    )
    @mock.patch("djoser.views.User", User)
    def test_post_not_create_user_with_missing_required_fields(self):
        data = {"custom_username": "john", "password": "secret"}
        response = self.client.post(self.base_url, data)

        self.assert_status_equal(response, status.HTTP_400_BAD_REQUEST)
        response.render()
        self.assertEqual(response.data["custom_required_field"][0].code, "required")


    @mock.patch("users.serializers.UserSerializer", User)
    @mock.patch("users.serializers.UserCreateSerializer.Meta.model", User)
    @mock.patch(
        "users.serializers.UserCreateSerializer.Meta.fields",
        tuple(User.REQUIRED_FIELDS)
        + (User.USERNAME_FIELD, User._meta.pk.name, "password"),
    )
    @mock.patch("djoser.views.User", User)
    def test_post_create_user_missing_required_fields(self):
        data = {"password": "secret"}
        response = self.client.post(self.base_url, data)

        self.assert_status_equal(response, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["email"][0].code, "required")

   