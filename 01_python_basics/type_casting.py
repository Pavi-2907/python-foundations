"""
Topic: Type Casting in Python
Author: Pavithra K
Description:
This file explains Python type casting (type conversion) with examples.
Type casting is used to convert a variable from one data type to another, which is essential in AI/ML data preprocessing.
"""

# ---------------------------
# 1. Converting to Integer
# ---------------------------
print("---- Converting to Integer ----")
x = 5.7
y = "10"

# Float to int
int_x = int(x)
print("int(5.7) ->", int_x)

# String to int
int_y = int(y)
print('int("10") ->', int_y)


# ---------------------------
# 2. Converting to Float
# ---------------------------
print("\n---- Converting to Float ----")
a = 10
b = "20.5"

# Integer to float
float_a = float(a)
print("float(10) ->", float_a)

# String to float
float_b = float(b)
print('float("20.5") ->', float_b)


# ---------------------------
# 3. Converting to String
# ---------------------------
print("\n---- Converting to String ----")
num = 100
pi = 3.14

str_num = str(num)
str_pi = str(pi)

print("str(100) ->", str_num)
print("str(3.14) ->", str_pi)


# ---------------------------
# 4. Converting to Boolean
# ---------------------------
print("\n---- Converting to Boolean ----")
val1 = 0
val2 = 10
val3 = ""

bool1 = bool(val1)
bool2 = bool(val2)
bool3 = bool(val3)

print("bool(0) ->", bool1)
print("bool(10) ->", bool2)
print('bool("") ->', bool3)


# ---------------------------
# 5. Practical Example in AI/ML
# ---------------------------
print("\n---- Practical Example ----")
# Converting string data to numeric for ML
data_str = ["1", "2", "3", "4", "5"]
data_int = [int(i) for i in data_str]
print("Original String Data:", data_str)
print("Converted to Integers:", data_int)

# Converting numeric labels to string for output
labels = [0, 1, 1, 0]
labels_str = [str(label) for label in labels]
print("Original Labels:", labels)
print("Converted to Strings:", labels_str)

