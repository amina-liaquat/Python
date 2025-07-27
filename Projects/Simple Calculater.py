def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

print("Simple Calculator")
print("-----------------")
print("Operations:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Select operation (1/2/3/4): ")

    if operation == '1':
        result = add(num1, num2)
    elif operation == '2':
        result = subtract(num1, num2)
    elif operation == '3':
        result = multiply(num1, num2)
    elif operation == '4':
        result = divide(num1, num2)
    else:
        result = "Invalid operation selected."

    print(f"Result: {result}")

except ValueError:
    print("Invalid input! Please enter numbers only.")
