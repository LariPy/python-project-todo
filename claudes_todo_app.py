
# using this for learning/ideas/inspiration

"""
Simple To-Do List App
----------------------
A GUI todo app built with Tkinter. Tasks are saved to a JSON file
(tasks.json) so they persist between runs.

Run with:  python todo_app.py
"""

import json
import os
import tkinter as tk
from tkinter import messagebox, simpledialog

DATA_FILE = "tasks.json"


def load_tasks():
    """Load tasks from the JSON file, or return an empty list if none exists."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []


def save_tasks(tasks):
    """Write the current list of tasks to the JSON file."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=4, ensure_ascii=False)


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("420x480")
        self.root.minsize(360, 400)

        self.tasks = load_tasks()  # each task: {"text": str, "done": bool}

        # --- Entry row ---
        entry_frame = tk.Frame(root, padx=10, pady=10)
        entry_frame.pack(fill=tk.X)

        self.entry = tk.Entry(entry_frame, font=("Segoe UI", 12))
        self.entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.entry.bind("<Return>", lambda event: self.add_task())

        add_btn = tk.Button(entry_frame, text="Add", command=self.add_task)
        add_btn.pack(side=tk.LEFT, padx=(8, 0))

        # --- Task list ---
        list_frame = tk.Frame(root, padx=10)
        list_frame.pack(fill=tk.BOTH, expand=True)

        self.listbox = tk.Listbox(
            list_frame, font=("Segoe UI", 12), selectmode=tk.SINGLE, activestyle="none"
        )
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.listbox.bind("<Double-Button-1>", lambda event: self.toggle_done())

        scrollbar = tk.Scrollbar(list_frame, command=self.listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.config(yscrollcommand=scrollbar.set)

        # --- Buttons row ---
        btn_frame = tk.Frame(root, padx=10, pady=10)
        btn_frame.pack(fill=tk.X)

        tk.Button(btn_frame, text="Toggle Done", command=self.toggle_done).pack(
            side=tk.LEFT, expand=True, fill=tk.X, padx=2
        )
        tk.Button(btn_frame, text="Edit", command=self.edit_task).pack(
            side=tk.LEFT, expand=True, fill=tk.X, padx=2
        )
        tk.Button(btn_frame, text="Delete", command=self.delete_task).pack(
            side=tk.LEFT, expand=True, fill=tk.X, padx=2
        )

        self.refresh_listbox()

        # Save on close
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def refresh_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            prefix = "[x] " if task["done"] else "[ ] "
            self.listbox.insert(tk.END, prefix + task["text"])
            if task["done"]:
                self.listbox.itemconfig(tk.END, fg="gray")

    def add_task(self):
        text = self.entry.get().strip()
        if not text:
            return
        self.tasks.append({"text": text, "done": False})
        self.entry.delete(0, tk.END)
        self.refresh_listbox()
        save_tasks(self.tasks)

    def get_selected_index(self):
        selection = self.listbox.curselection()
        if not selection:
            messagebox.showinfo("No selection", "Please select a task first.")
            return None
        return selection[0]

    def toggle_done(self):
        index = self.get_selected_index()
        if index is None:
            return
        self.tasks[index]["done"] = not self.tasks[index]["done"]
        self.refresh_listbox()
        save_tasks(self.tasks)

    def edit_task(self):
        index = self.get_selected_index()
        if index is None:
            return
        current_text = self.tasks[index]["text"]
        new_text = simpledialog.askstring(
            "Edit Task", "Update task text:", initialvalue=current_text
        )
        if new_text:
            self.tasks[index]["text"] = new_text.strip()
            self.refresh_listbox()
            save_tasks(self.tasks)

    def delete_task(self):
        index = self.get_selected_index()
        if index is None:
            return
        confirm = messagebox.askyesno("Delete Task", "Delete the selected task?")
        if confirm:
            del self.tasks[index]
            self.refresh_listbox()
            save_tasks(self.tasks)

    def on_close(self):
        save_tasks(self.tasks)
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()