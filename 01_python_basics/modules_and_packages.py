"""
Topic: Modules and Packages in Python
Author: Pavithra K
Description:
This file explains Python modules and packages, how to create them,
import different ways, and their importance in building scalable
AI/ML applications.
"""

# =====================================================
# 1. WHAT IS A MODULE?
# =====================================================
print("---- What is a Module ----")
print("A module is a file containing Python code (functions, classes, variables).")

# Example: using built-in module
import math

print("Square root of 25:", math.sqrt(25))
print("Value of PI:", math.pi)


# =====================================================
# 2. DIFFERENT WAYS TO IMPORT MODULES
# =====================================================
print("\n---- Import Styles ----")

# Import entire module
import random
print("Random number:", random.randint(1, 10))

# Import specific function
from math import factorial
print("Factorial of 5:", factorial(5))

# Import with alias
import numpy as np
arr = np.array([1, 2, 3])
print("NumPy Array:", arr)


# =====================================================
# 3. CREATING A CUSTOM MODULE
# =====================================================
print("\n---- Custom Module Example ----")

# Assume a file named utils.py exists with below code:
# def add(a, b):
#     return a + b

# from utils import add
# print("Addition:", add(3, 4))

print("Custom modules help organize reusable code.")


# =====================================================
# 4. WHAT IS A PACKAGE?
# =====================================================
print("\n---- What is a Package ----")
print("A package is a collection of modules inside a directory.")
print("It must contain an __init__.py file (Python <3.3 mandatory).")


# =====================================================
# 5. PACKAGE STRUCTURE EXAMPLE
# =====================================================
print("\n---- Package Structure ----")

"""
ml_project/
│
├── preprocessing/
│   ├── __init__.py
│   ├── scaler.py
│   └── cleaner.py
│
├── models/
│   ├── __init__.py
│   ├── svm.py
│   └── cnn.py
│
└── main.py
"""

print("This structure is commonly used in AI/ML projects.")


# =====================================================
# 6. IMPORTING FROM PACKAGES
# =====================================================
print("\n---- Importing from Packages ----")

# Example imports
# from preprocessing.scaler import normalize
# from models.svm import train_model

print("Packages improve readability and maintainability.")


# =====================================================
# 7. __name__ == '__main__'
# =====================================================
print("\n---- __name__ == '__main__' ----")

def main():
    print("Main function executed")

if __name__ == "__main__":
    main()


# =====================================================
# 8. AI/ML REAL-WORLD USE CASE
# =====================================================
print("\n---- AI/ML Use Case ----")

print("Large AI projects use packages to separate:")
print("- Data preprocessing")
print("- Feature engineering")
print("- Model training")
print("- Evaluation")
print("- Deployment utilities")

