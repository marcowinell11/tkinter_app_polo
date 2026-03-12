# Student Productivity Suite

## Overview
A desktop GUI application built with Python and Tkinter. This is a student productivity tool featuring:
- **Task Manager** — Add, complete, and delete tasks
- **Study Timer** — Pomodoro-style countdown timer
- **Grade Calculator** — Placeholder for future implementation

## Architecture
- **Language:** Python 3.12
- **GUI Framework:** Tkinter (via `python312Packages.tkinter` nix package)
- **Entry point:** `app.py`
- **Output type:** VNC (desktop GUI, not a web app)

## Running the App
The app runs via the "Start application" workflow using VNC output.

### Important: tkinter PYTHONPATH
Because the Nix package for tkinter (`python312Packages.tkinter`) installs the `_tkinter` shared library to a separate nix store path, the workflow command must set PYTHONPATH explicitly:

```bash
PYTHONPATH=/nix/store/izkldz9a5b7kbdlgfm1n7zrmmp6ihs1m-python3.12-tkinter-3.12.11/lib/python3.12/site-packages:$PYTHONPATH python3 app.py
```

This is configured in the workflow command and in `.replit`.

## Files
| File | Purpose |
|------|---------|
| `app.py` | Main application — all UI and logic |
| `code_review_sample.py` | Sample code for code review exercise (Part 4) |
| `my_app_spec.md` | App design document for Path B students |
| `README.md` | Project instructions |

## Nix Dependencies
- `python312Packages.tkinter` — provides `_tkinter` shared library for Python 3.12.11
