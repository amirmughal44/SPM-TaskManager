"""Command-line interface for SPM Task Manager."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Sequence

from .core import Task, TaskManager, VALID_PRIORITIES, VALID_STATUSES, summarize


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="spm-task", description="Manage project tasks.")
    parser.add_argument(
        "--data",
        default="data/tasks.json",
        help="Path to the JSON task storage file.",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="Create a task.")
    add_parser.add_argument("title")
    add_parser.add_argument("--description", default="")
    add_parser.add_argument("--owner", default="Unassigned")
    add_parser.add_argument("--priority", choices=sorted(VALID_PRIORITIES), default="medium")
    add_parser.add_argument("--due-date")

    list_parser = subparsers.add_parser("list", help="List tasks.")
    list_parser.add_argument("--status", choices=sorted(VALID_STATUSES))

    update_parser = subparsers.add_parser("update", help="Update a task.")
    update_parser.add_argument("task_id")
    update_parser.add_argument("--title")
    update_parser.add_argument("--description")
    update_parser.add_argument("--owner")
    update_parser.add_argument("--priority", choices=sorted(VALID_PRIORITIES))
    update_parser.add_argument("--due-date")

    status_parser = subparsers.add_parser("status", help="Change task status.")
    status_parser.add_argument("task_id")
    status_parser.add_argument("status", choices=sorted(VALID_STATUSES))

    delete_parser = subparsers.add_parser("delete", help="Delete a task.")
    delete_parser.add_argument("task_id")

    search_parser = subparsers.add_parser("search", help="Search tasks.")
    search_parser.add_argument("query")

    subparsers.add_parser("summary", help="Show status counts.")
    subparsers.add_parser("overdue", help="List overdue tasks.")

    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    manager = TaskManager(Path(args.data))

    if args.command == "add":
        task = manager.add_task(
            args.title,
            description=args.description,
            owner=args.owner,
            priority=args.priority,
            due_date=args.due_date,
        )
        print(f"Created task {task.id}: {task.title}")
        return 0

    if args.command == "list":
        _print_tasks(manager.list_tasks(status=args.status))
        return 0

    if args.command == "update":
        task = manager.update_task(
            args.task_id,
            title=args.title,
            description=args.description,
            owner=args.owner,
            priority=args.priority,
            due_date=args.due_date,
        )
        print(f"Updated task {task.id}: {task.title}")
        return 0

    if args.command == "status":
        task = manager.set_status(args.task_id, args.status)
        print(f"Updated status for {task.id}: {task.status}")
        return 0

    if args.command == "delete":
        task = manager.delete_task(args.task_id)
        print(f"Deleted task {task.id}: {task.title}")
        return 0

    if args.command == "search":
        _print_tasks(manager.search(args.query))
        return 0

    if args.command == "summary":
        for status, count in sorted(summarize(manager.list_tasks()).items()):
            print(f"{status}: {count}")
        return 0

    if args.command == "overdue":
        _print_tasks(manager.overdue_tasks())
        return 0

    parser.error(f"Unknown command: {args.command}")
    return 2


def _print_tasks(tasks: Sequence[Task]) -> None:
    if not tasks:
        print("No tasks found.")
        return

    for task in tasks:
        due = f", due {task.due_date}" if task.due_date else ""
        print(f"{task.id} | {task.status} | {task.priority} | {task.owner} | {task.title}{due}")


if __name__ == "__main__":
    raise SystemExit(main())
