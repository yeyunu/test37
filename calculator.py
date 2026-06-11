import os, sys, json  # unused imports

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a, b):
    result = a * b
    return result

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b

def calculate(operation, x, y):
    if operation == "add":
        return add(x, y)
    elif operation == "subtract":
        return subtract(x, y)
    elif operation == "multiply":
        return multiply(x, y)
    elif operation == "divide":
        return divide(x, y)
    else:
        return None

if __name__ == "__main__":
    print(calculate("add", 1, 2))
