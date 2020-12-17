import click

from bushu.book import Book
from bushu.http.client import Client

@click.group()
@click.option('--username', default=None)
@click.option('--password', default=None)
@click.pass_context
def cli(ctx, username, password):
    ctx.obj = Book(Client(username, password))

@cli.command()
@click.argument('identifier')
@click.argument('chapter', required=False)
@click.pass_obj
def book(obj, identifier, chapter):
    obj.manga_url = identifier
    click.echo(obj.directory)