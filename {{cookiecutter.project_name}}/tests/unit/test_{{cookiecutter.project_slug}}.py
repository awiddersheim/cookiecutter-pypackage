from {{ cookiecutter.project_slug }}.cli import cli


def test_{{ cookiecutter.project_slug }}(cli_invoke):
    result = cli_invoke(cli)
    assert result.exit_code == 0
    assert result.output == 'hello world\n'


def test_{{ cookiecutter.project_slug }}_usage(cli_invoke):
    result = cli_invoke(cli, ['--help'])
    assert result.exit_code == 0
    assert 'Usage:' in result.output
