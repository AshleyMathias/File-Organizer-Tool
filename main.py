import tkinter as tk
from tkinter import filedialog, messagebox
import shutil
import os

FILE_TYPES = {
    "Images": [".png", ".jpg", ".jpeg", ".gif"],
    "Videos": [".mp4", ".mov", ".mkv"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar"],
}

root = tk.Tk()
root.title("File Organizer Tool")
root.geometry("500x250")
root.configure(bg="#e6f2ff")


#step 2: define variable to hold folder
folder_path = tk.StringVar()

#Step 3: Function to select folder
def choose_folder():
    folder = filedialog.askdirectory()
    if folder:
        folder_path.set(folder)
    
# Organize files by type
def organize_files():
    folder = folder_path.get()
    if not folder:
        messagebox.showwarning("No Folder", "Please choose a folder first.")
        return

    files = os.listdir(folder)
    if not files:
        messagebox.showinfo("Empty", "The selected folder is empty.")
        return

    for file in files:
        full_path = os.path.join(folder, file)
        if os.path.isfile(full_path):  # Ignore folders
            ext = os.path.splitext(file)[1].lower()
            moved = False

            for folder_name, extensions in FILE_TYPES.items():
                if ext in extensions:
                    dest_folder = os.path.join(folder, folder_name)
                    os.makedirs(dest_folder, exist_ok=True)  # Create if not exists
                    shutil.move(full_path, os.path.join(dest_folder, file))
                    moved = True
                    break

            if not moved:
                others_folder = os.path.join(folder, "Others")
                os.makedirs(others_folder, exist_ok=True)
                shutil.move(full_path, os.path.join(others_folder, file))

    messagebox.showinfo("Done", "Files have been organized!")

#Step 4: Add a title label
title_label = tk.Label(root, text="📁 File Organizer Tool", font = ("Helvetica",18,"bold"), bg="#e6f2ff", fg="#003366")
title_label.pack(pady=20)

#step 5: Add a button to select or open a folder dialog
choose_button = tk.Button(root, text="Choose Folder", command=choose_folder, bg="#0099cc", fg="white", font=("Arial", 12), padx=10, pady=5)
choose_button.pack(pady=10)



#Step 6: Label to show selected folder path
path_display = tk.Label(root, textvariable=folder_path,wraplength=450, bg="#ffffff", fg="#333333", font=("Arial", 10), padx=10, pady=5)
path_display.pack(pady=5)

# Organize button
organize_button = tk.Button(root, text="Organize Files", command=organize_files,
                            bg="#28a745", fg="white", font=("Arial", 12), padx=10, pady=5)
organize_button.pack(pady=10)

#step 7: Start the main loop to show window
root.mainloop()