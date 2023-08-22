# 1 WAP to check if the given contact number is valid or invalid using regular expressions


import re


def is_valid_contact_number(number):
    # Regular expression pattern to match valid contact numbers

    pattern = r'^(\+?\d{1,2})?[-.\s]?(\d{3})?[-.\s]?(\d{3})[-.\s]?(\d{4})$'

    if re.match(pattern, number):
        return True
    else:
        return False


# List of example contact numbers
contact_numbers = [
    "2124567890",
    "212-456-7890",
    "(212)456-7890",
    "(212)-456-7890",
    "212.456.7890",
    "212 456 7890",
    "+12124567890",
    "+1 212.456.7890",
    "+212-456-7890",
    "1-212-456-7890"
]

for number in contact_numbers:
    if is_valid_contact_number(number):
        print(f"{number} is a valid contact number.")
    else:
        print(f"{number} is an invalid contact number.")
