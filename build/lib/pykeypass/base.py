import random
import string

def generate_password(length=12, uppercase=False, lowercase=True, numbers=True, special=False):
    characters = ""

    if uppercase:
        characters += string.ascii_uppercase

    if lowercase:
        characters += string.ascii_lowercase

    if numbers:
        characters += string.digits

    if special:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character type should be selected for the password.")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    try:
        length = int(input("Enter the password length: "))
        uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
        numbers = input("Include numbers? (y/n): ").lower() == 'y'
        special = input("Include special characters? (y/n): ").lower() == 'y'

        password = generate_password(length, uppercase, lowercase, numbers, special)
        print("Generated Password:", password)
    except ValueError as e:
        print(e)
