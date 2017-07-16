import click

@click.command()
@click.option('--done', '-d', help="move item to done list. item required.")
@click.option('--remove', '-r', help="straight up delete item. item required." )
@click.option('--resurrect', '-r', help="move item from done list to todo list")
@click.option('--amend', help="change item text. defaults to last item added.")
def todo(done, remove, amend, resurrect):
    pass


