# app.py
# ---------------------------------------------------------------
# YOUR NAME:Marco Montez Winell
# PROJECT NAME:Productivity App Polo
# DATE STARTED:
# DESCRIPTION:This app produces tivity.
#   (Write 2-3 sentences describing what your app does.)
# ---------------------------------------------------------------

import tkinter as tk
from tkinter import messagebox, filedialog
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import json


class MyApp:
    """Main application class. Sets up the window and all features."""

    def __init__(self, root):
        # --- Window setup ---
        self.root = root
        self.root.title("Polo Productivity App!")  # TODO: Change to your app name
        self.root.geometry("850x620")
        self.root.minsize(600, 400)

        # --- Data ---
        # These store your app's state while it's running.
        self.tasks = []
        self.task_notes = []  # parallel list — one note string per task

        # --- Build the UI ---
        self.create_menu()
        self.create_tabs()
        self.setup_task_manager()
        self.setup_study_timer()
        self.setup_notes()

        # --- Status bar along the bottom ---
        self.status_var = tk.StringVar(value="Ready")
        tk.Label(
            self.root,
            textvariable=self.status_var,
            anchor="w",
            relief="sunken",
            padx=8,
            font=("Arial", 9),
            fg="#555555"
        ).pack(side="bottom", fill="x")

    # ================================================================
    # PART 2 — MENU & TABS
    # ================================================================

    def create_menu(self):
        """Build the top menu bar with File and Help menus."""
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Save", command=self.save_data)
        file_menu.add_command(label="Load", command=self.load_data)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)

        # Help menu
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.show_about)

    def create_tabs(self):
        """Create the tabbed notebook and three tab frames."""
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=5)

        self.tab_tasks  = ttk.Frame(self.notebook)
        self.tab_timer  = ttk.Frame(self.notebook)
        self.tab_notes = ttk.Frame(self.notebook)

        # TODO (Part 2): Rename these to match your app's features
        self.notebook.add(self.tab_tasks,  text="Tasks")
        self.notebook.add(self.tab_timer,  text="Study Timer")
        self.notebook.add(self.tab_notes, text="Notes")

    # ================================================================
    # PART 1 & 2 — TAB CONTENT
    # Each method below fills one tab with widgets.
    # ================================================================

    def setup_task_manager(self):
        """
        Build the Task Manager tab.
        Layout: grid for the input row, pack for everything else.
        """
        # -- Header --
        tk.Label(
            self.tab_tasks,
            text="Task Manager",
            font=("Arial", 16, "bold")
        ).pack(pady=(15, 5))

        # -- Input row (grid layout) --
        # Grid is used here so the label, entry, and button line up neatly.
        input_frame = tk.Frame(self.tab_tasks)
        input_frame.pack(pady=5)

        tk.Label(input_frame, text="New task:").grid(row=0, column=0, padx=5)

        self.task_entry = tk.Entry(input_frame, width=35)
        self.task_entry.grid(row=0, column=1, padx=5)
        # Pressing Enter works the same as clicking Add
        self.task_entry.bind("<Return>", lambda event: self.add_task())

        tk.Button(
            input_frame,
            text="Add Task",
            command=self.add_task
        ).grid(row=0, column=2, padx=5)

        # -- Task listbox (pack layout) --
        list_frame = tk.Frame(self.tab_tasks)
        list_frame.pack(pady=10, fill="both", expand=True, padx=20)

        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side="right", fill="y")

        self.task_listbox = tk.Listbox(
            list_frame,
            width=55,
            height=14,
            yscrollcommand=scrollbar.set,
            font=("Arial", 11),
            selectmode="single"
        )
        self.task_listbox.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=self.task_listbox.yview)

        # -- Action buttons (pack layout) --
        btn_frame = tk.Frame(self.tab_tasks)
        btn_frame.pack(pady=5)

        tk.Button(
            btn_frame,
            text="Mark Complete",
            command=self.complete_task
        ).pack(side="left", padx=8)

        tk.Button(
            btn_frame,
            text="Delete Task",
            command=self.delete_task
        ).pack(side="left", padx=8)

    def setup_study_timer(self):
        """
        Build the Study Timer tab.
        Layout: grid throughout so everything centers neatly.
        """
        # Give columns equal weight so widgets stay centered
        for col in range(3):
            self.tab_timer.columnconfigure(col, weight=1)

        tk.Label(
            self.tab_timer,
            text="Study Timer",
            font=("Arial", 16, "bold")
        ).grid(row=0, column=0, columnspan=3, pady=(15, 10))

        tk.Label(self.tab_timer, text="Minutes:").grid(
            row=1, column=0, padx=10, sticky="e"
        )

        self.timer_entry = tk.Entry(self.tab_timer, width=6, font=("Arial", 13))
        self.timer_entry.insert(0, "25")  # Default: 25-minute Pomodoro
        self.timer_entry.grid(row=1, column=1, padx=5, sticky="w")

        # Large countdown display
        self.timer_display = tk.Label(
            self.tab_timer,
            text="25:00",
            font=("Arial", 48, "bold"),
            fg="#2c3e50"
        )
        self.timer_display.grid(row=2, column=0, columnspan=3, pady=20)

        # Control buttons
        btn_frame = tk.Frame(self.tab_timer)
        btn_frame.grid(row=3, column=0, columnspan=3, pady=10)

        tk.Button(btn_frame, text="Start", width=10, command=self.start_timer).pack(side="left", padx=8)
        tk.Button(btn_frame, text="Pause", width=10, command=self.pause_timer).pack(side="left", padx=8)
        tk.Button(btn_frame, text="Reset", width=10, command=self.reset_timer).pack(side="left", padx=8)

        # Internal timer state — not widgets, just variables we need
        self.timer_running = False
        self.timer_seconds = 0
        self._timer_job = None  # holds the root.after() reference so we can cancel it

    def setup_notes(self):
        """
        Build the Notes tab.
        This is a placeholder — complete it after the other tabs are working.
        """
        tk.Label(
            self.tab_notes,
            text="Notes",
            font=("Arial", 16, "bold")
        ).pack(pady=(15, 5))

        input_frame = tk.Frame(self.tab_notes)
        input_frame.pack(pady=5)
        tk.Label(input_frame, text="New note:").grid(row=0, column=0, padx=5)

        self.note_entry = tk.Entry(input_frame, width=35)
        self.note_entry.grid(row=0, column=1, padx=5)

        self.note_entry = tk.Entry(input_frame, width=35)
        self.note_entry.grid(row=0, column=1, padx=5)
        # Pressing Enter works the same as clicking Add
        self.note_entry.bind("<Return>", lambda event: self.add_note())

        tk.Button(
            input_frame,
            text="Add Note",
            command=self.add_note
        ).grid(row=0, column=2, padx=5)
        
        list_frame = tk.Frame(self.tab_notes)
        list_frame.pack(pady=10, fill="both", expand=True, padx=20)
        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side="right", fill="y")
        self.notes_listbox = tk.Listbox(
            list_frame,
            width=55,
            height=14,
            yscrollcommand=scrollbar.set,
            font=("Arial", 11),
            selectmode="single"
        )
        self.notes_listbox.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=self.notes_listbox.yview)

        # TODO (stretch goal): Replace the placeholder above with a form
        # where the user enters assignment names, scores, and weights,
        # and the app calculates a weighted average.

    # ================================================================
    # PART 3 — EVENT HANDLERS
    # This is where widgets connect to real logic.
    # ================================================================

    # --- Task Manager ---

    def add_task(self):
        """Get text from the entry field and add it to the listbox."""
        task = self.task_entry.get().strip()
        if not task:
            messagebox.showwarning("Empty Task", "Please enter a task name before clicking Add.")
            return
        self.task_listbox.insert(tk.END, f"☐  {task}")
        self.task_entry.delete(0, tk.END)
        self.status_var.set(f"Task added: {task}")

    def complete_task(self):
        """Mark the selected task as complete by updating its text."""
        selected = self.task_listbox.curselection()
        if not selected:
            messagebox.showwarning("No Selection", "Please select a task to mark complete.")
            return
        index = selected[0]
        task_text = self.task_listbox.get(index)
        if task_text.startswith("☐"):
            updated = task_text.replace("☐", "✓", 1)
            self.task_listbox.delete(index)
            self.task_listbox.insert(index, updated)
            self.task_listbox.itemconfig(index, fg="#888888")
        self.status_var.set("Task marked complete.")

    def delete_task(self):
        """Delete the selected task from the listbox."""
        selected = self.task_listbox.curselection()
        if not selected:
            messagebox.showwarning("No Selection", "Please select a task to delete.")
            return
        self.task_listbox.delete(selected[0])
        self.status_var.set("Task deleted.")

    # --- Study Timer ---

    def start_timer(self):
        """Start or resume the countdown timer."""
        if self.timer_running:
            return  # Already running, nothing to do

        # If starting fresh (not resuming a paused timer), read from the entry
        if self.timer_seconds == 0:
            try:
                minutes = int(self.timer_entry.get())
                if minutes <= 0:
                    raise ValueError
                self.timer_seconds = minutes * 60
            except ValueError:
                messagebox.showwarning("Invalid Input", "Please enter a whole number greater than 0.")
                return

        self.timer_running = True
        self._tick()

    def _tick(self):
        """
        Counts down one second, then schedules itself to run again.

        root.after(1000, self._tick) tells Tkinter:
        "Wait 1000 milliseconds, then call _tick again."
        This keeps the window responsive while the timer runs.
        """
        if not self.timer_running:
            return

        if self.timer_seconds <= 0:
            self.timer_display.config(text="00:00")
            self.timer_running = False
            messagebox.showinfo("Time's Up!", "Your study session is complete — take a break!")
            return

        mins, secs = divmod(self.timer_seconds, 60)
        self.timer_display.config(text=f"{mins:02d}:{secs:02d}")
        self.timer_seconds -= 1
        self._timer_job = self.root.after(1000, self._tick)

    def pause_timer(self):
        """Pause the running timer without resetting it."""
        if self.timer_running:
            self.timer_running = False
            if self._timer_job:
                self.root.after_cancel(self._timer_job)
            self.status_var.set("Timer paused.")

    def reset_timer(self):
        """Stop the timer and reset the display to the entered value."""
        self.timer_running = False
        if self._timer_job:
            self.root.after_cancel(self._timer_job)
        self.timer_seconds = 0
        try:
            minutes = int(self.timer_entry.get())
        except ValueError:
            minutes = 25
        self.timer_display.config(text=f"{minutes:02d}:00")
        self.status_var.set("Timer reset.")
    def add_note(self):
        note = self.note_entry.get().strip()
        if not note:
            messagebox.showwarning("Empty Note", "Please enter a note name before clicking Add.")
            return
        self.notes_listbox.insert(tk.END, f"☐  {note}")
        self.note_entry.delete(0, tk.END)
        self.status_var.set(f"Note added: {note}")

    # ================================================================
    # PART 3 — SAVE & LOAD
    # ================================================================

    def save_data(self):
        """Save app data to a JSON file chosen by the user."""
        data = {
            "tasks": list(self.task_listbox.get(0, tk.END)),
            # Add more keys here as you build more features
        }
        filename = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json")],
            title="Save App Data"
        )
        if filename:
            with open(filename, "w") as f:
                json.dump(data, f, indent=2)
            self.status_var.set(f"Saved to {filename}")
            messagebox.showinfo("Saved", "Your data has been saved successfully.")

    def load_data(self):
        """Load app data from a JSON file chosen by the user."""
        filename = filedialog.askopenfilename(
            filetypes=[("JSON files", "*.json")],
            title="Load App Data"
        )
        if filename:
            with open(filename, "r") as f:
                data = json.load(f)
            self.task_listbox.delete(0, tk.END)
            for task in data.get("tasks", []):
                self.task_listbox.insert(tk.END, task)
            self.status_var.set(f"Loaded from {filename}")
            messagebox.showinfo("Loaded", "Your data has been loaded successfully.")

    def show_about(self):
        """Show an About dialog."""
        # TODO: Update with your name and app description
        messagebox.showinfo(
            "About",
            "Polo Productivity App!\n\nBuilt with Python & Tkinter\nCreated by: Marco Montez Winell"
        )

# ================================================================
# ENTRY POINT
# ================================================================

if __name__ == "__main__":
    root = ttk.Window(themename="superhero")
    app = MyApp(root)
    root.mainloop()