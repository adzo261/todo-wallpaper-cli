import click
from db_helper import add_task, remove_task, get_list
from wallpaper import set_wallpaper


@click.command()
@click.option('-a', '--add', help='Task you want to add')
@click.option('-rm', '--remove', help='Type comma separated IDs of tasks you want to remove OR all to remove all tasks')
def cli(add, remove):
    if add:
        add_task(add)
    elif remove:
        remove_task(remove)
    else:
        list()
    set_wallpaper()


def list():
    todo_list = get_list()
    if len(todo_list) != 0:
        click.echo("ID :     DESCRIPTION")
        for key, value in todo_list.items():
            click.echo(key+"  :      "+value)
    else:
        click.echo("No tasks found")
