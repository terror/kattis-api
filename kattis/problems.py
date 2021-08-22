import requests
import re
import json
from .utils import Utils

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

  problem_page = Utils.html_page(requests.get(obj["url"]))
  stats_page = Utils.html_page(requests.get(obj["stats_url"]))

  add_problem_information(problem_page, obj)
  add_problem_statistics(stats_page, obj)

  return obj

def add_problem_information(problem_page, problem: dict) -> None:
  """
    Parses problem information and adds it
    to problem object

    """
  fields = ["time_limit", "memory_limit", "difficulty"]

  info = problem_page.find("div", {"class": "sidebar-info"}).findAll("p", recursive=True)[1:-1]

  for i in range(len(info)):
    s = re.compile(r"[^\d.]+")
    info[i] = s.sub("", str(info[i]))

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

  stats = stats_page.find("div", {"class": "stats-content"}).findAll("li", recursive=True)[:6]

  for i in range(len(stats)):
    s = re.compile(r"[^\d.]+")
    stats[i] = s.sub("", str(stats[i]))

  problem["stats"] = {fields[i]: stats[i] for i in range(min(len(stats), len(fields)))}

def problem_list(page):
  """
    Returns a list of problem ID's scraped from a
    Kattis problem page

    :param page: problem page
    """
  problems = page.findAll("a", recursive=True)[18:-4]
  return [str(problems[i]).split("/")[2].split('"')[0] for i in range(0, len(problems), 3)]
