import requests
import os
from .utils import Utils
from bs4 import BeautifulSoup

CACHE_DIR = os.path.expanduser("~") + "/.cache/kattis/"

class Database:
    def __init__(self):
        if not os.path.exists(CACHE_DIR):
            os.makedirs(CACHE_DIR)
        self.db = set()
        for root, dirs, files in os.walk(CACHE_DIR):
            self.db.update(files)

    def get(self, filename, url):
        filename += ".html"
        if filename in self.db:
            return BeautifulSoup(open(CACHE_DIR + filename, 'r', encoding = 'utf-8').read(), "html.parser")
        else:
            r = requests.get(url)
            open(CACHE_DIR + filename, 'w', encoding = 'utf-8').write(r.text)
            return Utils.html_page(r)
