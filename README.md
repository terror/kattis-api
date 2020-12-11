## Kattis API

[![build](https://travis-ci.com/terror/kattis-api.svg?token=ecmzsnHcAnyWvGJ3zTwV&branch=master)](https://travis-ci.com/terror/kattis-api)
[![code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A python wrapper for the [Kattis](https://open.kattis.com/) API.

## Usage

You can simply install the package using pip

```bash
$ pip install kattis
```

## Getting Started
import the kattis module
```python
import kattis
```

## Examples

Some examples to get started.

### Authentication

You can authenticate a Kattis user by calling `kattis.auth`, this will
return a KattisUser object with a few callable methods.

```python
user = kattis.auth('username', 'password')
```

### User Methods

Methods that are callable on a KattisUser object.

`user.problems(pages) -> dict`: Fetches solved user problems  
`user.submissions(pages) -> dict`: Fetches user submissions  
`user.stats() -> dict`: Fetches relevant user statistics  
`user.data() -> dict`: Combines problems, submissions and statistics  

```python
user = kattis.auth('username', 'password')

problems = user.problems(1)
sub = user.submissions(1)
stats = user.stats()
all_info = user.data()
```

### Problems

You can fetch kattis problems by ID or by full pages

`kattis.problem(id) -> dict`: Fetches problem information for a single problem  
`kattis.problems(pages) -> list[dict]` Fetches problem information across specified pages


```python
problem = kattis.problem('2048') # Fetches information for problem with ID '2048'
problems = kattis.problems(2) # Fetches all problems on first 2 pages
```
