"""
Topic: Conditional Statements in Python
Author: Pavithra K
Description:
This file explains Python conditional statements: if, elif, and else.
Conditional statements allow decision-making in programs based on certain conditions.
They are essential in AI/ML for data preprocessing, feature selection, and model decision logic.
"""

# ---------------------------
# 1. Basic if Statement
# ---------------------------
print("---- Basic if Statement ----")
age = 18

if age >= 18:
    print("You are eligible to vote.")

# ---------------------------
# 2. if-else Statement
# ---------------------------
print("\n---- if-else Statement ----")
num = 10

if num % 2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")

# ---------------------------
# 3. if-elif-else Statement
# ---------------------------
print("\n---- if-elif-else Statement ----")
marks = 85

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: F")

# ---------------------------
# 4. Nested if Statements
# ---------------------------
print("\n---- Nested if Statements ----")
x = 15
y = 20

if x > 10:
    if y > 15:
        print("x > 10 and y > 15")
    else:
        print("x > 10 but y <= 15")
else:
    print("x <= 10")

# ---------------------------
# 5. Logical Operators with Conditions
# ---------------------------
print("\n---- Logical Operators with Conditions ----")
age = 25
has_id = True

if age >= 18 and has_id:
    print("Eligible to enter club")
else:
    print("Not eligible")

# ---------------------------
# 6. Practical AI/ML Example
# ---------------------------
print("\n---- Practical AI/ML Example ----")
# Simple threshold-based decision for ML output
probability = 0.72  # Probability predicted by ML model

if probability >= 0.8:
    prediction = "High Risk"
elif probability >= 0.5:
    prediction = "Moderate Risk"
else:
    prediction = "Low Risk"

print("Predicted Risk Level:", prediction)

