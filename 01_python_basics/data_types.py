"""
Topic: Data Types in Python
Author: Pavithra K
Description:
This file explains Python data types with examples.
Python has several built-in data types which are essential for AI/ML/DL programming.
"""

# ---------------------------
# 1. Numeric Data Types
# ---------------------------

# Integer
age = 25
print("Age:", age, "| Type:", type(age))

# Float
height = 5.6
print("Height:", height, "| Type:", type(height))

# Complex
complex_number = 2 + 3j
print("Complex Number:", complex_number, "| Type:", type(complex_number))


# ---------------------------
# 2. Sequence Data Types
# ---------------------------

# String
name = "Pavithra"
print("Name:", name, "| Type:", type(name))

# List
fruits = ["apple", "banana", "mango"]
print("Fruits:", fruits, "| Type:", type(fruits))

# Tuple
colors = ("red", "green", "blue")
print("Colors:", colors, "| Type:", type(colors))

# Range
numbers = range(5)
print("Numbers:", list(numbers), "| Type:", type(numbers))


# ---------------------------
# 3. Mapping Data Type
# ---------------------------

# Dictionary
student = {"name": "Pavithra", "age": 25, "course": "AI/ML"}
print("Student Info:", student, "| Type:", type(student))


# ---------------------------
# 4. Set Types
# ---------------------------

# Set
unique_numbers = {1, 2, 3, 3, 4}
print("Unique Numbers:", unique_numbers, "| Type:", type(unique_numbers))

# Frozen Set (immutable set)
immutable_set = frozenset([1, 2, 3, 3, 4])
print("Immutable Set:", immutable_set, "| Type:", type(immutable_set))


# ---------------------------
# 5. Boolean Type
# ---------------------------

is_ai_student = True
print("Is AI Student:", is_ai_student, "| Type:", type(is_ai_student))


# ---------------------------
# 6. None Type
# ---------------------------

no_value = None
print("No Value:", no_value, "| Type:", type(no_value))
