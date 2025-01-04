import random
import string

def generate_password(length):
   
    if length < 1:
        raise ValueError("Password length must be at least 1.")

    characters = string.ascii_letters + string.digits + string.punctuation

    return ''.join(random.choices(characters, k=length))

    #    Main function to run the password generator.
def main():
    print("Welcome to the Password Generator!")

    while True:
        try:
            length = int(input("Enter the desired length of the password (or 0 to exit): "))

            if length == 0:
                print("Exiting the Password Generator. Goodbye!")
                break

            # Generate and display the password
            password = generate_password(length)
            print(f"Your generated password is: {password}\n")
        except ValueError:
            print("Invalid input. Please enter a valid number for the password length.\n")

if __name__ == "__main__":
    main()
