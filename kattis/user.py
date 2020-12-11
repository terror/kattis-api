import requests
import re
from .utils import Utils


class KattisUser:
    """
    An authenticated Kattis User

    :param username: kattis username
    :param password: kattis password
    :param cookies: user login cookies
    """

    def __init__(self, username, password, cookies):
        self.__username = username
        self.__password = password
        self.__cookies = cookies
        self.__submission_url = "https://open.kattis.com/users/"
        self.__problem_url = "https://open.kattis.com/problems?show_solved=on&show_tried=off&show_untried=off"

    def problems(self, pages=1) -> dict:
        """
        Gets a users solved problems.

        """
        obj, data = {}, {"script": "true"}

        problem_page = Utils.html_page(
            requests.get(self.__problem_url, data=data, cookies=self.__cookies)
        )

        return obj

    def submissions(self, pages=1) -> dict:
        """
        Gets a users problem submissions

        :param pages: submission pages, defaults to 10
        """
        obj, data = [], {"script": "true"}

        for page in range(pages):
            submissions_page = Utils.html_page(
                requests.get(
                    self.__submission_url + "?page={}".format(page),
                    data=data,
                    cookies=self.__cookies,
                )
            )
            ids = submissions_page.find_all("td", {"class": "submission_id"})
            dates = submissions_page.find_all("td", {"data-type": "time"})
            problems = submissions_page.find_all("td", {"id": "problem_title"})
            verdicts = submissions_page.find_all("td", {"data-type": "status"})
            times = submissions_page.find_all("td", {"data-type": "cpu"})
            langs = submissions_page.find_all("td", {"data-type": "lang"})

            for i in range(len(ids)):
                print(langs[i])

        return obj

    def stats(self) -> dict:
        """
        Gets a users stats (score, rank)

        """
        fields, data = ["score", "rank"], {"script": "true"}

        stats_page = Utils.html_page(
            requests.get(
                self.__submission_url + self.__username,
                data=data,
                cookies=self.__cookies,
            )
        )

        # Parse score and rank
        user_stats = stats_page.find(
            "ul", {"class": "profile-header-list"}
        ).findAll("li")

        for i in range(len(user_stats)):
            s = re.compile(r"[^\d.]+")
            user_stats[i] = s.sub("", str(user_stats[i]))

        return {
            fields[i]: user_stats[i]
            for i in range(min(len(user_stats), len(fields)))
        }

    def data(self) -> dict:
        """
        Combines solved problems, submissions and user statistics

        """
        return {
            "stats": self.stats(),
            "submissions": self.submissions(),
            "problems": self.problems(),
        }
