import random
import string

def get_length():
    while True:
        length = int(input("Enter password length (minimum 4): "))
        if length >= 4:
            return length
        print("Password length should be at least 4.")

def generate_password(length):
    upper = random.choice(string.ascii_uppercase)
    lower = random.choice(string.ascii_lowercase)
    digit = random.choice(string.digits)
    special = random.choice(string.punctuation)

    remaining = length - 4
    others = random.choices(
        string.ascii_letters + string.digits + string.punctuation,
        k=remaining
    )

    password = list(upper + lower + digit + special + ''.join(others))
    random.shuffle(password)

    return ''.join(password)

def display_password(password):
    print("\nGenerated Password:", password)

def main():
    print("===== PASSWORD GENERATOR =====")

    while True:
        length = get_length()
        password = generate_password(length)
        display_password(password)

        choice = input("\nGenerate another password? (y/n): ").lower()

        if choice != 'y':
            print("Thank You...!")
            break
main()
