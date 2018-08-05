import click


@click.command()
@click.version_option()
def cli():
    """Basic command line interface."""

    click.echo('hello world')


def main():  # pragma: no cover
    cli(
        auto_envvar_prefix='{{ cookiecutter.project_slug.upper() }}',
        prog_name='{{ cookiecutter.project_slug }}',
    )
