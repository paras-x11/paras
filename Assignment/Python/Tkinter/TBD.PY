import tkinter as tk
from tkinter import messagebox
import sqlite3

# Connect to the database
def get_db_connection():
    conn = sqlite3.connect('todo_list.db')
    return conn

# Function to refresh the task list from the database
def refresh_task_list():
    task_listbox.delete(0, tk.END)  # Clear current listbox
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks')  # Get all tasks from database
    tasks = cursor.fetchall()
    for task in tasks:
        task_listbox.insert(tk.END, task[1])  # Insert only task name (not id)
    conn.close()

# Function to add a new task
def add_task():
    task = task_entry.get()
    if task != "":
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO tasks (task) VALUES (?)', (task,))
        conn.commit()
        conn.close()
        task_entry.delete(0, tk.END)  # Clear the input field
        refresh_task_list()  # Refresh the listbox to show updated tasks
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# Function to delete a selected task
def delete_task():
    selected_task_index = task_listbox.curselection()  # Get selected task
    if selected_task_index:
        task = task_listbox.get(selected_task_index)  # Get the task text
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM tasks WHERE task = ?', (task,))
        conn.commit()
        conn.close()
        refresh_task_list()  # Refresh the listbox to show updated tasks
    else:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

# Tkinter window setup
root = tk.Tk()
root.title("To-Do List App")

# Entry widget to add a task
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

# Add Task Button
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=10)

# Listbox to display tasks
task_listbox = tk.Listbox(root, width=40, height=10)
task_listbox.pack(pady=10)

# Delete Task Button
delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=10)

# Refresh task list on startup
refresh_task_list()

# Run the Tkinter main loop
root.mainloop()
