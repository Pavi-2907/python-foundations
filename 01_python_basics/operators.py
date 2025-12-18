"""
Topic: Operators in Python
Author: Pavithra K
Description:
This file explains Python operators with examples.
Operators are used to perform operations on variables and values, which is essential for data manipulation in AI/ML.
"""

# ---------------------------
# 1. Arithmetic Operators
# ---------------------------
print("---- Arithmetic Operators ----")
a = 10
b = 3

print("a + b =", a + b)   # Addition
print("a - b =", a - b)   # Subtraction
print("a * b =", a * b)   # Multiplication
print("a / b =", a / b)   # Division (float)
print("a // b =", a // b) # Floor Division
print("a % b =", a % b)   # Modulus
print("a ** b =", a ** b) # Exponentiation


# ---------------------------
# 2. Comparison Operators
# ---------------------------
print("\n---- Comparison Operators ----")
x = 5
y = 8

print("x == y ->", x == y)   # Equal
print("x != y ->", x != y)   # Not Equal
print("x > y ->", x > y)     # Greater Than
print("x < y ->", x < y)     # Less Than
print("x >= y ->", x >= y)   # Greater or Equal
print("x <= y ->", x <= y)   # Less or Equal


# ---------------------------
# 3. Logical Operators
# ---------------------------
print("\n---- Logical Operators ----")
p = True
q = False

print("p and q ->", p and q) # Logical AND
print("p or q ->", p or q)   # Logical OR
print("not p ->", not p)     # Logical NOT


# ---------------------------
# 4. Assignment Operators
# ---------------------------
print("\n---- Assignment Operators ----")
num = 5
print("num =", num)

num += 2  # num = num + 2
print("num += 2 ->", num)

num -= 1  # num = num - 1
print("num -= 1 ->", num)

num *= 3  # num = num * 3
print("num *= 3 ->", num)

num /= 2  # num = num / 2
print("num /= 2 ->", num)


# ---------------------------
# 5. Membership Operators
# ---------------------------
print("\n---- Membership Operators ----")
fruits = ["apple", "banana", "mango"]

print("'apple' in fruits ->", 'apple' in fruits)
print("'grape' not in fruits ->", 'grape' not in fruits)


# ---------------------------
# 6. Identity Operators
# ---------------------------
print("\n---- Identity Operators ----")
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print("a is b ->", a is b)   # True, same object
print("a is c ->", a is c)   # False, different objects
print("a == c ->", a == c)   # True, same values

