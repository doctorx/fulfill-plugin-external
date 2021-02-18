import click


@click.group(name="external")
def external_group():
    """ External service"""
    pass



@external_group.command()
def external_command():
    print("Hello external world")
