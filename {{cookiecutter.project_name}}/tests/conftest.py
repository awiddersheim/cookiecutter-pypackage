import pytest

from {{ cookiecutter.project_name }}.cli import ENVVAR_PREFIX


@pytest.fixture
def cli_invoke(cli_runner):
    def func(*args, **kwargs):
        kwargs.setdefault('auto_envvar_prefix', ENVVAR_PREFIX)

        return cli_runner.invoke(*args, **kwargs)

    return func
