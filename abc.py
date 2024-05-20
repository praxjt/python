import sys

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    else:
        return x / y

if len(sys.argv) != 4:
    print("Usage: python abc.py <operation> <number1> <number2>")
    sys.exit(1)

operation = sys.argv[1]
num1 = float(sys.argv[2])
num2 = float(sys.argv[3])

if operation == '1':
    print("Result:", add(num1, num2))
elif operation == '2':
    print("Result:", subtract(num1, num2))
elif operation == '3':
    print("Result:", multiply(num1, num2))
elif operation == '4':
    print("Result:", divide(num1, num2))
else:
    print("Invalid operation")
