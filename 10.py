import math
import random
history = {}

def arithmetic():
    try:
        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter Second Number: "))

        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        choice = int(input("Enter Choice: "))

        if choice == 1:
            result = num1 + num2
        elif choice == 2:
            result = num1 - num2
        elif choice == 3:
            result = num1 * num2
        elif choice == 4:
            result = num1 / num2
        else:
            print("Invalid Choice")
            return

        print("Result:", result)

        time = input("Enter Timestamp: ")
        history.update({time: result})

    except ZeroDivisionError:
        print("Cannot divide by zero.")

    except ValueError:
        print("Please enter valid input.")


# Scientific Calculation Function
def scientific():
    try:
        num = float(input("Enter Number: "))

        print("1. Square Root")
        print("2. Power")
        print("3. Factorial")

        choice = int(input("Enter Choice: "))

        if choice == 1:
            result = math.sqrt(num)

        elif choice == 2:
            power = int(input("Enter Power: "))
            result = math.pow(num, power)

        elif choice == 3:
            result = math.factorial(int(num))

        else:
            print("Invalid Choice")
            return

        print("Result:", result)

        time = input("Enter Timestamp: ")
        history.update({time: result})

    except Exception:
        print("Invalid Input")


# Random Number Function
def random_number():
    try:
        start = int(input("Enter Start Number: "))
        end = int(input("Enter End Number: "))

        result = random.randint(start, end)

        print("Random Number:", result)

        time = input("Enter Timestamp: ")
        history.update({time: result})

    except ValueError:
        print("Please enter valid numbers.")


# View History
def view_history():
    if history:
        print("\nHistory")
        for key, value in history.items():
            print(key, ":", value)
    else:
        print("No History Available")


# Main Menu
while True:

    print("\n----- Smart Calculator & Data Manager -----")
    print("1. Basic Arithmetic")
    print("2. Scientific Calculations")
    print("3. Generate Random Number")
    print("4. Store Results in Dictionary")
    print("5. View History")
    print("6. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        arithmetic()

    elif choice == 2:
        scientific()

    elif choice == 3:
        random_number()

    elif choice == 4:
        print("Results are stored automatically after every calculation.")

    elif choice == 5:
        view_history()

    elif choice == 6:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")