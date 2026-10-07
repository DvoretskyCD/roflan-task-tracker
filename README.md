# Roflan Task Tracker

## Installation

Download the source code ZIP archive from **Releases** and extract it.

## Run in PowerShell

Open PowerShell in the project folder. You can run commands with Python:

```powershell
python ".\CLI Task-Tracker.py" add "Buy milk"
python ".\CLI Task-Tracker.py" list
```

## Commands

| `add "Title"` | Add a task |
| `list` | List all tasks |
| `list-todo` | List tasks with the `to-do` status |
| `list-in-progress` | List tasks with the `in-progress` status |
| `list-completed` | List completed tasks |
| `update ID "New title"` | Rename a task |
| `mark-in-progress ID` | Mark a task as in progress |
| `mark-completed ID` | Mark a task as completed |
| `delete ID` | Delete a task |
| `clear` | Delete all tasks |
