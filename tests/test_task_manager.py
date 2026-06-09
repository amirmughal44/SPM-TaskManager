from datetime import date
from pathlib import Path
import tempfile
import unittest

from src.task_manager.core import TaskManager, summarize


class TaskManagerTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.storage_path = Path(self.temp_dir.name) / "tasks.json"
        self.manager = TaskManager(self.storage_path)

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_add_task_persists_to_json(self) -> None:
        task = self.manager.add_task(
            "Create issue list",
            description="Prepare five lab issues",
            owner="Amir Mughal",
            priority="high",
            due_date="2026-06-10",
        )

        reloaded = TaskManager(self.storage_path)
        self.assertEqual(reloaded.get_task(task.id).title, "Create issue list")
        self.assertEqual(reloaded.get_task(task.id).priority, "high")

    def test_complete_task_sets_done_status(self) -> None:
        task = self.manager.add_task("Review pull request")

        completed = self.manager.set_status(task.id, "done")

        self.assertEqual(completed.status, "done")
        self.assertIsNotNone(completed.completed_at)

    def test_search_matches_title_and_description(self) -> None:
        self.manager.add_task("Build dashboard", description="Kanban board view")
        self.manager.add_task("Write release notes", description="Version 1.0.0")

        results = self.manager.search("kanban")

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "Build dashboard")

    def test_overdue_tasks_excludes_completed_items(self) -> None:
        old_task = self.manager.add_task("Fix overdue task", due_date="2026-06-01")
        done_task = self.manager.add_task("Done old task", due_date="2026-06-01")
        self.manager.set_status(done_task.id, "done")

        overdue = self.manager.overdue_tasks(today=date(2026, 6, 9))

        self.assertEqual([task.id for task in overdue], [old_task.id])

    def test_summarize_counts_statuses(self) -> None:
        self.manager.add_task("First")
        task = self.manager.add_task("Second")
        self.manager.set_status(task.id, "in-progress")

        summary = summarize(self.manager.list_tasks())

        self.assertEqual(summary["todo"], 1)
        self.assertEqual(summary["in-progress"], 1)
        self.assertEqual(summary["done"], 0)


if __name__ == "__main__":
    unittest.main()
