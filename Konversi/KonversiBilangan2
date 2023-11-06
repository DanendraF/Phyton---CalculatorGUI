import os
from enum import Enum

# Enumerate the base numbers (Numerasi menu otomatis).
class Base(Enum):
    DECIMAL = 1
    BINARY = 2
    OCTAL = 3
    HEXADECIMAL = 4
    ASCII = 5

# Clears the command prompt (Clearing di terminal).
def clear_cmd():
    os.system("cls") if os.name == "nt" else os.system("clear")

# Prints a separator line (Separator line pada menu dan title).
def separator():
    print("-" * 40)

# Prints the application title (Title pada menu).
def title():
    clear_cmd()
    separator()
    print("Simple Number Convertion with Python")
    separator()

# Prints the menu options (Menu options).
def menu():
    title()
    for base in Base:
        print(f"{base.value}. {base.name}")
    print(f"{len(Base) + 1}. EXIT")
    separator()

# Prompts the user for input data (Input data).
def get_input(base):
    title()
    data = input(f"Input your {base.name.lower()} number or word : ")
    if not data:
        raise ValueError(f"{base.name.lower()} number is required")
    return data

# Handles errors and prompts the user to continue or exit (Error handling pada konversi).
def error(err):
    separator()
    print(f"System error : {err}")
    separator()
    choice = input("Do you want to continue? [yes/no] : ")
    if choice.lower() in ["yes", "y"]:
        return True
    elif choice.lower() in ["no", "n"]:
        logic()
    else:
        return error("Invalid choice")

# Converts the input data to decimal and other bases (Logika pada konversi).
def convertion(base, data):
    try:
        if base == Base.DECIMAL:
            decimal = int(data)
        elif base == Base.BINARY:
            decimal = int(data, 2)
        elif base == Base.OCTAL:
            decimal = int(data, 8)
        elif base == Base.HEXADECIMAL:
            decimal = int(data, 16)
        elif base == Base.ASCII:
                """Convert string to array."""
                decimal = [ord(character) for character in data]

                """Convert array to other bases."""
                binary = ' '.join([bin(character)[2:] for character in decimal])
                octal = ' '.join([oct(character)[2:] for character in decimal])
                hexadecimal = ' '.join([hex(character)[2:] for character in decimal])
                asci = ''.join([chr(character) for character in decimal])

                """Convert array to decimal."""
                decimal = ' '.join([str(character) for character in decimal])

                """Return the result."""
                return [decimal, binary, octal, hexadecimal, asci]
        """Convert decimal to other bases."""
        binary = bin(decimal)[2:]
        octal = oct(decimal)[2:]
        hexadecimal = hex(decimal)[2:]
        asci = chr(decimal)

        """Return the result."""
        return [decimal, binary, octal, hexadecimal, asci]
    except ValueError as valErr:
        error(valErr)
    except TypeError as typeErr:
        error(typeErr)
    except Exception as err:
        error(err)
    """Return the result."""
    return main(base)

# Prompts the user to retry or exit (Percabangan retry dan exit).
def retry(base):
    choice = input("Do you want to try again? [yes/no] : ")
    separator()
    if choice.lower() in ["yes", "y"]:
        main(base)
    elif choice.lower() in ["no", "n"]:
        logic()
    else:
        error("Invalid choice")
        return retry(base)

# Main logic (Tampilan output konversi).
def main(base):
    try:
        data = get_input(base)
        conversions = convertion(base, data)
        separator()
        print(f"Decimal     : {conversions[0]}")
        print(f"Binary      : {conversions[1]}")
        print(f"Octal       : {conversions[2]}")
        print(f"Hexadecimal : {conversions[3]}")
        print(f"ASCII       : {conversions[4]}")
        separator()
        retry(base)
    except ValueError as err:
        error(err)
        main(base)

# Initial Logic (Logika output pada menu).
def logic():
    menu()
    select = input('Select your output : ')
    separator()
    if select == str(len(Base) + 1):
        exit()
    elif select not in [str(base.value) for base in Base]:
        error("Invalid choice")
    else:
        main(Base(int(select)))

# Run the application.
logic()