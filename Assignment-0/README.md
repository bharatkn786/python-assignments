# Assignment (0) - Python Version

## Problem Statement

Run a program that uses a latest Python feature which works in **Python 3.11+** but does **not** work in lower versions. Demonstrate how to install multiple Python versions and switch between them seamlessly.

## Python Versions Used

- Python 3.11
- Python 3.8

## Feature Demonstrated

### 1. Match-Case Statement
- Supported in **Python 3.11**
- Produces a **SyntaxError** in **Python 3.8**

### 2. ExceptionGroup (`except*`)
- Works correctly in **Python 3.11*
- Produces a **SyntaxError** in **Python 3.8**

## Version Switching

Separate virtual environments were created for Python 3.8 and Python 3.11 using `venv`, allowing seamless switching between versions.

venv3.8 for python version 3.8 and venv3.11 for python version 3.11

## Screenshots

The repository includes screenshots showing:

<img width="732" height="238" alt="Screenshot 2026-08-04 175104" src="https://github.com/user-attachments/assets/66d18448-1a04-4003-8af1-2f622ab28599" />

- Installation of multiple Python versions

##
                     Example 1(Match-Case Statement)
<img width="1032" height="500" alt="Screenshot 2026-08-04 175452" src="https://github.com/user-attachments/assets/5068a426-393f-4475-9afc-842e23423c8d" />
  
- Creating and activating virtual environments and Running the program in Python 3.11


  <img width="1361" height="708" alt="Screenshot 2026-08-04 175529" src="https://github.com/user-attachments/assets/5e3aa090-beaf-40a3-a00f-604970bd4530" />

- Running the same program in Python 3.8 and observing the syntax error



##
                     Example 2(ExceptionGroup (`except*`))
             
<img width="1527" height="767" alt="Screenshot 2026-08-04 175803" src="https://github.com/user-attachments/assets/2180679c-94e2-47cc-bf7a-30263b5b696b" />

- Creating and activating virtual environments and Running the program in Python 3.11


  <img width="1536" height="723" alt="Screenshot 2026-08-04 175728" src="https://github.com/user-attachments/assets/b7f6c91f-5cad-4a77-ad8e-d3609c95ec71" />


- Running the same program in Python 3.8 and observing the syntax error

# 🐧 GitHub Deployment using Ubuntu (WSL)

This assignment was pushed to GitHub using the **Ubuntu 22.04 LTS (WSL)** terminal instead of Windows PowerShell.

The workflow included:

- Navigating to the project using Linux commands.
- Initializing the Git repository.
- Adding the GitHub remote.
- Committing the project.
- Authenticating using a GitHub Personal Access Token (PAT).
- Successfully pushing the project to GitHub from Ubuntu (WSL).

### Successful Git Push from Ubuntu (WSL)

<img width="1520" height="676" alt="Screenshot 2026-08-05 135611" src="https://github.com/user-attachments/assets/6965d263-a95c-42e7-876c-1342043bc4a8" />


<!-- Add your Linux Git Push screenshot here -->

---
##  Conclusion

This assignment demonstrates:

- Installing and managing multiple Python versions.
- Creating version-specific virtual environments.
- Using Python 3.11 language features and comparing them with Python 3.8.
- Switching seamlessly between Python versions.
- Successfully managing the project using Git and GitHub.
- Deploying the project from **Ubuntu (WSL)** using Linux command-line tools.
