# ACADEMIC PROJECT REPORT

## PROJECT TITLE: PASSWORD GENERATOR

* **Course**: Python Essentials
* **Level**: First-Year Undergraduate
* **Language**: Python 3
* **Project Type**: Command-Line Application

---

## 1. INTRODUCTION

In today's digital world, computer security is an important topic. Most online accounts, school portals, and digital services require a password to protect user information. However, many users create passwords that are easy to guess, such as their birthdate, pet's name, or simple sequences like "123456" and "password". Such weak passwords make accounts vulnerable to unauthorized access.

A reliable way to create strong passwords is to use a password generator that randomly selects a mix of uppercase letters, lowercase letters, numbers, and special symbols. 

This project, titled **Password Generator**, is a simple command-line program created as part of a first-year Python programming course. It allows users to create random passwords based on their preferred length and character types. The project applies foundational programming concepts such as variables, conditionals, loops, functions, and standard library modules.

---

## 2. PROBLEM STATEMENT

Creating a secure password manually can be challenging because human beings tend to choose familiar words or predictable patterns. Moreover, different websites have different password requirements (for example, some require special characters, while others only accept letters and digits). 

There is a need for a lightweight, easy-to-use tool that allows a user to:
1. Specify the exact length of the password needed.
2. Select which character types should be included.
3. Automatically generate an unpredictable, random password.
4. Ensure that invalid inputs are handled gracefully without the program crashing.

---

## 3. OBJECTIVES

The main objectives of this project are:
1. To build an interactive, menu-driven command-line password generator using Python.
2. To allow users to select password length (between 4 and 100 characters).
3. To provide options for including uppercase letters, lowercase letters, numbers, and special characters.
4. To validate all user inputs (ensuring correct integer input and that at least one character type is chosen).
5. To demonstrate understanding of the topics taught in the Python Essentials course.
6. To keep the code clean, modular, and easy to explain during a viva or practical examination.

---

## 4. SCOPE

* **Target Users**: Students, beginners, and individuals looking for a simple tool to generate quick passwords.
* **Platform**: Any platform with Python 3 installed (Windows, macOS, Linux).
* **Environment**: Runs entirely in the terminal / command prompt.
* **Limitations of Scope**: This is an educational project. It does not connect to the internet, does not store passwords in a database, and does not provide cryptographic enterprise-level security.

---

## 5. TECHNOLOGIES USED

* **Programming Language**: Python 3 (Tested on Python 3.14 / 3.8+)
* **Standard Library Modules**:
  * `random`: Used to randomly pick characters from the available character pool (`random.choice`).
  * `string`: Used to obtain standard character sets (`ascii_uppercase`, `ascii_lowercase`, `digits`, `punctuation`).
* **External Dependencies**: None. Only built-in Python tools are used.

---

## 6. PYTHON CONCEPTS USED

The project applies key concepts from the Python Essentials syllabus:

1. **Variables and Assignment Operators**:
   * Storing user inputs, lengths, lists, and character sets using `=` and `+=`.
2. **Input and Output Operations**:
   * Using `input()` to receive user inputs from the console.
   * Using `print()` to display menus, prompts, error messages, and the final password.
3. **Type Conversion**:
   * Converting string input to an integer using `int()` for password length.
4. **The `type()` Function & Identity Operators**:
   * Verifying that the length variable is an integer using `type(length) is not int`.
5. **Relational / Comparison Operators**:
   * Checking boundaries (`length < 4`, `length > 100`) and matching values (`==`, `!=`).
6. **Logical Operators (`and`, `or`, `not`)**:
   * Checking compound conditions (e.g., verifying whether at least one character type was selected: `include_upper or include_lower or include_numbers or include_special`).
7. **Membership Operators (`in`, `not in`)**:
   * Checking if the user's input belongs to a valid response tuple (`upper_input in valid_yes`).
8. **Control-Flow Statements**:
   * `if`, `elif`, and `else` for condition branching.
   * `while` loops for input validation and program repeat loops.
   * `for` loop to repeat random character selection until the specified length is reached.
   * `break` statement to exit loops.
9. **Core Data Structures**:
   * **Tuple**: `valid_yes = ("yes", "y")` to store immutable valid options.
   * **Dictionary**: `choices = {"uppercase": ..., "lowercase": ...}` to store structured user options.
   * **List**: `character_list = list(character_pool)` and `password_chars = []` to store and append characters.
10. **Functions**:
    * Dividing the project into clear, single-responsibility functions.
11. **Modules**:
    * Importing and using Python's built-in `random` and `string` modules.

---

