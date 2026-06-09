# SPM Task Manager

SPM Task Manager is a small command-line task management application built for the Software Project Management lab on advanced GitHub workflows and collaboration.

The project demonstrates:

- A clean repository structure.
- A `main`, `dev`, and feature-branch workflow.
- Issue tracking, pull request, review, project board, merge conflict, and release evidence.
- A stable `v1.0.0` release-ready version.

## Features

- Create, list, update, complete, and delete tasks.
- Store task data in JSON.
- Track task priority, owner, status, and due date.
- Search tasks by title or description.

## Project Structure

```text
SPM-TaskManager/
  src/task_manager/      Application source code
  tests/                 Unit tests
  docs/                  Lab evidence and workflow documentation
  screenshots/           Screenshot-style evidence exports
  scripts/               Helper scripts
```

## Quick Start

```powershell
python -m task_manager.cli --help
python -m unittest discover
```

## Lab Status

This repository is prepared for Lab 2: Advanced GitHub Workflow & Collaboration.
