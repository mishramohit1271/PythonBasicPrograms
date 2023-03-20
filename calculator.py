# Add two number function
def add(num1, num2):
    return num1 + num2

# Function for subtraction
def subtract(num1, num2):
    return num1 - num2

# Function for multiplication
def multiply(num1, num2):
    return num1 * num2

# Function for division
def divide(num1, num2):
    return num1 / num2

# Code to get user input for numbers and operation
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

# Performing calculation based on user input
if operation == '+':
    print(num1, "+", num2, "=", add(num1, num2))
elif operation == '-':
    print(num1, "-", num2, "=", subtract(num1, num2))
elif operation == '*':
    print(num1, "*", num2, "=", multiply(num1, num2))
elif operation == '/':
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("Invalid operation")
