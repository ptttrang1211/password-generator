import string
import random

LETTERS = string.ascii_letters
NUMBERS = string.digits
PUNCTUATION = string.punctuation


def password_generator_auto(password_length):
    if password_length < 8:
        raise ValueError("Password must be at least 8 character security.\n")
    printable = f'{LETTERS}{NUMBERS}{PUNCTUATION}'
    printable = list(printable)
    random.shuffle(printable)
    random_password = ''.join(random.choices(printable, k=password_length))
    return random_password


def password_generator_custom(n_letters, n_numbers, n_punctuation):
    total_lenght = n_letters + n_numbers + n_punctuation
    if total_lenght < 8:
        raise ValueError("Password must be at least 8 character security.\n")
    letters_part = random.choices(LETTERS, k=n_letters)
    numbers_part = random.choices(NUMBERS, k=n_numbers)
    punctuation_part = random.choices(PUNCTUATION, k=n_punctuation)

    total_password = letters_part + numbers_part + punctuation_part
    random.shuffle(total_password)

    return ''.join(total_password)


def main():
    print("=======Password Generator=======")
    while True:
        print("1.Password generator auto ")
        print("2. Password generator custom ")
        choice = input(" Choose 1 or 2: ")
        if choice == "1":
            while True:
                try:
                    password_length = int(input("How long do you want your password\n"))
                    password = password_generator_auto(password_length)
                    break
                except ValueError as e:
                    print (e)
            break
        elif choice == "2":
            while True:
                try:
                    n_letters = int(input("How many letters you want in your password?\n"))
                    n_numbers = int(input("How many number you want in your password?\n"))
                    n_punctuation = int(input("How long punctuation you want in your password?\n"))
                    password = password_generator_custom(n_letters, n_numbers, n_punctuation)
                    break
                except ValueError as e:
                    print(e)
            break
        else:
            print("Invalid choice. Please try again.\n")
    print("Generated password: ", password)


if __name__ == '__main__':
    main()
