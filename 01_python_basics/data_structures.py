"""
Topic: Python Data Structures (Deep Dive)
Author: Pavithra K
Description:
This file explains Python built-in data structures: List, Tuple, Set, and Dictionary
with in-depth examples and AI/ML relevance.
Data structures are fundamental for efficient data storage, manipulation,
and preprocessing in AI/ML/DL pipelines.
"""

# =====================================================
# 1. LIST (Mutable, Ordered, Allows Duplicates)
# =====================================================
print("---- LIST ----")

numbers = [10, 20, 30, 40, 50]
print("Original List:", numbers)

# Accessing elements
print("First element:", numbers[0])
print("Last element:", numbers[-1])

# Modifying list
numbers.append(60)
numbers.insert(1, 15)
numbers.remove(30)
print("Modified List:", numbers)

# Iterating through list
for num in numbers:
    print("Number:", num)

# List comprehension (very important for interviews)
squares = [x ** 2 for x in numbers]
print("Squares:", squares)


# =====================================================
# 2. TUPLE (Immutable, Ordered, Allows Duplicates)
# =====================================================
print("\n---- TUPLE ----")

coordinates = (10, 20, 30)
print("Tuple:", coordinates)

# Accessing tuple elements
print("X coordinate:", coordinates[0])

# Tuple unpacking
x, y, z = coordinates
print("Unpacked:", x, y, z)

# Tuple is immutable (cannot modify)
# coordinates[0] = 50  # ❌ This will cause an error


# =====================================================
# 3. SET (Mutable, Unordered, No Duplicates)
# =====================================================
print("\n---- SET ----")

unique_values = {1, 2, 3, 3, 4, 5}
print("Set removes duplicates:", unique_values)

# Adding and removing
unique_values.add(6)
unique_values.discard(2)
print("Updated Set:", unique_values)

# Set operations (VERY IMPORTANT)
A = {1, 2, 3}
B = {3, 4, 5}

print("Union:", A | B)
print("Intersection:", A & B)
print("Difference:", A - B)


# =====================================================
# 4. DICTIONARY (Key-Value Pairs, Mutable)
# =====================================================
print("\n---- DICTIONARY ----")

student = {
    "name": "Pavithra",
    "age": 22,
    "course": "AI/ML"
}

print("Student Info:", student)

# Accessing values
print("Name:", student["name"])

# Adding & updating
student["age"] = 23
student["city"] = "India"

# Iterating dictionary
for key, value in student.items():
    print(key, ":", value)


# =====================================================
# 5. Choosing the Right Data Structure
# =====================================================
print("\n---- When to Use What ----")
print("List -> Ordered data, frequent updates")
print("Tuple -> Fixed data, faster & safer")
print("Set -> Unique values, fast lookup")
print("Dict -> Key-value mapping")


# =====================================================
# 6. Practical AI/ML Example
# =====================================================
print("\n---- Practical AI/ML Example ----")

# Dataset represented as list of dictionaries
dataset = [
    {"feature1": 10, "feature2": 20, "label": 1},
    {"feature1": 15, "feature2": 25, "label": 0},
    {"feature1": 30, "feature2": 35, "label": 1}
]

# Extract features and labels
features = []
labels = []

for row in dataset:
    features.append([row["feature1"], row["feature2"]])
    labels.append(row["label"])

print("Features:", features)
print("Labels:", labels)

