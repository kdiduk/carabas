# Carabas -- Online Judge Platform

Carabas is a lightweight online judge system for practicing programming problems.
It supports file-based submissions, containerized code execution, and minimal front-end via server-side rendering.

## Building and running from source

### Requirements

* Python 3.13
* [Poetry](https://python-poetry.org/)

### Installing dependencies 

```commandline
poetry install
```

### Launching the development server

```commandline
poetry run uvicorn app.main:app --reload
```

The server will be available at http://localhost:8000