## 7. METHODOLOGY

The development follows a **procedural, modular programming** approach:
1. **Requirement Analysis**: Identifying user inputs (length, character options) and output (generated password).
2. **Modular Decomposition**: Breaking down the program into small functions:
   * Getting and validating length.
   * Getting and validating character choices.
   * Assembling the character pool and selecting random characters.
   * Displaying the generated password.
   * Managing the overall flow in a `main()` loop.
3. **Input Validation Strategy**:
   * Using `.isdigit()` to prevent errors when users type text instead of numbers.
   * Using `.strip().lower()` so inputs like `" YES "` or `"No"` are processed correctly.
   * Forcing the user to re-enter choices if all character types are marked "no".
4. **Testing and Verification**:
   * Running test cases with varying lengths, mixed choices, and intentional input errors.

---

## 8. ALGORITHM

1. Start the program.
2. Display the project title and welcome header.
3. Prompt the user to enter the desired password length.
4. Check if the length is a positive integer between 4 and 100. If invalid, display an error message and repeat step 3.
5. Prompt the user whether to include uppercase letters (`yes`/`no`).
6. Prompt the user whether to include lowercase letters (`yes`/`no`).
7. Prompt the user whether to include numbers (`yes`/`no`).
8. Prompt the user whether to include special characters (`yes`/`no`).
9. Check if at least one character category was chosen. If none was selected, show an error message and repeat steps 5 to 8.
10. Combine the selected character sets into a character pool.
11. Convert the character pool into a list of characters.
12. Use a loop that runs `length` times, picking a random character from the list in each iteration.
13. Join the selected characters to form the final password string.
14. Display the generated password.
15. Ask the user if they wish to generate another password.
16. If "yes", repeat from step 3; if "no", display a thank-you message and end the program.

---

## 9. STEP-BY-STEP WORKING

1. **Initialization**: When executed, `main()` prints the program title banner.
2. **Length Input**: `get_password_length()` asks for input. If the user types non-numeric characters (e.g., `"abc"`), the program notifies the user and asks again. If the number is below 4, it asks again.
3. **Preferences Input**: `get_user_choices()` asks four yes/no questions. It stores the boolean results in a dictionary.
4. **Validation Check**: If all four answers are "no", the program prints:
   `Error: You must select at least one character type! Please try again.`
   and prompts the user again.
5. **Character Pool Creation**: `generate_password()` checks the dictionary. Depending on the `True` values, it appends constants from the `string` module (`ascii_uppercase`, `ascii_lowercase`, `digits`, `punctuation`) to `character_pool`.
6. **Random Selection**: Using `random.choice(character_list)` inside a `for` loop that runs `length` times, characters are appended to a list `password_chars`.
7. **Joining**: `"".join(password_chars)` converts the list of characters back into a string.
8. **Display**: `display_password()` displays the generated password to the screen.
9. **Repetition**: The program asks `Generate another password? (yes/no): `. If user enters `no`, the loop breaks and the program exits gracefully.

---

## 10. FUNCTIONS USED

### 1. `get_password_length()`
* **Purpose**: Solicits the password length from the user.
* **Validation**: Uses `str.isdigit()` to ensure the input is numeric and verifies that `4 <= length <= 100`.
* **Return Value**: An integer representing valid password length.

### 2. `get_user_choices()`
* **Purpose**: Collects preferences for uppercase, lowercase, numbers, and special characters.
* **Validation**: Ensures user provides valid yes/no responses and selects at least one category.
* **Return Value**: A dictionary containing boolean values for `"uppercase"`, `"lowercase"`, `"numbers"`, and `"special"`.

### 3. `generate_password(length, choices)`
* **Parameters**: 
  * `length` (int): Number of characters required.
  * `choices` (dict): Dictionary with boolean flags for character sets.
* **Purpose**: Builds the pool of available characters and randomly picks `length` characters.
* **Return Value**: A randomly generated password string.

### 4. `display_password(password)`
* **Parameters**: `password` (str).
* **Purpose**: Neatly prints the generated password to the console.

### 5. `main()`
* **Purpose**: Serves as the driver function that coordinates the execution of the other functions and manages the program loop.

---

## 11. SAMPLE INPUT AND OUTPUT

### Test Case 1: Standard Generation (Length = 8, No Special Characters)
**Input:**
* Length: `8`
* Uppercase: `yes`
* Lowercase: `yes`
* Numbers: `yes`
* Special Characters: `no`
* Generate another: `no`

