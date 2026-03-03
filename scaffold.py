# scaffold.py
# ---------------------------------------------------------------
# OPTIONAL SCAFFOLD — You do not have to use this file.
#
# If you want a head start, import AppShell in your app.py:
#
#     from scaffold import AppShell
#     app = AppShell()
#     app.run()
#
# If you prefer to build from scratch, ignore this file entirely
# and write your window setup directly in app.py.
#
# The AppShell class sets up:
#   - The main Tk window
#   - A ttk.Notebook with 3 placeholder tabs
#   - A menu bar with File and Help menus
#   - A status bar along the bottom
#
# You add your feature code in app.py by accessing:
#   self.tab1, self.tab2, self.tab3  (the three tab frames)
# ---------------------------------------------------------------

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import json


class AppShell:
    """
    Base class that provides a window, tabbed navigation, menu bar,
    and status bar. Extend or use directly in app.py.
    """

    def __init__(self, title="My App", width=850, height=620):
        # --- Main window setup ---
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}")
        self.root.minsize(600, 400)

        # --- Menu bar ---
        self._build_menu()

        # --- Notebook (tabbed interface) ---
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=(5, 0))

        # Three frames the student populates in app.py
        self.tab1 = ttk.Frame(self.notebook)
        self.tab2 = ttk.Frame(self.notebook)
        self.tab3 = ttk.Frame(self.notebook)

        # Default tab names — override in app.py by calling:
        #   self.notebook.tab(0, text="Your Tab Name")
        self.notebook.add(self.tab1, text="Tab 1")
        self.notebook.add(self.tab2, text="Tab 2")
        self.notebook.add(self.tab3, text="Tab 3")

        # --- Status bar along the bottom ---
        self.status_var = tk.StringVar(value="Ready")
        status_bar = tk.Label(
            self.root,
            textvariable=self.status_var,
            anchor="w",
            relief="sunken",
            padx=8,
            font=("Arial", 9),
            fg="#555555"
        )
        status_bar.pack(side="bottom", fill="x")

    # ------------------------------------------------------------------
    # MENU BAR
    # ------------------------------------------------------------------

    def _build_menu(self):
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

    # ------------------------------------------------------------------
    # MENU ACTIONS — override these in app.py to add real functionality
    # ------------------------------------------------------------------

    def save_data(self):
        """
        Override this method in app.py to save your app's data to a file.

        Example:
            def save_data(self):
                data = {"tasks": list(self.task_listbox.get(0, tk.END))}
                filename = filedialog.asksaveasfilename(
                    defaultextension=".json",
                    filetypes=[("JSON files", "*.json")]
                )
                if filename:
                    with open(filename, "w") as f:
                        json.dump(data, f, indent=2)
                    self.set_status("Data saved.")
        """
        messagebox.showinfo("Save", "Override save_data() in app.py to save your data.")

    def load_data(self):
        """
        Override this method in app.py to load data from a file.
        """
        messagebox.showinfo("Load", "Override load_data() in app.py to load your data.")

    def show_about(self):
        """Show an About dialog. Override in app.py to customize."""
        messagebox.showinfo(
            "About",
            f"{self.root.title()}\n\nBuilt with Python and Tkinter."
        )

    # ------------------------------------------------------------------
    # HELPERS
    # ------------------------------------------------------------------

    def set_status(self, message):
        """Update the status bar text at the bottom of the window."""
        self.status_var.set(message)

    def run(self):
        """Start the Tkinter event loop. Call this at the end of app.py."""
        self.root.mainloop()


# ------------------------------------------------------------------
# If you run scaffold.py directly, you'll see the bare shell.
# This is just for testing — your real app runs from app.py.
# ------------------------------------------------------------------
if __name__ == "__main__":
    app = AppShell(title="Scaffold Preview")
    app.run()
