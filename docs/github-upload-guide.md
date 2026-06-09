# GitHub Upload Guide

The local repository is complete and ready to upload. The remote URL is already configured:

```text
origin  https://github.com/amirmughal44/SPM-TaskManager.git
```

## Required GitHub Step

Create an empty GitHub repository named:

```text
SPM-TaskManager
```

Use the account:

```text
amirmughal44
```

Do not initialize it with README, `.gitignore`, or license because these files already exist locally.

## Push Commands

After the GitHub repository exists and Git credentials are available:

```powershell
git push -u origin main
git push origin dev
git push origin feature-task-core feature-cli feature-lab-docs
git push origin conflict-release-plan-a conflict-release-plan-b
git push origin v1.0.0
```

## GitHub Items To Recreate Online

The local documentation already contains all required content. Recreate these on GitHub after pushing:

- Issues from `docs/issues.md`
- Pull requests from `docs/pull-requests.md`
- Kanban project board from `docs/project-board.md`
- Release `v1.0.0` using `docs/release-notes-v1.0.0.md`

## Why Upload May Fail

Upload requires one of these:

- An existing GitHub repository with write access.
- A working GitHub login in Git Credential Manager.
- GitHub CLI authenticated with `gh auth login`.
- A GitHub personal access token with repository permissions.
