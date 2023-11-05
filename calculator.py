def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

def calculator():
    print("Options:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter choice (1/2/3/4):")

    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice")
        return

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "1":
        result = add(num1, num2)
        operation = "addition"
    elif choice == "2":
        result = subtract(num1, num2)
        operation = "subtraction"
    elif choice == "3":
        result = multiply(num1, num2)
        operation = "multiplication"
    else:
        result = divide(num1, num2)
        operation = "division"

    print(f"Result of {operation} is: {result}")

if __name__ == "__main__":
    calculator()
