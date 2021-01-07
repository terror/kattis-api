import requests
import re
from .utils import Utils
from .problems import problem


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
        obj, data, count = {}, {"script": "true"}, 0

        for page in range(pages):
            problem_page = Utils.html_page(
                requests.get(
                    self.__problem_url + "&page={}".format(page),
                    data=data,
                    cookies=self.__cookies,
                )
            )

            problem_list = problem_page.find_all(
                "td", {"class", "name_column"})

            for prob in problem_list:
                children = prob.findChildren("a", recursive=False, href=True)
                problem_id = children[0]["href"].split("/")[2]
                obj[problem_id] = problem(problem_id)
                count += 1

        obj["count"] = count
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
        user_stats = stats_page.find("ul", {"class": "profile-header-list"}).findAll(
            "li"
        )

        for i in range(len(user_stats)):
            s = re.compile(r"[^\d.]+")
            user_stats[i] = s.sub("", str(user_stats[i]))

        return {
            fields[i]: user_stats[i] for i in range(min(len(user_stats), len(fields)))
        }

    def data(self) -> dict:
        """
        Combined solved problems and user stats

        """
        pages = 28
        return {
            "username": self.__username,
            "stats": self.stats(),
            "problems": self.problems(pages)
        }
