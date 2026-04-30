import random
import string

print("===== PASSWORD GENERATOR =====")

while True:
    try:
        length = int(input("Enter password length: "))

        if length <= 0:
            print("Please enter a valid length!")
            continue

        # characters mix
        characters = string.ascii_letters + string.digits + string.punctuation

        # generate password
        password = ''.join(random.choice(characters) for _ in range(length))

        print("Generated Password:", password)

    except ValueError:
        print("Invalid input! Enter a number.")

    # ask again
    again = input("Generate another password? (yes/no): ").lower()
    if again != 'yes':
        print("Exiting... 👋")
        break