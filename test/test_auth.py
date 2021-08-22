import pytest
import os
from dotenv import load_dotenv
from kattis import auth

load_dotenv()

def test_auth():
  username, password = os.getenv('username'), os.getenv('password')
  try:
    auth(username, password)
  except Exception as Error:
    pytest.fail('Auth Error: {}'.format(Error))

def test_auth_exception():
  with pytest.raises(Exception):
    assert auth('god', '1234')
