"""
Topic: Loops in Python
Author: Pavithra K
Description:
This file explains loops in Python: for and while loops, including break, continue, and nested loops.
Loops are essential for iterating over data, preprocessing datasets, and automating repetitive tasks in AI/ML workflows.
"""

# ---------------------------
# 1. For Loop
# ---------------------------
print("---- For Loop ----")
fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print("I like", fruit)

# Iterating over numbers
for i in range(5):
    print("Number:", i)

# ---------------------------
# 2. While Loop
# ---------------------------
print("\n---- While Loop ----")
count = 0
while count < 5:
    print("Count is:", count)
    count += 1  # Increment to avoid infinite loop

# ---------------------------
# 3. Break Statement
# ---------------------------
print("\n---- Break Statement ----")
for i in range(10):
    if i == 5:
        print("Breaking the loop at i =", i)
        break
    print("i =", i)

# ---------------------------
# 4. Continue Statement
# ---------------------------
print("\n---- Continue Statement ----")
for i in range(5):
    if i == 2:
        print("Skipping i =", i)
        continue
    print("i =", i)

# ---------------------------
# 5. Nested Loops
# ---------------------------
print("\n---- Nested Loops ----")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i = {i}, j = {j}")

# ---------------------------
# 6. Loop with else
# ---------------------------
print("\n---- Loop with else ----")
for i in range(3):
    print("Looping i =", i)
else:
    print("Loop completed without break")

# ---------------------------
# 7. Practical AI/ML Example
# ---------------------------
print("\n---- Practical AI/ML Example ----")
# Iterating over dataset features
dataset = [
    {"feature1": 5, "feature2": 10},
    {"feature1": 7, "feature2": 14},
    {"feature1": 2, "feature2": 4}
]

# Scaling features using loops
scaled_dataset = []
for data in dataset:
    scaled_data = {}
    for key, value in data.items():
        scaled_data[key] = value / 10  # Simple normalization
    scaled_dataset.append(scaled_data)

print("Original Dataset:", dataset)
print("Scaled Dataset:", scaled_dataset)

