import json
import sys
import os
from datetime import datetime


TASKS_FILE = os.path.join(os.path.dirname(__file__), "tasks.json")


class Task:
    def __init__(self, id, title, status="todo", created_at=None):
        self.id = id
        self.title = title
        self.status = status
        self.created_at = created_at or datetime.now().isoformat()

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "status": self.status,
            "created_at": self.created_at,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data["id"],
            title=data["title"],
            status=data["status"],
            created_at=data["created_at"],
        )


class TaskManager:
    def __init__(self):
        self.tasks = self._load()

    def _load(self):
        if not os.path.exists(TASKS_FILE):
            return []
        try:
            with open(TASKS_FILE, "r") as f:
                return [Task.from_dict(d) for d in json.load(f)]
        except (json.JSONDecodeError, KeyError, TypeError) as e:
            print(f"Warning: tasks.json is corrupt or unreadable ({e}). Starting fresh.")
            return []

    def _save(self):
        with open(TASKS_FILE, "w") as f:
            json.dump([t.to_dict() for t in self.tasks], f, indent=2)

    def _next_id(self):
        return max((t.id for t in self.tasks), default=0) + 1

    def _find(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def add_task(self, title):
        task = Task(id=self._next_id(), title=title)
        self.tasks.append(task)
        self._save()
        print(f"Added task [{task.id}]: {task.title}")

    def complete_task(self, task_id):
        task = self._find(task_id)
        if task is None:
            print(f"Error: No task with id {task_id}.")
            return
        task.status = "done"
        self._save()
        print(f"Marked task [{task_id}] as done: {task.title}")

    def list_tasks(self, filter=None):
        tasks = self.tasks
        if filter:
            if filter not in ("todo", "done"):
                print(f"Error: filter must be 'todo' or 'done', got '{filter}'.")
                return
            tasks = [t for t in tasks if t.status == filter]
        if not tasks:
            print("No tasks found.")
            return
        print(f"{'ID':<4} {'Status':<6} {'Created':<22} Title")
        print("-" * 60)
        for t in tasks:
            created = t.created_at[:19].replace("T", " ")
            print(f"{t.id:<4} {t.status:<6} {created:<22} {t.title}")

    def delete_task(self, task_id):
        task = self._find(task_id)
        if task is None:
            print(f"Error: No task with id {task_id}.")
            return
        self.tasks.remove(task)
        self._save()
        print(f"Deleted task [{task_id}]: {task.title}")


def main():
    args = sys.argv[1:]
    if not args:
        print("Usage:")
        print("  python exercise_1.py add 'title'")
        print("  python exercise_1.py done <id>")
        print("  python exercise_1.py delete <id>")
        print("  python exercise_1.py list [--filter todo|done]")
        return

    manager = TaskManager()
    command = args[0]

    if command == "add":
        if len(args) < 2:
            print("Error: provide a task title.")
            return
        manager.add_task(" ".join(args[1:]))

    elif command == "done":
        if len(args) < 2 or not args[1].isdigit():
            print("Error: provide a valid task id.")
            return
        manager.complete_task(int(args[1]))

    elif command == "delete":
        if len(args) < 2 or not args[1].isdigit():
            print("Error: provide a valid task id.")
            return
        manager.delete_task(int(args[1]))

    elif command == "list":
        filter_val = None
        if "--filter" in args:
            idx = args.index("--filter")
            if idx + 1 >= len(args):
                print("Error: --filter requires a value (todo|done).")
                return
            filter_val = args[idx + 1]
        manager.list_tasks(filter=filter_val)

    else:
        print(f"Error: unknown command '{command}'.")


if __name__ == "__main__":
    main()
