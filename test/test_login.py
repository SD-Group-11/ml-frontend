from io import StringIO
import pytest
import login

tAdmin=StringIO("admi")
tPass=StringIO("password")

def test_enterUsername(monkeypatch):
    monkeypatch.setattr('sys.stdin', tAdmin)
    assert login.enterUsername()=="admin"

def test_enterPassword(monkeypatch):
    monkeypatch.setattr('sys.stdin', tPass)
    assert login.enterPassword()=="password"
