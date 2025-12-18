"""
Topic: Error Handling in Python
Author: Pavithra K
Description:
This file explains error handling in Python using try, except, else, and finally blocks.
Error handling helps build robust, production-ready applications and is critical in AI/ML
pipelines where data issues and runtime errors are common.
"""

# ---------------------------
# 1. Basic try-except Block
# ---------------------------
print("---- Basic try-except ----")

try:
    x = int(input("Enter a number: "))
    print("You entered:", x)
except ValueError:
    print("Error: Please enter a valid integer")


# ---------------------------
# 2. Handling Multiple Exceptions
# ---------------------------
print("\n---- Multiple Exceptions ----")

try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    result = a / b
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed")
except ValueError:
    print("Error: Invalid input, please enter integers")


# ---------------------------
# 3. Using else Block
# ---------------------------
print("\n---- try-except-else ----")

try:
    num = int(input("Enter a positive number: "))
except ValueError:
    print("Error: Not a number")
else:
    print("You entered:", num)


# ---------------------------
# 4. Using finally Block
# ---------------------------
print("\n---- try-except-finally ----")

try:
    file = open("sample.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("Error: File not found")
finally:
    print("File operation attempted")


# ---------------------------
# 5. Catching All Exceptions (Not Recommended in Production)
# ---------------------------
print("\n---- Generic Exception Handling ----")

try:
    data = [1, 2, 3]
    print(data[5])
except Exception as e:
    print("An error occurred:", e)


# ---------------------------
# 6. Raising Custom Exceptions
# ---------------------------
print("\n---- Raising Exceptions ----")

def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or above")
    return "Access granted"

try:
    print(check_age(16))
except ValueError as e:
    print("Error:", e)


# ---------------------------
# 7. Custom Exception Class
# ---------------------------
print("\n---- Custom Exception Class ----")

class InvalidDataError(Exception):
    pass

def validate_data(value):
    if value < 0:
        raise InvalidDataError("Data value cannot be negative")
    return value

try:
    validate_data(-10)
except InvalidDataError as e:
    print("Custom Error:", e)


# ---------------------------
# 8. Practical AI/ML Example
# ---------------------------
print("\n---- Practical AI/ML Example ----")

def preprocess_data(data):
    try:
        cleaned_data = [float(x) for x in data]
        return cleaned_data
    except ValueError:
        print("Data preprocessing error: Non-numeric value found")
        return []

raw_data = ["10", "20", "abc", "40"]
processed_data = preprocess_data(raw_data)

print("Processed Data:", processed_data)

