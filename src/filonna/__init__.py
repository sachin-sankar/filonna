import click


@click.command()
def hello():
    click.echo("Hello World!")


def main():
    hello()
