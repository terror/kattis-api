import dotenv
import json
import kattis
import os
import sys

def main(pids, data):
  print("[~] Fetching problem information...")

  for pid in pids:
    try:
      with open("problems/{}.json".format(pid), "w+") as file:
        file.write(json.dumps(kattis.problem(pid), indent=2))
      print("Problem: {} data fetched successfully".format(pid))
    except Exception as error:
      print("Error fetching problem information for problem: {} {}".format(pid, error))

  print("[~] Fetching first page of problems")

  try:
    with open("problems/page1.json", "w+") as file:
      file.write(json.dumps(kattis.problems(1), indent=2))
  except Exception as error:
    print("Error fetching first page of problems: {}".format(error))

  print("[~] Fetching user information...")

  try:
    username, password = data
    user = kattis.auth(username, password)
  except Exception as error:
    print(error)
    sys.exit(1)

  with open("user/stats.json", "w+") as file:
    try:
      file.write(json.dumps(user.stats(), indent=2))
      print("Stats fetched successfully!")
    except Exception as error:
      print("Error fetching user stats: {}".format(error))

  with open("user/data.json", "w+") as file:
    try:
      file.write(json.dumps(user.data(), indent=2))
      print("Data fetched successfully!")
    except Exception as error:
      print("Error fetching user data: {}".format(error))

if __name__ == "__main__":
  dotenv.load_dotenv()
  main(["2048", "abc", "election"], (os.getenv("username"), os.getenv("password")))
