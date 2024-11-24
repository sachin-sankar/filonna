import click
from filonna.helpers import get_config_file_path
from rich import print


@click.group()
def cli():
    pass


@cli.group("config")
def config():
    """Work wih filonna config"""
    pass


@config.command()
def init():
    """Create filonna.ini in your OS respective config folder"""
    path = get_config_file_path()
    print(f"[green]Created filonna.ini at [/][blue bold]{path}[/]")


def main():
    cli()
