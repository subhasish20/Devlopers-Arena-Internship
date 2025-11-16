# Make a simple calculator that can add, subtract, multiply, divide

def simple_calculator():
    print("Simple Calculator")
    num1 = float(input("Enter the first number: "))
    operator = input("Enter the operator (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))

    if operator == "+":
        print(f"{num1} + {num2} = {num1 + num2}")
    elif operator == "-":
        print(f"{num1} - {num2} = {num1 - num2}")
    elif operator == "*":
        print(f"{num1} * {num2} = {num1 * num2}")
    elif operator == "/":
        if num2 != 0:
            print(f"{num1} / {num2} = {num1 / num2}")
        else:
            print("Error! Division by zero.")
    else:
        print("Invalid operator.")

simple_calculator()
