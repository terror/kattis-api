ci: fmt test

fmt:
  yapf --in-place --recursive **/*.py

test:
  pytest

run *args:
  python3 placeholder {{args}}

install *pkg:
  pipenv install {{pkg}} --skip-lock

build:
  python3 setup.py sdist && python3 setup.py build

clean:
  rm -rf dist build kattis-api.egg-info

publish:
  twine upload dist/*

lock:
  pipenv lock --pre

install-editable:
  pipenv install -e .
