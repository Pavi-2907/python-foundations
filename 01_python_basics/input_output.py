"""
Topic: Input and Output in Python
Author: Pavithra K
Description:
This file explains Python input and output operations.
Python provides built-in functions to take input from the user and display output.
Input and output operations are essential for data collection, preprocessing, and debugging in AI/ML/DL workflows.
"""

# ---------------------------
# 1. Output using print()
# ---------------------------
print("---- Output using print() ----")
print("Hello, Pavithra!")  # Basic output
print("Python", "for", "AI/ML")  # Multiple arguments
print("Addition:", 5 + 3)  # Combining text and result
print(f"Formatted String: {5} + {3} = {5 + 3}")  # f-string formatting (Python 3.6+)
print("Using separator:", 1, 2, 3, sep="-")  # Custom separator
print("Using end:", "Hello", end=" | ")  # Custom end character
print("World!")  # Output continues on the same line due to end=" | "

# ---------------------------
# 2. Input from the User
# ---------------------------
print("\n---- Input using input() ----")
# Basic input (always returns string)
name = input("Enter your name: ")
print("Hello,", name)

# Input integer
age = int(input("Enter your age: "))  # Convert string input to integer
print("Your age is:", age)

# Input float
height = float(input("Enter your height in meters: "))
print("Your height is:", height)

# Input multiple values (split)
x, y = input("Enter two numbers separated by space: ").split()
x = int(x)
y = int(y)
print(f"Sum of {x} and {y} is {x + y}")

# ---------------------------
# 3. Advanced Input Techniques
# ---------------------------
print("\n---- Advanced Input Techniques ----")
# Taking multiple inputs using list comprehension
numbers = [int(i) for i in input("Enter numbers separated by space: ").split()]
print("List of numbers:", numbers)
print("Sum:", sum(numbers))

# Using map() for type conversion
numbers_map = list(map(int, input("Enter numbers using map(): ").split()))
print("Numbers using map():", numbers_map)

# ---------------------------
# 4. File Input/Output Basics
# ---------------------------
print("\n---- File Input/Output Basics ----")
# Writing to a file
with open("sample.txt", "w") as file:
    file.write("Hello AI/ML World!\n")
    file.write("This is a sample file for Python I/O operations.\n")

# Reading from a file
with open("sample.txt", "r") as file:
    content = file.read()
print("Content of sample.txt:")
print(content)

# ---------------------------
# 5. Practical AI/ML Example
# ---------------------------
print("\n---- Practical AI/ML Example ----")
# Collecting user input for ML features
feature1 = float(input("Enter feature 1 (float): "))
feature2 = float(input("Enter feature 2 (float): "))
feature3 = float(input("Enter feature 3 (float): "))

features = [feature1, feature2, feature3]
print("Collected Features:", features)

# Converting features to string for storage
features_str = ','.join(map(str, features))
print("Features saved as string:", features_str)

