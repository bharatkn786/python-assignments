#  Week 1 - Lab 1: Project and Environment Setup

## Objective

Set up a Python development environment by creating a project structure, configuring a virtual environment, and running the Python Program.



---

## Environment

- **Operating System:** Ubuntu 22.04 LTS (WSL)
- **Python Version:** 3.11.15
- **Virtual Environment:** venv
- **Editor:** Visual Studio Code

---
## Project Update

- The project folder was initially created as **`week1-foundations`**.
- Before pushing it to Github, it was renamed to **`week1-lab1`** to maintain a consistent naming convention across all assignments and labs.

## Project Structure

```text
week1-lab1/
│
├── .venv/
├── main.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Steps Performed

- Installed Python **3.11** on Ubuntu (WSL).
- Created and activated a virtual environment.
- Verified the installed Python version.
- Created the required project files.
- Executed the Python program inside the virtual environment.
- Generated the `requirements.txt` file.
- Configured `.gitignore` to exclude the virtual environment.

---

## Linux Commands Used

### Install Python 3.11

```bash
sudo apt update
sudo apt install python3.11
sudo apt install python3.11-venv
```

### Create and Activate Virtual Environment

```bash
python3.11 -m venv .venv
source .venv/bin/activate
```

### Verify Python Version

```bash
python3.11 --version
```

### Run the Program

```bash
python main.py
```

### Generate Requirements

```bash
pip freeze > requirements.txt
```

---

# Screenshots

## 1. Installing Python 3.11

<img width="1535" height="647" alt="Screenshot 2026-08-05 171910" src="https://github.com/user-attachments/assets/2af43600-ff2b-444c-8fd0-7959dfe944ec" />


---

## 2. Creating and Activating the Virtual Environment

<img width="1536" height="367" alt="Screenshot 2026-08-05 171930" src="https://github.com/user-attachments/assets/20e43ade-74b7-4f02-93d2-07a75ab268f0" />



---

## 3. Project Structure

<img width="1536" height="537" alt="Screenshot 2026-08-05 172009" src="https://github.com/user-attachments/assets/1a95c147-86e9-4ebd-9c98-42eb1f5fdc05" />


---

## 4. Running the Program

<img width="1536" height="510" alt="Screenshot 2026-08-05 172047" src="https://github.com/user-attachments/assets/b7b90af2-bf66-4640-baba-0427a4e163e9" />


---
---

## Challenges Faced

During the setup, I encountered a few issues:

1. **Virtual environment creation failed initially**
   - While creating the virtual environment, I encountered an `ensurepip` error because the `python3.11-venv` package was not installed. Installing the required package resolved the issue.

2. **Learning Linux commands**
   - Since I was setting up the project entirely through Ubuntu (WSL), I familiarized myself with Linux commands for creating files, managing directories, creating virtual environments, and running Python programs.

---

Through this lab, I learned how to:

- Install Python on Ubuntu (WSL).
- Create and manage virtual environments.
- Execute Python programs from the Linux terminal.
- Generate a `requirements.txt` file.
- Organize a Python project using a standard directory structure.
- Prepare a project for version control using Git and GitHub.
