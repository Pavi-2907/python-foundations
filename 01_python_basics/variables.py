"""
Topic: Variables in Python
Author: Pavithra K
Description:
This file explains Python variables in depth, including assignment,
dynamic typing, naming conventions, and best practices.
"""

# 1. Variable assignment (dynamic typing)
age = 22          # int
name = "Pavithra" # str
height = 5.4      # float
is_ai_student = True  # bool

print(age, name, height, is_ai_student)

# 2. Checking data types
print(type(age))
print(type(name))
print(type(height))
print(type(is_ai_student))

# 3. Reassignment (Python allows changing type)
age = "twenty two"
print(age, type(age))

# 4. Multiple assignment
x, y, z = 10, 20, 30
print(x, y, z)

# 5. Same value to multiple variables
a = b = c = 100
print(a, b, c)

# 6. Variable naming conventions (PEP8)
student_name = "AI Student"  # snake_case (recommended)
# StudentName = "Wrong style"  # not recommended

# 7. Variable references (memory concept)
num1 = 50
num2 = num1
print(id(num1), id(num2))  # same memory reference

# 8. Why this matters for AI / ML
# Variables store data, features, model parameters, and predictions
learning_rate = 0.01
epochs = 100
