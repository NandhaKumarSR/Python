#Folder maker program

import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

def select_directory():
    directory = filedialog.askdirectory()
    directory_var.set(directory)

def create_folders():
    directory = directory_var.get()
    folder_name = folder_name_var.get()
    try:
        start_number = int(start_number_var.get())
        end_number = int(end_number_var.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Start and End numbers must be integers.")
        return

    if not directory or not folder_name:
        messagebox.showerror("Missing Information", "Please provide all the required information.")
        return

    if start_number > end_number:
        messagebox.showerror("Invalid Range", "Start number should be less than or equal to end number.")
        return

    for folder_number in range(start_number, end_number + 1):
        folder_path = os.path.join(directory, f"{folder_name} {folder_number}")
        if os.path.exists(folder_path):
            response = messagebox.askyesno("Folder Exists", f"'{folder_name} {folder_number}' exists.\nDo you want to replace it?")
            if response:
                shutil.rmtree(folder_path)
            else:
                continue
        os.makedirs(folder_path)
    messagebox.showinfo("Success", "Folders created successfully!")

# Initialize the main window
root = tk.Tk()
root.title("Folder Maker")

# Variables to hold user input
directory_var = tk.StringVar()
folder_name_var = tk.StringVar()
start_number_var = tk.StringVar(value="1")
end_number_var = tk.StringVar()

# GUI Layout
tk.Label(root, text="Select Directory:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
tk.Entry(root, textvariable=directory_var, width=40).grid(row=0, column=1, pady=5)
tk.Button(root, text="Browse", command=select_directory).grid(row=0, column=2, padx=10, pady=5)

tk.Label(root, text="Folder Name:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
tk.Entry(root, textvariable=folder_name_var).grid(row=1, column=1, pady=5)

tk.Label(root, text="Start Number:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
tk.Entry(root, textvariable=start_number_var).grid(row=2, column=1, pady=5)

tk.Label(root, text="End Number:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
tk.Entry(root, textvariable=end_number_var).grid(row=3, column=1, pady=5)

tk.Button(root, text="Create Folders", command=create_folders, bg="#4CAF50", fg="white").grid(row=4, column=1, pady=20)

# Run the application
root.mainloop()