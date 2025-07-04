# 📝 Simple Command-Line To-Do List App

This is a beginner-friendly **Python command-line To-Do list application**.  
It allows you to add, view, and delete (check off) tasks — and it automatically saves your tasks to a local `.txt` file so you never lose your progress.

---

## 🚀 Features

- ✅ Add tasks
- ❌ Delete / check-off tasks
- 💾 Automatically save and load tasks from `tasks.txt`
- 📃 Simple numbered task display
- 🔁 Menu-driven loop that runs until you quit

---

## 🧠 How It Works

- The app reads tasks from `tasks.txt` on startup.
- It presents a menu with options to:
  1. Add a new task
  2. Delete a task
  3. Quit and save
- Tasks are stored in memory as a list of strings and saved back to `tasks.txt` when quitting.

---

## 💻 How to Run

1. Make sure you have Python 3 installed.
2. Clone this repo or copy the script into a `.py` file.
3. Open a terminal and run:

```bash
python3 main.py
