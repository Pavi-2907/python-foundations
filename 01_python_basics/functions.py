"""
Topic: Functions in Python
Author: Pavithra K
Description:
This file explains Python functions including definition, arguments, return values, *args, **kwargs, and practical examples.
Functions allow code reusability, modularity, and are essential for AI/ML workflows like data preprocessing, feature extraction, and model evaluation.
"""

# ---------------------------
# 1. Defining a Basic Function
# ---------------------------
print("---- Basic Function ----")

def greet():
    print("Hello, Pavithra!")

greet()  # Function call

# ---------------------------
# 2. Function with Parameters
# ---------------------------
print("\n---- Function with Parameters ----")

def add(a, b):
    return a + b

result = add(5, 3)
print("Sum of 5 and 3 is:", result)

# ---------------------------
# 3. Function with Default Parameters
# ---------------------------
print("\n---- Function with Default Parameters ----")

def greet_person(name="Guest"):
    print("Hello,", name)

greet_person("Alice")
greet_person()  # Uses default parameter

# ---------------------------
# 4. Function with Multiple Parameters
# ---------------------------
print("\n---- Function with Multiple Parameters ----")

def multiply(a, b, c):
    return a * b * c

print("Multiplication of 2,3,4:", multiply(2, 3, 4))

# ---------------------------
# 5. *args (Variable-length Arguments)
# ---------------------------
print("\n---- *args Example ----")

def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print("Sum of 1,2,3,4,5:", sum_all(1, 2, 3, 4, 5))

# ---------------------------
# 6. **kwargs (Keyword Variable-length Arguments)
# ---------------------------
print("\n---- **kwargs Example ----")

def display_info(**info):
    for key, value in info.items():
        print(f"{key} : {value}")

display_info(name="Pavithra", age=22, course="AI/ML")

# ---------------------------
# 7. Nested Functions
# ---------------------------
print("\n---- Nested Functions ----")

def outer_function(text):
    def inner_function():
        print("Inner Function:", text)
    inner_function()

outer_function("Hello from outer function")

# ---------------------------
# 8. Lambda Functions (Anonymous Functions)
# ---------------------------
print("\n---- Lambda Functions ----")

square = lambda x: x ** 2
print("Square of 5:", square(5))

# ---------------------------
# 9. Practical AI/ML Example
# ---------------------------
print("\n---- Practical AI/ML Example ----")

# Function to normalize a list of feature values
def normalize_features(features):
    max_val = max(features)
    min_val = min(features)
    return [(x - min_val) / (max_val - min_val) for x in features]

features = [10, 20, 30, 40, 50]
normalized = normalize_features(features)
print("Original Features:", features)
print("Normalized Features:", normalized)

