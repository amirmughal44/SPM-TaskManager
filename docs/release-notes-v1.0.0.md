# Release Notes: v1.0.0

## Version

`v1.0.0`

## Summary

This stable release completes the SPM Task Manager lab workflow and provides a functional command-line task manager.

## Included Features

- Task creation with title, description, owner, priority, and due date.
- Task listing by status.
- Task updates for title, description, owner, priority, and due date.
- Status changes for `todo`, `in-progress`, and `done`.
- Task deletion.
- Task search.
- Overdue task reporting.
- Status summary counts.
- Unit tests for persistence, completion, search, overdue behavior, and summaries.

## Workflow Evidence

- Required repository structure added.
- `main`, `dev`, and feature branches used.
- Five issues documented.
- Pull requests and reviews documented.
- Merge conflict created and resolved.
- Project board documented.
- Tag `v1.0.0` created locally.

## Test Command

```powershell
python -m unittest discover -s tests
```
