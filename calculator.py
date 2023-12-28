while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("Enter the number of the operation you want to perform (1/2/3/4): ")

    select_digit = int(input("Your choice: "))

    if select_digit == 1:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result_of_one = num1 + num2
        print("Result:", result_of_one)

    elif select_digit == 2:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result_of_two = num1 - num2
        print("Result:", result_of_two)

    elif select_digit == 3:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result_of_three = num1 * num2
        print("Result:", result_of_three)

    elif select_digit == 4:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        if num2 == 0:
            print("Error: Division by zero")
        else:
            result_of_four = num1 / num2
            print("Result:", result_of_four)

    else:
        print("Invalid choice. Please select a valid option (1/2/3/4).")
        break