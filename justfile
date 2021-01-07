clean:
  rm -rf ./dist && \
  rm -rf ./kattis.egg-info

build:
  python3 setup.py sdist
