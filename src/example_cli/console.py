import textwrap

import click

from . import __version__, cat_fact_model


@click.command()
@click.version_option(version=__version__)
def main():
    """The entrypoint for the application"""

    click.secho("Cat fact of the day:", fg="blue")
    fact = cat_fact_model.get_fact()
    click.echo(textwrap.fill(fact, 100))
