from kattis import problem


def test_problem():
    ids = ['jobexpenses', 'abc', '2048']
    for problem_id in ids:
        p = problem(problem_id)
        assert p['id']
        assert p['url']
        assert p['stats_url']
        assert len(p['info']) == 3
        assert len(p['stats']) == 6