**Output:**
```text
========================================
PASSWORD GENERATOR
========================================

Enter password length: 8

Include uppercase letters? (yes/no): yes
Include lowercase letters? (yes/no): yes
Include numbers? (yes/no): yes
Include special characters? (yes/no): no

Generated Password: f49pQLw7

Generate another password? (yes/no): no

Thank you for using Password Generator!
```

---

### Test Case 2: 12-Character Password with All Character Types
**Input:**
* Length: `12`
* Uppercase: `yes`
* Lowercase: `yes`
* Numbers: `yes`
* Special Characters: `yes`
* Generate another: `no`

**Output:**
```text
========================================
PASSWORD GENERATOR
========================================

Enter password length: 12

Include uppercase letters? (yes/no): yes
Include lowercase letters? (yes/no): yes
Include numbers? (yes/no): yes
Include special characters? (yes/no): yes

Generated Password: 2,o1N,:@`QO^

Generate another password? (yes/no): no

Thank you for using Password Generator!
```

---

### Test Case 3: Invalid Length Handling
**Input:**
* Length: `abc` (text)
* Length: `2` (too short)
* Length: `10` (valid)
* Uppercase: `yes`
* Lowercase: `yes`
* Numbers: `yes`
* Special Characters: `no`
* Generate another: `no`

**Output:**
```text
========================================
PASSWORD GENERATOR
========================================

Enter password length: abc
Error: Invalid input! Please enter a positive whole number.

Enter password length: 2
Error: Password length must be at least 4. Please try again.

Enter password length: 10

Include uppercase letters? (yes/no): yes
Include lowercase letters? (yes/no): yes
Include numbers? (yes/no): yes
Include special characters? (yes/no): no

Generated Password: 2YEQ9omFf4

Generate another password? (yes/no): no

Thank you for using Password Generator!
```

---

### Test Case 4: Rejection when All Character Types are "no"
**Input:**
* Length: `10`
* First attempt: `no`, `no`, `no`, `no`
* Second attempt: `yes`, `yes`, `yes`, `no`
* Generate another: `no`

**Output:**
```text
========================================
PASSWORD GENERATOR
========================================

Enter password length: 10

Include uppercase letters? (yes/no): no
Include lowercase letters? (yes/no): no
Include numbers? (yes/no): no
Include special characters? (yes/no): no

Error: You must select at least one character type! Please try again.

Include uppercase letters? (yes/no): yes
Include lowercase letters? (yes/no): yes
Include numbers? (yes/no): yes
Include special characters? (yes/no): no

Generated Password: HJGfM0fqcY

Generate another password? (yes/no): no

Thank you for using Password Generator!
```

---

## 12. ADVANTAGES

* **Easy to Understand**: The code uses basic, clear syntax suitable for a beginner.
* **No Dependencies**: Runs using standard Python without requiring `pip install`.
* **Reliable Input Validation**: Handles invalid numbers and answers without raising unhandled errors or crashing.
* **Customizable**: Allows users to tailor passwords to specific website requirements.
* **Modular Code Structure**: Organized into discrete functions that can be tested independently.

---

## 13. LIMITATIONS

* **Terminal Only**: Does not have a graphical user interface (GUI).
* **Pseudo-Random Generator**: Uses Python's standard `random` module, which is suitable for general use and education, but not for high-security cryptographic secrets.
* **No Storage**: Does not store or log passwords. Once the terminal is closed, the generated password is lost unless copied.
* **Manual Copying**: The user must manually highlight and copy the generated password from the terminal.

---

## 14. FUTURE SCOPE

* **Password Strength Checker**: Evaluate and display password strength (e.g., Weak, Medium, Strong) based on length and variety.
* **Exclude Ambiguous Characters**: Give the user an option to exclude easily confused characters (like `O` and `0`, `l` and `1`).
* **Clipboard Support**: Automatically copy the generated password to the system clipboard.
* **Export Feature**: Provide an option to save the generated password into a local text file.
* **Graphical Interface**: Create a simple graphical user interface using Tkinter after learning GUI topics in later semesters.

---

## 15. CONCLUSION

The **Password Generator** project successfully fulfills all objectives set out for a first-year Python project. By combining user input handling, conditional validation, iterative loops, functions, and standard library modules (`random` and `string`), the program delivers a functional, user-friendly utility. 

This project reinforces fundamental programming knowledge acquired during the Python Essentials course and serves as a solid foundation for more advanced programming concepts in future studies.

---

## 16. IMPORTANT SECURITY NOTE
> **Disclaimer**: This is an educational project designed for academic demonstration. It does not provide password hashing, cryptographic encryption, multi-factor authentication, or enterprise-level security.
