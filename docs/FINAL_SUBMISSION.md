# Final Submission: Lab 2 GitHub Workflow

## Repository

Repository name: `SPM-TaskManager`

Remote URL prepared locally:

```text
https://github.com/amirmughal44/SPM-TaskManager.git
```

## Completed Lab Tasks

| Task | Requirement | Evidence |
| --- | --- | --- |
| Task 1 | Repository setup and structure | `README.md`, `CONTRIBUTING.md`, `.gitignore` |
| Task 2 | Branching strategy | `main`, `dev`, `feature-task-core`, `feature-cli`, `feature-lab-docs` |
| Task 3 | Issue tracking | `docs/issues.md` |
| Task 4 | Pull requests and code review | `docs/pull-requests.md` and merge commits |
| Task 5 | Merge conflict resolution | `docs/conflict-resolution.md`, `docs/conflict-target.md` |
| Task 6 | Project board management | `docs/project-board.md` |
| Task 7 | Release and version management | `docs/release-notes-v1.0.0.md`, tag `v1.0.0` |
| Task 8 | Repository collaboration | `docs/team.md`, `docs/workflow-checkpoints.md` |

## Screenshots

| Screenshot | File |
| --- | --- |
| Repository setup | `screenshots/01-task-repository-setup.png` |
| Branching strategy | `screenshots/02-task-branching-strategy.png` |
| Issue tracking | `screenshots/03-task-issue-tracking.png` |
| Pull requests and review | `screenshots/04-task-pull-requests-review.png` |
| Merge conflict resolution | `screenshots/05-merge-conflict-resolution.png` |
| Project board | `screenshots/06-project-board.png` |
| Release version | `screenshots/07-release-version.png` |
| Collaboration | `screenshots/08-task-collaboration.png` |

## Verification Commands

```powershell
git branch --list
git tag --list
git rev-list --count --all
git shortlog -sne --all
python -m unittest discover -s tests
```

## Final Verification Result

- Commit count: 100+ commits.
- Tests: 5 passing tests.
- Stable release tag: `v1.0.0`.
- Working tree: clean.
