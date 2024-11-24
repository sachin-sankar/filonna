import click
from filonna.helpers import get_config_value
from rich import print
from rich.panel import Panel


@click.group()
def cli():
    pass


@cli.group("config")
def config():
    """Work wih filonna config"""
    pass


@config.command()
def init():
    """Create filonna.ini in your OS respective config folder if not exists"""
    if get_config_value("basic", "media_path") == "none":
        print(
            Panel(
                title=":information: Info",
                expand=False,
                renderable="You havent setup you media library paths yet, to setup run \n[bold yellow]filonna setup[/]",
            )
        )
    else:
        print("[green] Config good[/]")


def main():
    cli()
