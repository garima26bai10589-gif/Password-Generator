# Password Generator

A simple, beginner-friendly command-line Password Generator developed as a first-year Python project following a **Python Essentials** course.

---

## 1. Project Title
**Password Generator**

## 2. Project Description
The **Password Generator** is an interactive, menu-driven terminal application written in Python. It allows users to create random passwords based on their preferred length and choice of character sets (uppercase letters, lowercase letters, numbers, and special symbols). 

The project demonstrates core Python fundamentals—including control flow, loops, functions, basic data structures, and standard library modules—without relying on any external packages or complex frameworks.

---

## 3. Objective
The primary objectives of this project are:
* To provide a tool for generating random passwords with customizable lengths and character types.
* To practice and demonstrate core Python programming topics learned in a Python Essentials course.
* To implement input validation to ensure the program runs smoothly without crashing on invalid user input.
* To structure code cleanly into modular, beginner-friendly functions that are easy to explain during a viva or project evaluation.

---

## 4. Features
* **Customizable Password Length**: Users can specify any desired length (minimum 4 characters, up to 100 characters).
* **Flexible Character Selection**:
  * Uppercase letters (`A-Z`)
  * Lowercase letters (`a-z`)
  * Digits (`0-9`)
  * Special characters (`!@#$%^&*...`)
* **Input Validation**:
  * Validates that password length is a positive integer.
  * Validates that at least one character category is selected.
  * Validates simple `yes`/`no` choices.
* **Continuous Execution**: Users can generate multiple passwords in a single session without having to restart the script.
* **Zero External Dependencies**: Built entirely with Python's built-in standard library (`random` and `string`).

---

## 5. Python Concepts Used

This project naturally applies concepts covered in the **Python Essentials** curriculum:

| Topic | Implementation in Project |
| :--- | :--- |
| **Python Fundamentals & Syntax** | Clean, readable syntax with variables and comments |
| **Input & Output Operations** | `input()` for reading user preferences; `print()` for menus and results |
| **Type Conversion** | Converting string input to integer using `int()` |
| **`type()` Function & Identity Operators** | Checking data type using `type(length) is not int` |
| **Assignment Operators** | `=`, `+=` (building the character pool string) |
| **Relational / Comparison Operators** | `<`, `>`, `==`, `!=`, `<=`, `>=` for range and choice checks |
| **Logical Operators** | `and`, `or`, `not` for validation conditions |
| **Membership Operators** | `in` and `not in` to validate choices in tuples and lists |
| **Control Flow Statements** | `if`, `elif`, `else` conditions, `while` loops, `for` loops, and `break` |
| **Data Structures** | **Tuple**: valid inputs `("yes", "y")`<br>**Dictionary**: storing user preferences `{"uppercase": True, ...}`<br>**List**: `character_list`, storing selected characters before joining |
| **Functions** | Modular decomposition: `get_password_length()`, `get_user_choices()`, `generate_password()`, `display_password()`, `main()` |
| **Modules & Packages** | Built-in standard library modules `random` and `string` |

---

## 6. Requirements
* **Python**: Version 3.8 or higher.
* **External Packages**: **None**. No external packages or `pip` installations are required.

---

## 7. Installation and Setup Instructions

Follow these simple steps to set up the project on your computer:

### Step 1: Ensure Python is Installed
Open your terminal or Command Prompt and check if Python is installed:
```bash
python --version
```
or on Windows:
```cmd
py --version
```
*(If Python is not installed, download it from [python.org](https://www.python.org/downloads/)).*

### Step 2: Download or Clone the Repository
Download the project files into a folder on your computer.

### Step 3: Navigate to the Project Folder
Open your terminal or Command Prompt and change directory to the project folder:
```bash
cd Password-Generator
```

---

## 8. How to Run the Program from the Terminal

Run the program with one of the following commands depending on your operating system:

### Windows:
```cmd
python password_generator.py
```
or
```cmd
py password_generator.py
```

### macOS / Linux:
```bash
python3 password_generator.py
```

---

## 9. Example Input and Output

### Example 1: Standard Generation
```text
========================================
PASSWORD GENERATOR
========================================

Enter password length: 10

Include uppercase letters? (yes/no): yes
Include lowercase letters? (yes/no): yes
Include numbers? (yes/no): yes
Include special characters? (yes/no): no

Generated Password: A7kLm92Qpx

Generate another password? (yes/no): no

Thank you for using Password Generator!
```

### Example 2: Handling Invalid Input & Selecting All Options
```text
========================================
PASSWORD GENERATOR
========================================

Enter password length: abc
Error: Invalid input! Please enter a positive whole number.

Enter password length: 2
Error: Password length must be at least 4. Please try again.

Enter password length: 12

Include uppercase letters? (yes/no): yes
Include lowercase letters? (yes/no): yes
Include numbers? (yes/no): yes
Include special characters? (yes/no): yes

Generated Password: 2,o1N,:@`QO^

Generate another password? (yes/no): no

Thank you for using Password Generator!
```

### Example 3: Handling No Character Types Selected
```text
========================================
PASSWORD GENERATOR
========================================

Enter password length: 8

Include uppercase letters? (yes/no): no
Include lowercase letters? (yes/no): no
Include numbers? (yes/no): no
Include special characters? (yes/no): no

Error: You must select at least one character type! Please try again.

Include uppercase letters? (yes/no): yes
Include lowercase letters? (yes/no): yes
Include numbers? (yes/no): yes
Include special characters? (yes/no): no

Generated Password: f49pQLw7

Generate another password? (yes/no): no

Thank you for using Password Generator!
```

---

## 10. Project Structure

```text
Password-Generator/
│
├── README.md               # Project documentation and instructions
├── password_generator.py   # Main Python source code
├── requirements.txt        # Dependency statement (standard library only)
└── project_report.md       # Complete academic project report
```

---

## 11. Limitations
* **Educational Scope**: Built for educational demonstration, not for enterprise-grade cryptographic secrets.
* **Terminal Interface Only**: Runs exclusively in a command-line interface; no graphical user interface (GUI).
* **No Permanent Storage**: Does not store or save generated passwords to any file or database.
* **No Clipboard Integration**: The generated password must be manually highlighted and copied from the terminal.

---

## 12. Future Improvements
* Add a **password strength indicator** (Weak, Medium, Strong) based on character diversity and length.
* Add an option to **exclude ambiguous characters** (such as `l`, `1`, `I`, `0`, `O`) to avoid visual confusion.
* Add an optional feature to **export generated passwords** to a local text file.
* Add a feature to copy the generated password directly to the operating system clipboard.

---

## Important Security Note
> **Educational Disclaimer**: This project is developed strictly for educational and learning purposes. It does not include password encryption, cryptographic hashing, database storage, multi-factor authentication, or enterprise-level security protocols.
