# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

[![PyPI version](https://img.shields.io/pypi/v/{{ cookiecutter.project_name }}.svg)](https://pypi.org/project/{{ cookiecutter.project_name }})
[![Python Versions](https://img.shields.io/pypi/pyversions/{{ cookiecutter.project_name }}.svg)](https://pypi.org/project/{{ cookiecutter.project_name }})
[![Build Status](https://img.shields.io/circleci/project/github/{{ cookiecutter.github_user }}/{{ cookiecutter.project_name }}/master.svg)](https://circleci.com/gh/{{ cookiecutter.github_user }}/{{ cookiecutter.project_name }})
[![License](https://img.shields.io/pypi/l/{{ cookiecutter.project_name }}.svg)](https://github.com/awiddersheim/{{ cookiecutter.project_name }}/blob/master/LICENSE)
[![Docker Pulls](https://img.shields.io/docker/pulls/{{ cookiecutter.github_user }}/{{ cookiecutter.project_name }}.svg)](https://hub.docker.com/r/{{ cookiecutter.github_user }}/{{ cookiecutter.project_name }})

## Installation

```
$ pip install {{ cookiecutter.project_name }}
```

## Running

```
$ python -m {{ cookiecutter.project_slug }} --help
$ {{ cookiecutter.project_name }} --help
```

## Docker

### DockerHub

```
$ docker run \
    --rm \
    --tty \
    --interactive \
    {{ cookiecutter.github_user }}/{{ cookiecutter.project_name }} --help
```

### Building Locally

```
$ docker build --tag {{ cookiecutter.project_name }} --target prod .
```

## Development

```
$ pip install --editable .
$ {{ cookiecutter.project_name }} --help
```

## Testing

```
# Install development packages (preferably in a virtualenv)
$ pip install --editable .[dev]

# Run tests
$ pytest

# Run tests for available Python interpreters
$ tox

# Linting
$ tox -e flake8
```
