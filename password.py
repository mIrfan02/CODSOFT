import random
import string

def generate_password(length):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    characters = lowercase_letters + uppercase_letters + digits + special_characters


    password = ''.join(random.choice(characters) for _ in range(length))

    return password

def main():
    print("Password Generator")
    try:
        length = int(input("Enter the desired password length: "))
        if length < 1:
            print("Password length must be at least 1.")
        else:
            password = generate_password(length)
            print(f"Generated Password: {password}")
    except ValueError:
        print("Invalid input. Please enter a valid integer for password length.")

if __name__ == "__main__":
    main()
