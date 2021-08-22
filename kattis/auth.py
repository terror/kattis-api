import requests
from .user import KattisUser

URL = "https://open.kattis.com/login"

class AuthError(Exception):
  pass

def auth(username: str, password: str) -> KattisUser:
  """
    Authenticate kattis user with username and password

    """
  login = {"user": username, "password": password, "script": "true"}

  res = requests.post(URL, data=login)
  if res.status_code == 200:
    return KattisUser(username, password, res.cookies)

  raise AuthError("Invalid user credentials.")
