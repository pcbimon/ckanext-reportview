import click


@click.group(short_help="reportview CLI.")
def reportview():
    """reportview CLI.
    """
    pass


@reportview.command()
@click.argument("name", default="reportview")
def command(name):
    """Docs.
    """
    click.echo("Hello, {name}!".format(name=name))


def get_commands():
    return [reportview]
