"""
Password Generator
Author: First-Year Student
Course: Python Essentials
Description: A simple command-line program that generates random passwords
based on user-specified length and character preferences.
"""

import random
import string


def get_password_length():
    """
    Prompt the user for password length and validate it.
    Ensures the input is a positive integer of at least 4 characters.
    """
    while True:
        length_input = input("Enter password length: ").strip()

        # Check if the input consists of digits only
        if length_input.isdigit():
            length = int(length_input)

            # Check minimum and maximum boundaries
            if length < 4:
                print("Error: Password length must be at least 4. Please try again.\n")
            elif length > 100:
                print("Error: Password length cannot exceed 100. Please try again.\n")
            else:
                return length
        else:
            print("Error: Invalid input! Please enter a positive whole number.\n")


def get_user_choices():
    """
    Prompt user for character preferences (uppercase, lowercase, numbers, special characters).
    Validates that user chooses at least one character type.
    Returns choices stored in a dictionary.
    """
    # Tuple of acceptable answers
    valid_yes = ("yes", "y")
    valid_no = ("no", "n")

    while True:
        # Uppercase choice
        upper_input = input("Include uppercase letters? (yes/no): ").strip().lower()
        while upper_input not in valid_yes and upper_input not in valid_no:
            print("Please enter 'yes' or 'no'.")
            upper_input = input("Include uppercase letters? (yes/no): ").strip().lower()

        # Lowercase choice
        lower_input = input("Include lowercase letters? (yes/no): ").strip().lower()
        while lower_input not in valid_yes and lower_input not in valid_no:
            print("Please enter 'yes' or 'no'.")
            lower_input = input("Include lowercase letters? (yes/no): ").strip().lower()

        # Numbers choice
        num_input = input("Include numbers? (yes/no): ").strip().lower()
        while num_input not in valid_yes and num_input not in valid_no:
            print("Please enter 'yes' or 'no'.")
            num_input = input("Include numbers? (yes/no): ").strip().lower()

        # Special characters choice
        special_input = input("Include special characters? (yes/no): ").strip().lower()
        while special_input not in valid_yes and special_input not in valid_no:
            print("Please enter 'yes' or 'no'.")
            special_input = input("Include special characters? (yes/no): ").strip().lower()

        # Convert responses to booleans
        include_upper = upper_input in valid_yes
        include_lower = lower_input in valid_yes
        include_numbers = num_input in valid_yes
        include_special = special_input in valid_yes

        # Logical check: at least one character type must be selected
        if include_upper or include_lower or include_numbers or include_special:
            # Store choices in a dictionary
            choices = {
                "uppercase": include_upper,
                "lowercase": include_lower,
                "numbers": include_numbers,
                "special": include_special
            }
            return choices
        else:
            print("\nError: You must select at least one character type! Please try again.\n")


def generate_password(length, choices):
    """
    Generate a random password of given length using the selected character types.
    """
    # Verify parameter type using type() function and identity operator
    if type(length) is not int:
        length = int(length)

    # Build character pool based on user choices
    character_pool = ""

    if choices["uppercase"]:
        character_pool += string.ascii_uppercase

    if choices["lowercase"]:
        character_pool += string.ascii_lowercase

    if choices["numbers"]:
        character_pool += string.digits

    if choices["special"]:
        # Standard special punctuation characters
        character_pool += string.punctuation

    # Convert character pool string into a list
    character_list = list(character_pool)

    # Randomly select characters until desired length is reached
    password_chars = []
    for _ in range(length):
        random_char = random.choice(character_list)
        password_chars.append(random_char)

    # Join list of characters into a single string
    password = "".join(password_chars)
    return password


def display_password(password):
    """
    Display the generated password to the user.
    """
    print("\nGenerated Password: " + password)


def main():
    """
    Main function to control program execution flow.
    """
    print("========================================")
    print("PASSWORD GENERATOR")
    print("========================================")
    print()

    while True:
        # Step 1: Get validated password length
        length = get_password_length()
        print()

        # Step 2: Get user character preferences
        choices = get_user_choices()

        # Step 3: Generate the password
        password = generate_password(length, choices)

        # Step 4: Display the result
        display_password(password)

        # Step 5: Ask if user wants to generate another password
        print()
        again = input("Generate another password? (yes/no): ").strip().lower()
        while again not in ("yes", "y", "no", "n"):
            print("Please enter 'yes' or 'no'.")
            again = input("Generate another password? (yes/no): ").strip().lower()

        if again in ("no", "n"):
            print("\nThank you for using Password Generator!")
            break
        print()


if __name__ == "__main__":
    main()
