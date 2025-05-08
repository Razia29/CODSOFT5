import random
import string

def generate_password():
    print("Password Generator")
    print("------------------")

    # Prompt user for password length
    try:
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            print("Password length must be greater than 0.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    # Define character sets for complexity
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))

    # Display the generated password
    print(f"\nGenerated Password: {password}")

# Run the password generator
generate_password()
