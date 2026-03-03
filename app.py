# app.py
# ---------------------------------------------------------------
# YOUR NAME:
# PROJECT NAME:
# DATE STARTED:
# DESCRIPTION:
#   (Write 2-3 sentences describing what your app does.)
# ---------------------------------------------------------------
#
# HOW TO USE THIS FILE:
#
# OPTION A (using the scaffold):
#   The AppShell class in scaffold.py gives you a ready-made
#   window, tabs, and menu bar. This file imports it and adds
#   your features on top. Just follow the TODO comments below.
#
# OPTION B (from scratch):
#   Delete the import line and the AppShell reference below.
#   Build your own Tk window from the ground up.
#   The TODO structure still applies — just implement everything
#   directly in your own class or functions.
#
# ---------------------------------------------------------------

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import json

# --- OPTION A: Import the scaffold base class ---
from scaffold import AppShell

# ================================================================
# YOUR APP CLASS
# Extends AppShell (Option A) or builds from scratch (Option B)
# ================================================================

class MyApp(AppShell):
    """
    Main application class. Inherits window, tabs, and menu from
    AppShell. All feature setup methods are called from __init__.
    """

    def __init__(self):
        # --- Call the parent scaffold setup ---
        # Change the title and size to match your app.
        super().__init__(title="Student Productivity Suite", width=850, height=620)

        # --- Rename tabs to match your features ---
        # (Do this after super().__init__ so the notebook exists)
        self.notebook.tab(0, text="Tasks")
        self.notebook.tab(1, text="Study Timer")
        self.notebook.tab(2, text="Grades")

        # --- Initialize your data stores ---
        # Add any lists, dicts, or variables your app needs to track state.
        self.tasks = []          # Example for Task Manager
        self.timer_running = False

        # --- Build each tab's interface ---
        # TODO (Part 1 & 2): Call your setup methods here.
        self.setup_task_manager()
        self.setup_study_timer()
        self.setup_grade_calculator()

    # ================================================================
    # PART 1 & 2 — TAB SETUP
    # Each method populates one tab with widgets and layout.
    # ================================================================

    def setup_task_manager(self):
        """
        Build the Task Manager tab interface.
        Uses: self.tab1
        Layout: pack for the overall structure, grid for the input row.
        TODO (Part 1): Add your widgets.
        TODO (Part 2): Finalize layout — use grid in the input row,
                       pack for the listbox and button area.
        """
        # -- Header --
        tk.Label(
            self.tab1,
            text="Task Manager",
            font=("Arial", 16, "bold")
        ).pack(pady=(15, 5))

        # -- Input row (grid layout) --
        input_frame = tk.Frame(self.tab1)
        input_frame.pack(pady=5)

        tk.Label(input_frame, text="New task:").grid(row=0, column=0, padx=5)

        # TODO (Part 1): Create self.task_entry and add it to input_frame
        self.task_entry = tk.Entry(input_frame, width=35)
        self.task_entry.grid(row=0, column=1, padx=5)
        # Bind Enter key so user doesn't have to click Add every time
        self.task_entry.bind("<Return>", lambda event: self.add_task())

        tk.Button(
            input_frame,
            text="Add Task",
            command=self.add_task
        ).grid(row=0, column=2, padx=5)

        # -- Task listbox (pack layout) --
        list_frame = tk.Frame(self.tab1)
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
        btn_frame = tk.Frame(self.tab1)
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
        Build the Study Timer tab interface.
        Uses: self.tab2
        TODO (Part 1): Add label, entry, and button widgets.
        TODO (Part 2): Use grid layout throughout this tab.
        TODO (Part 3): Wire up the countdown logic.
        """
        # -- Header --
        tk.Label(
            self.tab2,
            text="Study Timer",
            font=("Arial", 16, "bold")
        ).grid(row=0, column=0, columnspan=3, pady=(15, 10))

        # -- Minutes input --
        tk.Label(self.tab2, text="Minutes:").grid(row=1, column=0, padx=10, sticky="e")

        self.timer_entry = tk.Entry(self.tab2, width=6, font=("Arial", 13))
        self.timer_entry.insert(0, "25")  # Default: 25-minute Pomodoro
        self.timer_entry.grid(row=1, column=1, padx=5, sticky="w")

        # -- Countdown display --
        self.timer_display = tk.Label(
            self.tab2,
            text="25:00",
            font=("Arial", 48, "bold"),
            fg="#2c3e50"
        )
        self.timer_display.grid(row=2, column=0, columnspan=3, pady=20)

        # -- Control buttons --
        btn_frame = tk.Frame(self.tab2)
        btn_frame.grid(row=3, column=0, columnspan=3, pady=10)

        # TODO (Part 3): Connect these to your timer logic
        tk.Button(
            btn_frame, text="Start", width=10,
            command=self.start_timer
        ).pack(side="left", padx=8)

        tk.Button(
            btn_frame, text="Pause", width=10,
            command=self.pause_timer
        ).pack(side="left", padx=8)

        tk.Button(
            btn_frame, text="Reset", width=10,
            command=self.reset_timer
        ).pack(side="left", padx=8)

        # Center the grid columns
        self.tab2.columnconfigure(0, weight=1)
        self.tab2.columnconfigure(1, weight=1)
        self.tab2.columnconfigure(2, weight=1)


    def setup_grade_calculator(self):
        """
        Build the Grade Calculator tab interface.
        Uses: self.tab3
        TODO (Part 2): Add widgets and layout.
        TODO (Part 3): Implement grade calculation logic.
        Note: This tab can remain a polished placeholder until
              the core features (Task Manager, Timer) are done.
        """
        tk.Label(
            self.tab3,
            text="Grade Calculator",
            font=("Arial", 16, "bold")
        ).pack(pady=(15, 5))

        tk.Label(
            self.tab3,
            text="Coming soon — build this after completing Parts 1-3.",
            font=("Arial", 11),
            fg="#888888"
        ).pack(pady=20)

        # TODO (Part 3 extension): Replace the placeholder above with
        # a form where the user enters assignment names, scores, and
        # weights, and the app calculates a weighted average.


    # ================================================================
    # PART 3 — EVENT HANDLERS & LOGIC
    # Connect your widgets to real functionality.
    # ================================================================

    # --- Task Manager logic ---

    def add_task(self):
        """Add a new task to the listbox from the entry field."""
        # TODO (Part 3): Get text from self.task_entry.
        # If empty, show a messagebox warning.
        # Otherwise, insert into self.task_listbox and clear the entry.
        task = self.task_entry.get().strip()
        if not task:
            messagebox.showwarning("Empty Task", "Please enter a task name.")
            return
        self.task_listbox.insert(tk.END, f"☐  {task}")
        self.task_entry.delete(0, tk.END)
        self.set_status(f"Task added: {task}")

    def complete_task(self):
        """Mark the selected task as complete."""
        # TODO (Part 3): Get the selected index from self.task_listbox.
        # Update its text to show it's complete (e.g., add ✓ or strikethrough style).
        # If nothing is selected, show a warning.
        pass

    def delete_task(self):
        """Delete the selected task from the listbox."""
        # TODO (Part 3): Get selected index, delete it.
        # If nothing is selected, show a warning.
        pass

    # --- Timer logic ---

    def start_timer(self):
        """Start or resume the countdown timer."""
        # TODO (Part 3): Read minutes from self.timer_entry.
        # Validate that it's a positive integer.
        # Begin countdown, updating self.timer_display each second.
        # Use self.root.after(1000, ...) for the countdown loop.
        # When timer hits 0:0, show a messagebox and stop.
        pass

    def pause_timer(self):
        """Pause the running timer."""
        # TODO (Part 3): Stop the countdown without resetting the time.
        pass

    def reset_timer(self):
        """Reset the timer to the entered value."""
        # TODO (Part 3): Stop countdown, restore display to entered minutes.
        pass

    # ================================================================
    # PART 3 — SAVE & LOAD (override scaffold placeholders)
    # ================================================================

    def save_data(self):
        """Save all app data to a JSON file chosen by the user."""
        # TODO (Part 3): Build a dict with all data you want to save.
        # Example structure shown below — expand for your features.
        data = {
            "tasks": list(self.task_listbox.get(0, tk.END)),
            # "grades": [...],  # add when Grade Calculator is built
        }

        filename = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json")],
            title="Save App Data"
        )
        if filename:
            with open(filename, "w") as f:
                json.dump(data, f, indent=2)
            self.set_status(f"Saved to {filename}")
            messagebox.showinfo("Saved", "Your data has been saved.")

    def load_data(self):
        """Load app data from a JSON file chosen by the user."""
        # TODO (Part 3): Open file dialog, read JSON, restore app state.
        filename = filedialog.askopenfilename(
            filetypes=[("JSON files", "*.json")],
            title="Load App Data"
        )
        if filename:
            with open(filename, "r") as f:
                data = json.load(f)

            # Restore tasks
            self.task_listbox.delete(0, tk.END)
            for task in data.get("tasks", []):
                self.task_listbox.insert(tk.END, task)

            self.set_status(f"Loaded from {filename}")
            messagebox.showinfo("Loaded", "Your data has been loaded.")

    def show_about(self):
        """Show app info dialog."""
        # TODO (Part 1): Update with your name and app description.
        messagebox.showinfo(
            "About",
            "Student Productivity Suite\n\nBuilt with Python & Tkinter\nCreated by: [Your Name]"
        )


# ================================================================
# ENTRY POINT — Run the app
# ================================================================

if __name__ == "__main__":
    app = MyApp()
    app.run()
