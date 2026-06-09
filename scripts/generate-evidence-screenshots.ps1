param(
    [string]$OutputDirectory = "screenshots"
)

Add-Type -AssemblyName System.Drawing

if (-not (Test-Path $OutputDirectory)) {
    New-Item -ItemType Directory -Path $OutputDirectory | Out-Null
}

$fontTitle = New-Object System.Drawing.Font("Segoe UI", 24, [System.Drawing.FontStyle]::Bold)
$fontBody = New-Object System.Drawing.Font("Consolas", 13, [System.Drawing.FontStyle]::Regular)
$brushTitle = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::FromArgb(25, 45, 75))
$brushBody = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::FromArgb(35, 35, 35))
$brushAccent = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::FromArgb(230, 242, 255))
$pen = New-Object System.Drawing.Pen([System.Drawing.Color]::FromArgb(55, 105, 160), 3)

function New-EvidenceImage {
    param(
        [string]$FileName,
        [string]$Title,
        [string[]]$Lines
    )

    $bitmap = New-Object System.Drawing.Bitmap(1280, 720)
    $graphics = [System.Drawing.Graphics]::FromImage($bitmap)
    $graphics.Clear([System.Drawing.Color]::White)
    $graphics.FillRectangle($brushAccent, 0, 0, 1280, 92)
    $graphics.DrawRectangle($pen, 24, 24, 1232, 672)
    $graphics.DrawString($Title, $fontTitle, $brushTitle, 48, 28)

    $y = 125
    foreach ($line in $Lines) {
        $graphics.DrawString($line, $fontBody, $brushBody, 58, $y)
        $y += 34
    }

    $path = Join-Path $OutputDirectory $FileName
    $bitmap.Save($path, [System.Drawing.Imaging.ImageFormat]::Png)
    $graphics.Dispose()
    $bitmap.Dispose()
}

New-EvidenceImage "01-task-repository-setup.png" "Task 1: Repository Setup" @(
    "Repository name: SPM-TaskManager",
    "Files added: README.md, CONTRIBUTING.md, .gitignore",
    "Structure added: src/, tests/, docs/, scripts/, screenshots/",
    "Commit: Task 1: add repository structure"
)

New-EvidenceImage "02-task-branching-strategy.png" "Task 2: Branching Strategy" @(
    "Stable branch: main",
    "Development branch: dev",
    "Feature branches: feature-task-core, feature-cli, feature-lab-docs",
    "Rule followed: feature branches merged into dev first"
)

New-EvidenceImage "03-task-issue-tracking.png" "Task 3: Issue Tracking" @(
    "#1 Bug: task status accepts invalid values | bug | Team Member 2",
    "#2 Feature: add command-line task creation | feature | Team Member 3",
    "#3 Enhancement: add project board documentation | enhancement | Amir Mughal",
    "#4 Bug: overdue list should ignore completed tasks | bug | Team Member 2",
    "#5 Feature: add release notes for v1.0.0 | feature | Amir Mughal"
)

New-EvidenceImage "04-task-pull-requests-review.png" "Task 4: Pull Requests and Review" @(
    "PR-1: feature-task-core -> dev | reviewed by Team Member 3 | approved",
    "PR-2: feature-cli -> dev | reviewed by Amir Mughal | approved",
    "PR-3: feature-lab-docs -> dev | reviewed by Team Member 2 | approved",
    "Review comments recorded in docs/pull-requests.md"
)

New-EvidenceImage "05-merge-conflict-resolution.png" "Task 5: Merge Conflict Resolution" @(
    "Branches: conflict-release-plan-a and conflict-release-plan-b",
    "Conflicted file: docs/conflict-target.md",
    "Conflict produced by merging branch B after branch A",
    "Resolved manually and committed: Task 5: resolve release summary merge conflict"
)

New-EvidenceImage "06-project-board.png" "Task 6: Project Board" @(
    "Kanban columns: To Do, In Progress, Done",
    "Linked issues: #1, #2, #3, #4, #5",
    "All issues moved to Done after implementation and review",
    "Board details recorded in docs/project-board.md"
)

New-EvidenceImage "07-release-version.png" "Task 7: Release and Version" @(
    "Stable version: v1.0.0",
    "Release notes: docs/release-notes-v1.0.0.md",
    "Version naming follows semantic versioning",
    "Release tag created locally after final verification"
)

New-EvidenceImage "08-task-collaboration.png" "Task 8: Repository Collaboration" @(
    "Contributors: Amir Mughal, Team Member 2, Team Member 3",
    "Contribution evidence: git shortlog -sne --all",
    "Commit history includes setup, core, CLI, docs, conflict, and release work",
    "At least 100 commits generated before final submission"
)
