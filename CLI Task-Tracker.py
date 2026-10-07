import json, argparse, time
from pathlib import Path

def is_file() -> Path:
    tasks_file = Path(__file__).resolve().parent / "tasks.json"

    try:
        with tasks_file.open("x", encoding="utf-8") as file:
            json.dump([], file)
    except FileExistsError:
        pass

    return tasks_file

def add_task(title: str) -> None:
    tasks_file = is_file()

    with tasks_file.open("r", encoding="utf-8") as file:
        tasks = json.load(file)

    if tasks:
        largest_id = max(task["id"] for task in tasks)
        next_id = largest_id + 1
    else:
        next_id = 1

    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    task = {
        "id": next_id,
        "title": title,
        "status": "to-do",
        "createdAt": now,
        "updatedAt": now
    }
    tasks.append(task)

    with tasks_file.open("w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=2)

    print()
    print(f"Task added(ID: {next_id})")
    print()

def update_task(task_id: int, new_title: str) -> None:
    tasks_file = is_file()

    with tasks_file.open("r", encoding="utf-8") as file:
        tasks = json.load(file)

    found_task = None

    for task in tasks:
        if task["id"] == task_id:
            found_task = task
            break

    if found_task is None:
        print("Task with this ID not found")
    else:
        found_task["title"] = new_title
        found_task["updatedAt"] = time.strftime(
            "%Y-%m-%d %H:%M:%S", time.localtime()
        )
        print()
        print(f"Task updated.")
        print()

    with tasks_file.open("w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=2)

def delete_task(task_id: int) -> None:
    tasks_file = is_file()

    with tasks_file.open("r", encoding="utf-8") as file:
        tasks = json.load(file)

    found_task = None

    for task in tasks:
        if task["id"] == task_id:
            found_task = task
            break

    if found_task is None:
        print("Task with this ID not found")
    else:
        tasks.remove(found_task)
        print()
        print(f"Task {task_id} deleted")
        print()

    for new_id, task in enumerate(tasks, start=1):
        task["id"] = new_id

    with tasks_file.open("w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=2)


def mark_in_progress(task_id: int) -> None:
    tasks_file = is_file()

    with tasks_file.open("r", encoding="utf-8") as file:
        tasks = json.load(file)

    found_task = None

    for task in tasks:
        if task["id"] == task_id:
            found_task = task
            break

    if found_task is None:
        print("Task with this ID not found")
    else:
        found_task["status"] = "in-progress"
        found_task["updatedAt"] = time.strftime(
            "%Y-%m-%d %H:%M:%S", time.localtime()
        )
        print()
        print(f"Task {task_id} in progress now")
        print()

    with tasks_file.open("w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=2)


def mark_completed(task_id: int) -> None:
    tasks_file = is_file()

    with tasks_file.open("r", encoding="utf-8") as file:
        tasks = json.load(file)

    found_task = None

    for task in tasks:
        if task['id'] == task_id:
            found_task = task
            break

    if found_task is None:
        print("Task with this ID not found")
    else:
        found_task["status"] = "completed"
        found_task["updatedAt"] = time.strftime(
            "%Y-%m-%d %H:%M:%S", time.localtime()
        )
        print()
        print(f"Task {task_id} is done")
        print()

    with tasks_file.open("w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=2)

def list_completed():
    tasks_file = is_file()

    with tasks_file.open("r", encoding="utf-8") as file:
        tasks = json.load(file)

    completed_tasks = []

    for task in tasks:
        if task['status'] == 'completed':
            completed_tasks.append(task)

    if completed_tasks:
        for task in completed_tasks:
            print(f"{task['id']} - {task['title']}")
            print()
    else:
        print("There is no completed tasks")

def list_todo():
    tasks_file = is_file()

    with tasks_file.open("r", encoding="utf-8") as file:
        tasks = json.load(file)

    todo_tasks = []

    for task in tasks:
        if task['status'] == 'to-do':
            todo_tasks.append(task)

    if todo_tasks:
        for task in todo_tasks:
            print(f"{task['id']} - {task['title']}")
            print()
    else:
        print(f"There is no to-do tasks")

def list_in_progress():
    tasks_file = is_file()

    with tasks_file.open("r", encoding="utf-8") as file:
        tasks = json.load(file)

    in_progress_tasks = []

    for task in tasks:
        if task['status'] == 'in-progress':
            in_progress_tasks.append(task)

    if in_progress_tasks:
        for task in in_progress_tasks:
            print(f"{task['id']} - {task['title']}")
            print()
    else:
        print(f"There is no in-progress tasks")

def list_all_tasks():
    tasks_file = is_file()

    with tasks_file.open("r", encoding="utf-8") as file:
        tasks = json.load(file)

    if tasks:
        for task in tasks:
            print(f"{task['id']} - {task['title']}")
            print()
    else:
        print("There is no tasks")

def clear_tasks():
    tasks_file = is_file()

    tasks = []

    with tasks_file.open("w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=2)

    print("Tasks are cleared")


parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="command", required=True)

update_parser = subparsers.add_parser("update")
update_parser.add_argument("task_id", type=int)
update_parser.add_argument("title")

add_parser = subparsers.add_parser("add")
add_parser.add_argument("title")

mark_in_progress_parser = subparsers.add_parser("mark-in-progress")
mark_in_progress_parser.add_argument("task_id", type=int)

mark_completed_parser = subparsers.add_parser("mark-completed")
mark_completed_parser.add_argument("task_id", type=int)

delete_parser = subparsers.add_parser("delete")
delete_parser.add_argument("task_id", type=int)

list_completed_parser = subparsers.add_parser("list-completed")

list_todo_parser = subparsers.add_parser("list-todo")

list_in_progress_parser = subparsers.add_parser("list-in-progress")

list_all_tasks_parser = subparsers.add_parser("list")

clear_tasks_parser = subparsers.add_parser("clear")

args = parser.parse_args()

if args.command == "clear":
    clear_tasks()

if args.command == "list":
    list_all_tasks()

if args.command == "list-in-progress":
    list_in_progress()

if args.command == "list-todo":
    list_todo()

if args.command == "list-completed":
    list_completed()

if args.command == "mark-completed":
    mark_completed(args.task_id)

if args.command == "mark-in-progress":
    mark_in_progress(args.task_id)

if args.command == "update":
    update_task(args.task_id, args.title)

if args.command == "add":
    add_task(args.title)

if args.command == "delete":
    delete_task(args.task_id)

if __name__ == "__main__":
    is_file()
