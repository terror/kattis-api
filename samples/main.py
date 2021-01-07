import kattis
import json
import os
from dotenv import load_dotenv
load_dotenv()

pids = ['2048', 'abc', 'election']
username, password = os.getenv('username'), os.getenv('password')


def main():
    # A few problems
    print('[~] Fetching problem information...')
    for pid in pids:
        try:
            with open('problems/{}.json'.format(pid), 'w+') as pfile:
                pfile.write(json.dumps(kattis.problem(pid), indent=4))
            print('Problem: {} data fetched successfully'.format(pid))
        except Exception as error:
            print(
                'Error fetching problem information for problem: {} {}'.format(
                    pid, error)
            )

    # First page of problems
    print('[~] Fetching first page of problems')
    try:
        with open('problems/page1.json', 'w+') as pfile:
            pfile.write(json.dumps(kattis.problems(1), indent=4))
    except Exception as error:
        print('Error fetching first page of problems: {}'.format(error))

    # User information
    print('[~] Fetching user information...')
    try:
        user = kattis.auth(username, password)
    except Exception as error:
        print(error)

    with open('user/stats.json', 'w+') as ufile:
        try:
            ufile.write(json.dumps(user.stats(), indent=4))
            print('Stats fetched successfully!')
        except Exception as error:
            print('Error fetching stats: {}'.format(error))


if __name__ == '__main__':
    main()
