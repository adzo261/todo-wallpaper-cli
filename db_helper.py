import os
import pickledb
PATH_TO_DB = os.path.join(os.path.abspath(
    os.path.dirname(__file__)), "todo.db")
db = pickledb.load(PATH_TO_DB, True)


def get_smallest_unused_id():
    key_list = db.getall()
    for i in range(1, len(key_list)+2):
        if str(i) not in key_list:
            return str(i)


def add_task(add):
    db.set(get_smallest_unused_id(), add)
    print("Task added successfully")


def remove_task(delete):
    id_list = [s for s in delete.split(',')]
    if id_list[0] == 'all':
        db.deldb()
        print("All tasks removed successfully")
    else:
        for task_id in id_list:
            db.rem(task_id)
            print("Task with id="+task_id+" removed successfully")


def get_list():
    todo_list = {key: db.get(key) for key in db.getall()}
    return todo_list
