from kattis import problems


def test_problems():
    p = problems(1)
    assert len(p) == 100
