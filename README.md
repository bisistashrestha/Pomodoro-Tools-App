# Pomodoro Productivity App

**File:** main.py  
**Author:** Bisista Shrestha  
**Date:** 2024-06-27  
**License:** MIT License (see [LICENSE](LICENSE) file)  

---

## Overview
This is a **desktop productivity app** built using **CustomTkinter**. It combines three essential tools into one interface:  

1. **Pomodoro Timer** – Focused work sessions with configurable breaks.  
2. **Task Manager** – Add, edit, and remove tasks with persistence.  
3. **Notepad** – Take notes and save them for each user.  

The app supports **multi-user accounts**, saves tasks and notes to a local database (`data.db`), and tracks completed Pomodoro sessions.  

---

## Features
- **Multi-user support**: Separate tasks and notes for each username.  
- **Pomodoro timer**: Track focused work and take short/long breaks.  
- **Task persistence**: Tasks are saved automatically to `data.db`.  
- **Editable tasks**: Add, edit, and delete tasks dynamically.  
- **Notepad**: Simple in-app notepad for personal notes.  
- **Session tracking**: Counts the number of Pomodoro sessions completed.  
- **User-friendly interface**: Built with CustomTkinter for a modern look.  

---

## Installation
1. Clone the repository:  
git clone https://github.com/bisistashrestha/Pomodoro-Tools-App.git

2. Navigate to the project folder:  
cd [<project-folder>]

3. Create a virtual environment:  
python -m venv myenv

4. Activate the environment:  
- **Windows:** `myenv\Scripts\activate`  
- **Linux/macOS:** `source myenv/bin/activate`

5. Install dependencies:  
pip install -r requirements.txt


python main.py
---

## Usage
1. Enter a **username** and click **Enter**.  
2. Use the **Pomodoro timer** to start a focus session.  
3. Add tasks via the **Task Manager**, or edit/remove them as needed.  
4. Take notes in the **Notepad**, which saves automatically.  
5. Switch between **Pomodoro**, **Short Break**, and **Long Break** modes.  

---

## License
This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

