from django.contrib.auth import get_user_model
from django.db import IntegrityError

from djoser.conf import settings as djoser_settings

from unittest import mock

__all__ = [
    "get_user_model",
    "IntegrityError",
    "mock",
    "RunCheck",
    "PermCheckClass",
    "SerializerCheckClass",
]

Token = djoser_settings.TOKEN_MODEL


def create_user(use_custom_data=False, **kwargs):
    data = (
        {"first_name": "Johnny","last_name":"Test","username": "jt", "password": "5ecret@$123", "email": "john@test.com"}    
        
        if not use_custom_data
        else {
            "first_name": "Johnny",
            "last_name":"Test",
            "username": "jt",
            "password": "5ecret@$123",
            "email": "john@test.com"
        }
    )
    data.update(kwargs)
    user = get_user_model().objects.create_user(**data)
    user.raw_password = data["password"]
    return user


def login_user(client, user):
    token = Token.objects.create(user=user)
    client.credentials(HTTP_AUTHORIZATION="Token " + token.key)


def perform_create_mock(x):
    raise IntegrityError


class RunCheck(Exception):
    pass


class PermCheckClass:
    def has_permission(self, *args, **kwargs):
        raise RunCheck("working")

    def has_object_permission(self, *args, **kwargs):
        raise RunCheck("working")


class SerializerCheckClass:
    def __init__(self, *args, **kwargs):
        raise RunCheck("working")