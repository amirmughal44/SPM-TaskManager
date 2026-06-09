"""Core task management logic."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import date, datetime
import json
from pathlib import Path
from typing import Iterable
from uuid import uuid4


VALID_PRIORITIES = {"low", "medium", "high"}
VALID_STATUSES = {"todo", "in-progress", "done"}


@dataclass
class Task:
    """A single task item."""

    id: str
    title: str
    description: str = ""
    owner: str = "Unassigned"
    priority: str = "medium"
    status: str = "todo"
    due_date: str | None = None
    created_at: str = ""
    completed_at: str | None = None

    @classmethod
    def create(
        cls,
        title: str,
        description: str = "",
        owner: str = "Unassigned",
        priority: str = "medium",
        due_date: str | None = None,
    ) -> "Task":
        title = title.strip()
        if not title:
            raise ValueError("Task title is required.")
        if priority not in VALID_PRIORITIES:
            raise ValueError(f"Priority must be one of: {', '.join(sorted(VALID_PRIORITIES))}.")
        if due_date:
            _parse_date(due_date)
        return cls(
            id=str(uuid4()),
            title=title,
            description=description.strip(),
            owner=owner.strip() or "Unassigned",
            priority=priority,
            due_date=due_date,
            created_at=datetime.utcnow().isoformat(timespec="seconds") + "Z",
        )

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "Task":
        return cls(
            id=str(data["id"]),
            title=str(data["title"]),
            description=str(data.get("description", "")),
            owner=str(data.get("owner", "Unassigned")),
            priority=str(data.get("priority", "medium")),
            status=str(data.get("status", "todo")),
            due_date=data.get("due_date") if data.get("due_date") else None,
            created_at=str(data.get("created_at", "")),
            completed_at=data.get("completed_at") if data.get("completed_at") else None,
        )

    def to_dict(self) -> dict[str, object]:
        return asdict(self)


class TaskManager:
    """Manage tasks loaded from a JSON file."""

    def __init__(self, storage_path: str | Path = "data/tasks.json") -> None:
        self.storage_path = Path(storage_path)
        self.tasks: list[Task] = []
        self.load()

    def load(self) -> None:
        if not self.storage_path.exists():
            self.tasks = []
            return
        raw_tasks = json.loads(self.storage_path.read_text(encoding="utf-8"))
        self.tasks = [Task.from_dict(item) for item in raw_tasks]

    def save(self) -> None:
        self.storage_path.parent.mkdir(parents=True, exist_ok=True)
        payload = [task.to_dict() for task in self.tasks]
        self.storage_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    def add_task(
        self,
        title: str,
        description: str = "",
        owner: str = "Unassigned",
        priority: str = "medium",
        due_date: str | None = None,
    ) -> Task:
        task = Task.create(title, description, owner, priority, due_date)
        self.tasks.append(task)
        self.save()
        return task

    def list_tasks(self, status: str | None = None) -> list[Task]:
        if status is None:
            return list(self.tasks)
        _validate_status(status)
        return [task for task in self.tasks if task.status == status]

    def get_task(self, task_id: str) -> Task:
        for task in self.tasks:
            if task.id == task_id:
                return task
        raise KeyError(f"Task not found: {task_id}")

    def update_task(self, task_id: str, **changes: str | None) -> Task:
        task = self.get_task(task_id)
        if "title" in changes and changes["title"] is not None:
            title = changes["title"].strip()
            if not title:
                raise ValueError("Task title is required.")
            task.title = title
        if "description" in changes and changes["description"] is not None:
            task.description = changes["description"].strip()
        if "owner" in changes and changes["owner"] is not None:
            task.owner = changes["owner"].strip() or "Unassigned"
        if "priority" in changes and changes["priority"] is not None:
            priority = changes["priority"]
            if priority not in VALID_PRIORITIES:
                raise ValueError(f"Priority must be one of: {', '.join(sorted(VALID_PRIORITIES))}.")
            task.priority = priority
        if "due_date" in changes:
            due_date = changes["due_date"]
            if due_date:
                _parse_date(due_date)
            task.due_date = due_date
        self.save()
        return task

    def set_status(self, task_id: str, status: str) -> Task:
        _validate_status(status)
        task = self.get_task(task_id)
        task.status = status
        task.completed_at = datetime.utcnow().isoformat(timespec="seconds") + "Z" if status == "done" else None
        self.save()
        return task

    def delete_task(self, task_id: str) -> Task:
        task = self.get_task(task_id)
        self.tasks = [item for item in self.tasks if item.id != task_id]
        self.save()
        return task

    def search(self, query: str) -> list[Task]:
        needle = query.casefold().strip()
        if not needle:
            return []
        return [
            task
            for task in self.tasks
            if needle in task.title.casefold() or needle in task.description.casefold()
        ]

    def overdue_tasks(self, today: date | None = None) -> list[Task]:
        today = today or date.today()
        return [
            task
            for task in self.tasks
            if task.due_date and _parse_date(task.due_date) < today and task.status != "done"
        ]


def summarize(tasks: Iterable[Task]) -> dict[str, int]:
    summary = {status: 0 for status in VALID_STATUSES}
    for task in tasks:
        summary[task.status] += 1
    return summary


def _validate_status(status: str) -> None:
    if status not in VALID_STATUSES:
        raise ValueError(f"Status must be one of: {', '.join(sorted(VALID_STATUSES))}.")


def _parse_date(value: str) -> date:
    return datetime.strptime(value, "%Y-%m-%d").date()
