import click

from bushu.book import Book
from bushu.http.client import Client


@click.group()
@click.option('--username', default=None)
@click.option('--password', default=None)
@click.option('--directory', default=None)
@click.pass_context
def cli(ctx, username, password, directory):
    client = Client(username, password)
    if username is not None and password is not None:
        client.login()
    book = Book(client)
    if directory is not None:
        book.directory = directory
    ctx.obj = book


@cli.command()
@click.option('--chapter', type=int, required=False, default=None)
@click.option('--all', is_flag=True)
@click.argument('identifier')
@click.pass_obj
def book(obj, identifier, all, chapter):
    obj.manga_url = identifier
    obj.enumerate_chapters()
    if chapter is not None:
        obj.chapter_number = chapter
    obj.get_chapter_data()
    if all:
        obj.download_book()
    else:
        obj.download_chapter()