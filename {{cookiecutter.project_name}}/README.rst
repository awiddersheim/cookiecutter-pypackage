{{ cookiecutter.project_name }}
{{ '=' * cookiecutter.project_name | length }}

{{ cookiecutter.description }}

|Status| |PackageVersion| |PythonVersions|

Installation
------------

::

    $ pip install {{ cookiecutter.project_name }}
    $ pip install --upgrade {{ cookiecutter.project_name }}


Running
-------

::

    $ python -m {{ cookiecutter.project_slug }} --help
    $ {{ cookiecutter.project_name }} --help


Development
-----------

::

    $ pip install -e .
    $ {{ cookiecutter.project_name }} --help


Testing
-------

::

    # Install development packages (preferably in a virtualenv)
    $ pip install -e .[dev]

    # Run tests
    $ pytest

    # Run tests for available Python interpreters
    $ tox

    # Linting
    $ tox -e flake8


.. |PackageVersion| image:: https://img.shields.io/pypi/v/{{ cookiecutter.project_name }}.svg?style=flat
    :alt: PyPI version
    :target: https://pypi.org/project/{{ cookiecutter.project_name }}

.. |PythonVersions| image:: https://img.shields.io/pypi/pyversions/{{ cookiecutter.project_name }}.svg
    :alt: Supported Python versions
    :target: https://pypi.org/project/{{ cookiecutter.project_name }}

.. |Status| image:: https://img.shields.io/circleci/project/github/{{ cookiecutter.github_user }}/{{ cookiecutter.project_name }}/master.svg
    :alt: Build
    :target: https://circleci.com/gh/{{ cookiecutter.github_user }}/{{ cookiecutter.project_name }}
