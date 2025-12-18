"""
Topic: Object-Oriented Programming (OOP) in Python
Author: Pavithra K
Description:
This file covers core OOP concepts in Python including
Class, Object, Constructor, Inheritance, Encapsulation,
Polymorphism, and Abstraction with real-world and AI/ML examples.
"""

# =====================================================
# 1. CLASS AND OBJECT
# =====================================================
print("---- Class and Object ----")

class Student:
    def display(self):
        print("I am a student")

obj = Student()
obj.display()


# =====================================================
# 2. CONSTRUCTOR (__init__)
# =====================================================
print("\n---- Constructor ----")

class Person:
    def __init__(self, name, age):
        self.name = name      # instance variable
        self.age = age

    def info(self):
        print(f"Name: {self.name}, Age: {self.age}")

p1 = Person("Pavithra", 22)
p1.info()


# =====================================================
# 3. INSTANCE VS CLASS VARIABLES
# =====================================================
print("\n---- Instance vs Class Variables ----")

class Employee:
    company = "Google"  # class variable

    def __init__(self, name):
        self.name = name  # instance variable

e1 = Employee("Alice")
e2 = Employee("Bob")

print(e1.name, e1.company)
print(e2.name, e2.company)


# =====================================================
# 4. INHERITANCE
# =====================================================
print("\n---- Inheritance ----")

class Model:
    def train(self):
        print("Training model...")

class NeuralNetwork(Model):
    def predict(self):
        print("Predicting output...")

nn = NeuralNetwork()
nn.train()
nn.predict()


# =====================================================
# 5. METHOD OVERRIDING (Polymorphism)
# =====================================================
print("\n---- Method Overriding ----")

class MLModel:
    def accuracy(self):
        print("Base model accuracy")

class CNN(MLModel):
    def accuracy(self):
        print("CNN accuracy: 92%")

class SVM(MLModel):
    def accuracy(self):
        print("SVM accuracy: 88%")

models = [CNN(), SVM()]

for model in models:
    model.accuracy()


# =====================================================
# 6. ENCAPSULATION
# =====================================================
print("\n---- Encapsulation ----")

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print("Balance:", account.get_balance())


# =====================================================
# 7. ABSTRACTION
# =====================================================
print("\n---- Abstraction ----")

from abc import ABC, abstractmethod

class Algorithm(ABC):

    @abstractmethod
    def execute(self):
        pass

class SortingAlgorithm(Algorithm):
    def execute(self):
        print("Executing sorting algorithm")

algo = SortingAlgorithm()
algo.execute()


# =====================================================
# 8. STATIC METHOD & CLASS METHOD
# =====================================================
print("\n---- Static & Class Methods ----")

class MathUtils:

    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def info(cls):
        print("Utility class for math operations")

print(MathUtils.add(5, 10))
MathUtils.info()


# =====================================================
# 9. PRACTICAL AI/ML USE CASE
# =====================================================
print("\n---- Practical AI/ML Example ----")

class Dataset:
    def __init__(self, data):
        self.data = data

    def normalize(self):
        max_val = max(self.data)
        min_val = min(self.data)
        return [(x - min_val) / (max_val - min_val) for x in self.data]

data = Dataset([10, 20, 30, 40])
print("Normalized Data:", data.normalize())

