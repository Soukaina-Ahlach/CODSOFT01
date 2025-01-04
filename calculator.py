def calculator():
    print("Welcome to the Simple Calculator!")
    print("Please select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    # Prompt user for operation and numbers
    operation = input("Enter your choice (1/2/3/4): ").strip()

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Perform calculations
        if operation == "1":
            print(f"The result of {num1} + {num2} is: {num1 + num2}")
        elif operation == "2":
            print(f"The result of {num1} - {num2} is: {num1 - num2}")
        elif operation == "3":
            print(f"The result of {num1} * {num2} is: {num1 * num2}")
        elif operation == "4":
            if num2 != 0:
                print(f"The result of {num1} / {num2} is: {num1 / num2}")
            else:
                print("Error: Division by zero is not allowed.")
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

    except ValueError:
        print("Error: Please enter valid numeric inputs.")


# Run the calculator
calculator()
