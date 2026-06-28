#!/usr/bin/python3
# Quest 26: The Simple Calculator - functions and if-elif-else


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error! Cannot divide by zero."
    return a / b


a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operation = input("Enter operation (add, subtract, multiply, divide): ")

if operation == "add":
    print("Result: {}".format(add(a, b)))
elif operation == "subtract":
    print("Result: {}".format(subtract(a, b)))
elif operation == "multiply":
    print("Result: {}".format(multiply(a, b)))
elif operation == "divide":
    print("Result: {}".format(divide(a, b)))
else:
    print("Invalid operation!")
