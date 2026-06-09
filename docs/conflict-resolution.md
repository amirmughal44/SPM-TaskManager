# Merge Conflict Resolution Evidence

## Conflict Setup

Two branches changed the same line in `docs/conflict-target.md`.

- `conflict-release-plan-a` changed the release summary to require task validation and CLI testing.
- `conflict-release-plan-b` changed the release summary to require documentation, board evidence, and review notes.

## Conflict Command

```powershell
git switch dev
git merge --no-ff conflict-release-plan-a -m "Merge conflict-release-plan-a into dev"
git merge --no-ff conflict-release-plan-b -m "Merge conflict-release-plan-b into dev"
```

The second merge produced:

```text
CONFLICT (content): Merge conflict in docs/conflict-target.md
Automatic merge failed; fix conflicts and then commit the result.
```

## Manual Resolution

The final resolved line keeps both branches' useful recommendations:

```text
Release summary: Release after task validation, CLI testing, documentation, board evidence, and review notes are complete.
```

## Resolution Commit

```text
Task 5: resolve release summary merge conflict
```
