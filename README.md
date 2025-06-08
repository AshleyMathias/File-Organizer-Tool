# 📁 File Organizer & Directory Automation Tool

[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)](https://www.python.org/)
[![Tkinter](https://img.shields.io/badge/GUI-Tkinter-yellow?logo=python)]
[![Repo Status](https://img.shields.io/badge/status-Active-success)]

> A simple yet powerful Python GUI tool to clean up and organize messy directories based on file types.

---

## ✨ Features

- 📂 Select any folder from your system
- 🧠 Automatically sorts files into subfolders like `Images`, `Documents`, `Videos`, etc.
- 🎨 Simple and vibrant UI built with Tkinter
- ⚙️ Uses built-in Python modules for seamless performance
- 📦 One-click automation for file management

---

## 🖥️ GUI Preview

![App Screenshot](Screenshot.png)

---

## 🛠️ How It Works

1. Select a target folder using the GUI
2. The tool scans all files in that folder
3. Files are moved into subfolders based on file types:
    - `.jpg`, `.png` → `Images`
    - `.pdf`, `.docx` → `Documents`
    - `.mp4`, `.mov` → `Videos`
    - `.mp3`, `.wav` → `Music`
    - `.zip`, `.rar` → `Archives`
    - Unknown → `Others`

---

## 🧰 Technologies Used

- **Python**
- **Tkinter** (for GUI)
- **os** & **shutil** (for automation)

---

## 📂 Project Structure
📁 Downloads/
├── Images/
├── Documents/
├── Videos/
├── Music/
├── Archives/
└── Others/

---

## ⚙️ Setup Instructions

> ✅ Requires Python 3.8 or higher

### Step 1: Clone or Download the Project

You can manually download this project as a ZIP file and extract it.

Or, if using Git:
bash:
git clone https://github.com/AshleyMathias/File-Organizer-Tool.git
cd File-Organizer-Tool

### Step 2: Install Dependencies
pip install -r Requirments.txt

### Step 3: Run the Application
python main.py

---

###🙋‍♀️ About the Developer
Ashley Mathias
Python Developer & AI Enthusiast
Linkedin: ashleymathias10, Github: Ashley Mathias

---

<p align="center">
  Built with 💻 and ☕ by <strong>Ashley Mathias</strong>
</p>


