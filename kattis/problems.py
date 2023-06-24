import requests
import re
from .utils import Utils
from kattis.database import Database

database = Database()
URL = "https://open.kattis.com/problems/"

def problems(pages=1) -> dict:
    """
    Fetches all Kattis problems

    :param pages: number of problem pages, defaults to 1
    :rtype: list of problem objects
    """
    ret = []
    for page in range(pages):
        probs = Utils.html_page(requests.get(URL + "?page={}".format(page)))
        for problem_id in problem_list(probs):
            ret.append(problem(problem_id))
    return ret


def problem(problem_id: str) -> dict:
    """
    Fetches information for a single Kattis problem

    :param problem_id: id of a Kattis problem
    :rtype: json object
    """
    obj = {
        "url": URL + problem_id,
        "stats_url": URL + problem_id + "/statistics",
    }

    problem_page = database.get(problem_id, obj["url"])
    stats_page = database.get(problem_id + "_statistics", obj["stats_url"])

    add_problem_information(problem_page, obj)
    add_problem_statistics(stats_page, obj)

    return obj


def add_problem_information(problem_page, problem: dict) -> None:
    """
    Parses problem information and adds it
    to problem object

    """
    fields = ["time_limit", "memory_limit", "difficulty"]
    info = problem_page.findAll("div", "metadata_list-item")[:3]
    for i in range(len(info)):
        s = info[i].find('span').find_next_sibling().text.strip()
        info[i] = re.sub(r'[a-zA-Z]', '', s).strip()
    problem["info"] = {fields[i]: info[i] for i in range(min(len(info), len(fields)))}

def add_problem_statistics(stats_page, problem: dict) -> None:
    """
    Parses problem statistics and adds it
    to problem object

    """
    fields = [
        "submissions",
        "accepted_submissions",
        "submission_ratio",
        "authors",
        "accepted_authors",
        "author_ratio",
    ]

    stats = stats_page.find("table", class_="table2 condensed mt-5").findAll("tr")

    # Extract the numeric values from each <td> tag
    stats = [re.sub(r'<[^>]+>', '', str(td)).strip('\n%') for tr in stats for td in tr.findAll("td")[1:]]

    problem["stats"] = {
        fields[i]: stats[i] for i in range(min(len(stats), len(fields)))
    }


def problem_list(page):
    """
    Returns a list of problem ID's scraped from a
    Kattis problem page

    :param page: problem page
    """
    problems = page.findAll("a", recursive=True)[18:-4]
    return [
        str(problems[i]).split("/")[2].split('"')[0] for i in range(0, len(problems), 3)
    ]
