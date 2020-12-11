import os
from dotenv import load_dotenv
from kattis import auth
load_dotenv()


def test_user_stats():
    username, password = os.getenv('username'), os.getenv('password')
    user = auth(username, password)
    assert len(user.stats().keys()) == 2
