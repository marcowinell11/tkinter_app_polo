# GUI & Teamwork: Personal Productivity App
### A Multi-Part Programming Project

---

## Overview

In this project you will build a **desktop application using Python and Tkinter** — from a blank window all the way to a polished, functional app. Each Part builds directly on the last, so by the end you have one complete project you can be proud of.

You will also practice real-world developer habits: using **Git and GitHub** to track your progress, writing a **code review** of someone else's work, and reflecting on your own **career direction** as a programmer.

---

## Choose Your Path

You have two options. Pick one before you write any code.

### 🗂 Path A: Personal Productivity App
Follow the provided specification. You will build a productivity app with a task manager, study timer, and grade calculator. Starter scaffolding is provided in `scaffold.py` and `app.py` to get you going quickly.

### 🎨 Path B: Your Own App
Design your own app. It must hit all the same technical requirements, but the theme, features, and purpose are entirely up to you. Fill out `my_app_spec.md` before you begin coding — this is your design document and your first Git commit.

> **Not sure?** Go with Path A. You can always make it your own by customizing colors, fonts, and feature details as you build.

---

## Git Setup (Do This First — Every Student)

You will use Git and GitHub to save your progress. Every Part ends with a commit. This mirrors how real development teams track their work.

### Step 1: Create a GitHub Account
Go to [github.com](https://github.com) and create a free account if you don't have one.

### Step 2: Create a New Repository
- Click the **+** icon → **New repository**
- Name it something like `productivity-app` or your own app name
- Set it to **Public**
- Check **"Add a README file"**
- Click **Create repository**

### Step 3: Connect to Your Project

**On Replit:**
1. Open your Repl and click the **Git** icon in the left sidebar (looks like a branch)
2. Click **"Connect to GitHub"** and authorize Replit
3. Click **"Connect to an existing GitHub repository"**
4. Select the repo you just created
5. You're connected — you'll stage, commit, and push from this panel throughout the project

**On the command line (local development):**
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```

### Step 4: Add Your Project Files
Copy `app.py`, `scaffold.py`, `code_review_sample.py`, and (if Path B) `my_app_spec.md` into your project folder/Repl.

### Step 5: Your First Commit

**On Replit Git panel:**
1. You'll see your new files listed under "Changes"
2. Click the **+** next to each file to stage it
3. Type a commit message in the box: `Initial commit: project files added`
4. Click **Commit & Push**

**On the command line:**
```bash
git add .
git commit -m "Initial commit: project files added"
git push origin main
```

> ✅ Check GitHub in your browser — your files should now appear in the repository.

---

## How Commits Work Throughout This Project

At the end of **every Part**, you will commit your work. A good commit message describes *what you did and why*, not just "updated code." Examples:

| Weak message | Strong message |
|---|---|
| `changes` | `Part 1: window and widgets set up, layout uses Pack` |
| `added stuff` | `Part 2: tab navigation added with Grid layout in timer frame` |
| `done` | `Part 4: accessibility fixes — contrast improved, input validation added` |

You will be assessed on your commit history, so make them count.

---

## Part 1: The Window & Widgets

**Outcomes covered:** Explain the characteristics and capabilities of Windows apps · Add widgets to a GUI using Tkinter

### Background

Desktop apps are different from websites and scripts in an important way: they are **event-driven**. Nothing happens until the user does something — clicks a button, types in a field, selects an item. Your code doesn't run top-to-bottom; it waits, listens, and responds.

Before you write code, take 5 minutes to think about a desktop app you use regularly. Notice:
- It has a persistent window that stays open
- It remembers state (what you typed, what you selected)
- Every interaction triggers something
- It gives you feedback when something goes wrong

Your app will do all of these things by the end of this project.

### Instructions

Open `app.py`. If you're using the scaffold, the basic window structure is already imported — your job is to customize it and add widgets. If you're building from scratch, create your window from the ground up.

**By the end of Part 1, your app must have:**

- [ ] A working window with a meaningful title and appropriate starting size
- [ ] At least one `Label`
- [ ] At least one `Button` that does something when clicked (even just prints to console for now)
- [ ] At least one `Entry` field (text input)
- [ ] At least one `Listbox` or `Text` widget
- [ ] Widgets arranged using at least one layout manager (`pack`, `grid`, or `place`)
- [ ] A short comment block at the top of `app.py` describing what your app does and who made it

**Path A students:** Follow the structure in `app.py` — set up the main window and populate the Task Manager tab with the widgets listed above.

**Path B students:** Your widgets should match your spec in `my_app_spec.md`. If your spec needs updating based on what you're learning, update the spec file too and include it in your commit.

### Commit Checklist
When Part 1 is complete:

**Replit:**
1. Open the Git panel
2. Stage all changed files
3. Write your commit message (describe what you built in Part 1)
4. Click Commit & Push

**Command line:**
```bash
git add app.py
git commit -m "Part 1: [describe what you built]"
git push origin main
```

---

## Part 2: Layouts & Navigation

**Outcomes covered:** Create advanced GUIs using different layouts in Tkinter

### Background

Tkinter has three layout managers, and experienced developers use them deliberately:

- **`pack()`** — Simple and fast. Stacks widgets vertically or horizontally. Good for toolbars, button rows, and simple frames.
- **`grid()`** — Places widgets in rows and columns. Best for forms, calculators, anything that lines up neatly.
- **`place()`** — Pixel-precise positioning. Rarely the right choice, but useful for overlapping elements or custom designs.

You should use at least **two different layout managers** in your app, in different frames, for a reason you can explain.

A `ttk.Notebook` gives you a tabbed interface — the cleanest way to organize multiple features in one window without overwhelming the user.

### Instructions

**By the end of Part 2, your app must have:**

- [ ] A `ttk.Notebook` with at least **3 tabs** (or equivalent navigation if Path B calls for something different)
- [ ] `grid()` used in at least one frame
- [ ] `pack()` used in at least one frame
- [ ] A menu bar with at least **File** and **Help** menus
  - File menu: Save, Load, Exit
  - Help menu: About (shows a messagebox with your app name and your name)
- [ ] All tabs visible and switchable (content can still be placeholder for now)
- [ ] A comment in your code explaining *why* you chose each layout manager where you used it

### Commit Checklist

**Replit:**
1. Stage changes in the Git panel
2. Commit message should describe your layout decisions specifically
3. Commit & Push

**Command line:**
```bash
git add app.py
git commit -m "Part 2: [describe navigation and layout choices]"
git push origin main
```

---

## Part 3: Functional Code Behind the GUI

**Outcomes covered:** Develop functional code behind a graphical user interface in Tkinter

### Background

So far your app looks like something. Now it needs to *do* something. This is where the real programming lives — connecting user actions to logic, storing data, and making the app actually useful.

You'll also add **data persistence**: the app saves its state to a file when the user saves, and loads it back when the app opens. This is what separates a real app from a demo.

### Instructions

**By the end of Part 3, your app must have:**

- [ ] At least **2 fully functional features** (not placeholders) with real logic behind them
- [ ] At least **5 event handlers** total (button clicks, key presses, listbox selections, etc.)
- [ ] **Input validation** — if a user submits an empty field or invalid input, the app catches it and shows a helpful `messagebox` warning rather than crashing
- [ ] **Save functionality** — exports app data to a `.json` file using `filedialog.asksaveasfilename()`
- [ ] **Load functionality** — reads that `.json` file back in and restores the app state
- [ ] All functions have a one-line docstring describing what they do

**Path A — the two features to complete:**

1. **Task Manager:** Add task, mark complete (strikethrough or moved to "Done" list), delete task, tasks save/load from JSON
2. **Study Timer:** Countdown timer (user sets minutes), starts/pauses/resets, displays time remaining, plays a sound or shows a popup when done

*The Grade Calculator tab can remain as a polished placeholder for now — you'll have time to extend it if you finish early.*

**Path B:** Complete whichever two features are highest priority in your spec. Document in a comment what remains to be built.

### Commit Checklist

**Replit:**
1. Stage changes
2. Write a detailed commit message — name the features you completed
3. Commit & Push

**Command line:**
```bash
git add app.py
git commit -m "Part 3: [list the features you implemented]"
git push origin main
```

---

## Part 4: Ethical Design & Code Review

**Outcomes covered:** Discuss the legal and ethical components of user interfaces [Inclusive] · Participate in a peer code review

### Part 4A: Code Review

Open `code_review_sample.py` and run it. Read through the code carefully. Then write your review in a file called `code_review.txt` (create this file in your project).

Your review must address all of the following:

**1. What does this code do?**
In 2-3 sentences, describe what the app is supposed to do.

**2. What works well?**
Identify at least **2 specific things** the code does correctly or clearly. Reference line numbers.

**3. What could break?**
Identify at least **2 things** that could cause errors or unexpected behavior. Describe exactly what a user would have to do to trigger the problem.

**4. Code quality issues**
Identify at least **2 issues** with readability or style — variable names, missing comments, repeated code, etc.

**5. Your concrete suggestion**
Pick the single most important problem and write the corrected code. Show the before and after.

> A good code review is specific, kind, and actionable. Vague feedback like "this is confusing" isn't useful. "Line 23: the variable `x` should be named `task_input` so its purpose is clear" is useful.

### Part 4B: Accessibility & Ethical UI Audit

Read through the following principles, then audit your own app against them.

**Key principles:**
- **Color contrast** — Text and background should have sufficient contrast. WCAG AA standard requires a 4.5:1 ratio for normal text. In practice: don't put light grey text on a white background.
- **Keyboard navigation** — Can a user operate your app without a mouse? Tab should move between fields, Enter should activate buttons.
- **Clear language** — Button labels and error messages should be plain English. "Submit" is better than "Execute." "Please enter a task name" is better than "Error 001."
- **Error handling** — Never let the app crash silently. Always tell the user what went wrong and how to fix it.
- **Data privacy** — Where is user data stored? Who can access it? Your app saves to a local file — note that this means data stays on the user's machine, which is good.

**Deliverable:** Add a section to `code_review.txt` called `MY APP AUDIT` and document:
- [ ] 3 specific accessibility or ethical issues you found in your own app
- [ ] The change you made to fix each one (with before/after code snippets if relevant)
- [ ] One thing your app does *well* from an ethical/inclusive design standpoint

### Commit Checklist

**Replit:**
1. Stage `app.py` (with your fixes) and `code_review.txt`
2. Commit message should mention both the review and the fixes
3. Commit & Push

**Command line:**
```bash
git add app.py code_review.txt
git commit -m "Part 4: code review complete, accessibility fixes applied"
git push origin main
```

---

## Part 5: Final Polish & Career Plan

**Outcomes covered:** Select and use appropriate communication tools for programmers · Create a personal career plan [Self-Aware]

### Part 5A: Final Polish & Communication Reflection

Spend the first portion of this session finishing anything incomplete, fixing any remaining bugs, and making your app feel polished. Then write a short section at the top of your `code_review.txt` (or a new file `dev_log.txt`) that answers:

1. What communication tools would a real development team use on a project like this? Name at least 3 (e.g. GitHub Issues, Slack, pull requests, project boards) and briefly describe what each is used for.
2. Look at your Git commit history. Does it tell the story of how your project developed? What would you do differently with your commits next time?
3. What was the hardest part of this project technically? How did you work through it?

### Part 5B: Career Plan

Open `career_plan.txt` and respond to each prompt. This is a personal reflection — there are no wrong answers, only shallow ones. Write in full sentences.

### Final Commit

**Replit:**
1. Stage all remaining files
2. Final commit message: `Part 5: project complete — [one sentence about what you built]`
3. Commit & Push

**Command line:**
```bash
git add .
git commit -m "Part 5: project complete — [one sentence about what you built]"
git push origin main
```

Then share your GitHub repository link with your instructor.

---

## Grading Overview

| Part | Focus | Points |
|------|-------|--------|
| Part 1 | Window & Widgets | 15 |
| Part 2 | Layouts & Navigation | 20 |
| Part 3 | Functional Code | 30 |
| Part 4A | Code Review | 15 |
| Part 4B | Ethical UI Audit | 10 |
| Part 5A | Dev Communication Reflection | 5 |
| Git History | Quality of commits across all parts | 5 |
| **Total** | | **100** |

*Career Plan (`career_plan.txt`) is submitted as a separate assignment.*

---

## Quick Reference: Tkinter Widgets

| Widget | What it's for |
|--------|--------------|
| `tk.Label` | Display text or images |
| `tk.Button` | Clickable button |
| `tk.Entry` | Single-line text input |
| `tk.Text` | Multi-line text input/display |
| `tk.Listbox` | Scrollable list of items |
| `ttk.Notebook` | Tabbed interface |
| `ttk.Frame` | Container for grouping widgets |
| `tk.Menu` | Menu bar |
| `tk.Scrollbar` | Scrollbar (attach to Text or Listbox) |
| `messagebox` | Popup alerts and confirmations |
| `filedialog` | Open/save file dialogs |
