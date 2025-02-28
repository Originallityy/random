###########################################################
#                                                         #
#                 PYTHON BASICS                           #
#                                                         #
###########################################################

#############################################
# BASIC PYTHON CONCEPTS
#############################################

# Print function: Used to output text to the console.
print("Hello, World!")

# Variables: Used to store data values.
x = 5
y = "Hello"

# Data types: Different types of data that can be stored in variables.
integer = 10  # Integer
floating_point = 10.5  # Floating point number
string = "Hello"  # String
boolean = True  # Boolean

# Type conversion
str_to_int = int("42")
float_to_int = int(10.5)
int_to_str = str(42)

# F-strings (formatted string literals)
name = "Python"
version = 3.11
print(f"{name} version {version} is awesome!")

# Asking the user for input
prompt = input("Enter your name: ")

#############################################
# DATA STRUCTURES
#############################################

# Lists: Ordered collection of items.
my_list = [1, 2, 3, 4, 5]

# List operations
my_list.append(6)        # Add element
my_list.pop()            # Remove last element
my_list.insert(0, 0)     # Insert at specific position
print(my_list[2:4])      # Slicing

# Tuples: Ordered, immutable collection of items.
my_tuple = (1, 2, 3, 4, 5)

# Dictionaries: Collection of key-value pairs.
my_dict = {"name": "John", "age": 30}
my_dict["email"] = "john@example.com"  # Add new key-value pair

# Sets: Unordered collection of unique items
my_set = {1, 2, 3, 4, 5}
my_set.add(6)
duplicates = {1, 2, 2, 3, 3, 4}  # Will only store {1, 2, 3, 4}

# List comprehensions: Concise way to create lists.
squares = [x**2 for x in range(10)]
print(squares)

# Dictionary comprehension
squared_dict = {x: x**2 for x in range(5)}

#############################################
# CONTROL FLOW
#############################################

# Conditional statements: Used to perform different actions based on different conditions.
if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")

# Ternary operator
result = "Even" if x % 2 == 0 else "Odd"

# Loops: Used to repeat a block of code multiple times.
# For loop
for i in range(5):
    print(i)

# Loop with enumerate
for index, value in enumerate(my_list):
    print(f"Index: {index}, Value: {value}")

# While loop
count = 0
while count < 5:
    print(count)
    count += 1

# Break and continue
for i in range(10):
    if i == 3:
        continue  # Skip this iteration
    if i == 8:
        break     # Exit the loop
    print(i)

#############################################
# FUNCTIONS AND LAMBDAS
#############################################

# Functions: Block of code that only runs when it is called.
def greet(name):
    print("Hello, " + name)

greet("Alice")

# Default parameters
def greet_with_message(name, message="Good day!"):
    print(f"Hello, {name}. {message}")

greet_with_message("Bob")
greet_with_message("Charlie", "How are you?")

# Return values
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)

# Lambda functions: Small anonymous functions.
add = lambda a, b: a + b
print(add(2, 3))

# Using lambda with map and filter
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))

###########################################################
#                                                         #
#               INTERMEDIATE PYTHON                       #
#                                                         #
###########################################################

#############################################
# OBJECT-ORIENTED PROGRAMMING
#############################################

# Classes: Used to create user-defined data structures.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is " + self.name)

# Creating an object of the class
person1 = Person("John", 30)
person1.greet()

# Inheritance
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # Call parent class constructor
        self.student_id = student_id
        
    def study(self):
        print(f"{self.name} is studying")

student1 = Student("Emma", 20, "S12345")
student1.greet()
student1.study()

#############################################
# FILE HANDLING
#############################################

# File handling: Used to read and write files.
with open("example.txt", "w") as file:
    file.write("Hello, World!")

with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# Reading file line by line
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())
        
# Working with JSON
import json

data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Write JSON to file
with open("data.json", "w") as file:
    json.dump(data, file)
    
# Read JSON from file
with open("data.json", "r") as file:
    loaded_data = json.load(file)

#############################################
# ERROR HANDLING
#############################################

# Exception handling: Used to handle errors.
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("This will always execute")
    
# Handling multiple exceptions
try:
    value = int(input("Enter a number: "))
    result = 10 / value
except ValueError:
    print("Invalid input: not a number")
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception as e:
    print(f"An error occurred: {e}")
    
# Raising exceptions
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

###########################################################
#                                                         #
#                    ADVANCED PYTHON                      #
#                                                         #
###########################################################

#############################################
# ADVANCED PYTHON FEATURES
#############################################

# Decorators: Used to modify the behavior of a function.
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# Decorator with arguments
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say_hi(name):
    print(f"Hi, {name}!")
    
say_hi("Alice")

# Generators: Functions that return an iterable set of items.
def my_generator():
    for i in range(5):
        yield i

for value in my_generator():
    print(value)
    
# Generator expressions
gen = (x**2 for x in range(5))
print(next(gen))  # 0
print(next(gen))  # 1

# Context managers: Used to manage resources.
class MyContextManager:
    def __enter__(self):
        print("Entering the context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context")
        if exc_type:
            print(f"An exception occurred: {exc_type}, {exc_value}")
        return False  # Propagate the exception if any

with MyContextManager():
    print("Inside the context")
    
# Creating context manager with contextlib
from contextlib import contextmanager

@contextmanager
def my_context():
    print("Entering context")
    try:
        yield
    finally:
        print("Exiting context")
        
with my_context():
    print("Inside the context manager")

#############################################
# MODULES AND LIBRARIES
#############################################

# Importing modules: Used to include external libraries.
import math
print(math.sqrt(16))

# Importing specific functions
from math import pi, sin
print(sin(pi/2))

# Aliasing imports
import numpy as np
import pandas as pd  # Commented out to avoid dependency issues

# Using pip to install external libraries
# $ pip install requests
import requests
response = requests.get("https://api.github.com")
print(response.status_code)

#############################################
# CONCURRENCY AND PARALLELISM
#############################################

# Threading
import threading

def print_numbers():
    for i in range(5):
        print(f"Number {i}")
        
def print_letters():
    for letter in 'ABCDE':
        print(f"Letter {letter}")
        
# Create threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

# Start threads
t1.start()
t2.start()

# Wait for threads to finish
t1.join()
t2.join()

# Asyncio for asynchronous programming
import asyncio

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

# This would normally be run in an async environment
# asyncio.run(say_after(1, "Hello"))

###########################################################
#                                                         #
#                    EXPERT PYTHON                        #
#                                                         #
###########################################################

#############################################
# METAPROGRAMMING
#############################################

# Metaclasses - classes that define classes
class Meta(type):
    def __new__(cls, name, bases, attrs):
        # Add a new attribute to the class
        attrs['added_by_meta'] = True
        print(f"Creating class {name}")
        return super().__new__(cls, name, bases, attrs)

class MyClass(metaclass=Meta):
    pass

# Check the attribute added by the metaclass
print(MyClass.added_by_meta)  # True

# Modifying class attributes via __getattribute__ and __setattr__
class AttributeTracker:
    def __init__(self):
        self._x = None
        
    @property
    def x(self):
        print("Getting x")
        return self._x
        
    @x.setter
    def x(self, value):
        print(f"Setting x to {value}")
        self._x = value
        
    def __getattribute__(self, name):
        if name.startswith('_'):
            return super().__getattribute__(name)
        print(f"Accessing {name}")
        return super().__getattribute__(name)
        
obj = AttributeTracker()
obj.x = 10
print(obj.x)

#############################################
# ADVANCED FUNCTIONAL PROGRAMMING
#############################################

# Partial functions
from functools import partial

def multiply(x, y):
    return x * y

# Create a new function with x fixed to 2
double = partial(multiply, 2)
print(double(5))  # 10

# Closures - functions that remember their enclosing scope
def create_counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment
    
counter = create_counter()
print(counter())  # 1
print(counter())  # 2

# Currying - transforming multiple argument functions into a chain of single-argument functions
def curry(func):
    def curried(*args, **kwargs):
        if len(args) + len(kwargs) >= func.__code__.co_argcount:
            return func(*args, **kwargs)
        return lambda *more_args, **more_kwargs: curried(*(args + more_args), **{**kwargs, **more_kwargs})
    return curried

@curry
def add_three(a, b, c):
    return a + b + c

print(add_three(1)(2)(3))  # 6
print(add_three(1, 2)(3))  # 6
print(add_three(1)(2, 3))  # 6

#############################################
# PERFORMANCE OPTIMIZATION
#############################################

# Profiling code
import cProfile
import time

def slow_function():
    total = 0
    for i in range(1000000):
        total += i
    return total

# Example of how to profile (commented out to prevent execution)
# To profile, uncomment the line below:
# cProfile.run('slow_function()')

# Using timeit for benchmarking
import timeit

# Define the performance test function
def performance_test():
    # Comparing list creation methods
    setup = "import random"
    
    list_comp = timeit.timeit(
        "[random.random() for _ in range(10000)]",
        setup=setup,
        number=100
    )
    
    list_append = timeit.timeit(
        "result = []; [result.append(random.random()) for _ in range(10000)]",
        setup=setup,
        number=100
    )
    
    print(f"List comprehension: {list_comp:.6f} seconds")
    print(f"List append: {list_append:.6f} seconds")

# To run the performance test, uncomment the line below:
# performance_test()

# Memory optimization with __slots__
class RegularClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class SlottedClass:
    __slots__ = ['x', 'y']
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Memory usage example (commented out):

# To demonstrate memory usage difference:
import sys
regular_objects = [RegularClass(1, 2) for _ in range(1000)]
slotted_objects = [SlottedClass(1, 2) for _ in range(1000)]
print(f"Regular class size: {sys.getsizeof(regular_objects[0]) * len(regular_objects)}")
print(f"Slotted class size: {sys.getsizeof(slotted_objects[0]) * len(slotted_objects)}")


#############################################
# ADVANCED CONCURRENCY
#############################################

# Multiprocessing for CPU-bound tasks
import multiprocessing

def cpu_bound_task(n):
    # A CPU-bound task that computes the sum of squares up to n.
    return sum(i * i for i in range(n))

# Example of multiprocessing (commented out because it needs __main__ protection)
def demo_multiprocessing():
    # Create a pool of worker processes
    with multiprocessing.Pool(processes=3) as pool:
        # Map the function to different inputs
        results = pool.map(cpu_bound_task, [10000000, 20000000, 30000000])
        print(f"Results: {results}")

# To run the multiprocessing demo, you must use the if __name__ == "__main__" guard:

if __name__ == "__main__":
    demo_multiprocessing()


# Advanced asyncio patterns
import asyncio

async def fetch_data(url):
    print(f"Fetching {url}")
    await asyncio.sleep(1)  # Simulate network delay
    print(f"Fetched {url}")
    return f"Data from {url}"

async def process_async_tasks():
    # Gather multiple tasks to run concurrently
    urls = ['url1', 'url2', 'url3']
    tasks = [fetch_data(url) for url in urls]
    results = await asyncio.gather(*tasks)
    print(results)
    
    # Run tasks as they complete
    for task in asyncio.as_completed([fetch_data(f'url{i}') for i in range(5)]):
        result = await task
        print(f"Task completed with result: {result}")

# To run an asyncio event loop (commented out):

if __name__ == "__main__":
    asyncio.run(process_async_tasks())


#############################################
# DESIGN PATTERNS
#############################################

# Singleton pattern
class Singleton:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)  # Fixed: removed args, kwargs from __new__
        return cls._instance
    
    def __init__(self, value=None):
        # Initialize attributes in __init__, not in __new__
        self.value = value
        
# Example of singleton usage:
singleton1 = Singleton("first")
singleton2 = Singleton("second")
print(singleton1 is singleton2)  # True
print(singleton1.value)  # "second" (the second initialization overwrote the first)

# Factory pattern
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class AnimalFactory:
    def create_animal(self, animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError(f"Unknown animal type: {animal_type}")

# Usage example
factory = AnimalFactory()
dog = factory.create_animal("dog")
cat = factory.create_animal("cat")
print(dog.speak())  # Woof!
print(cat.speak())  # Meow!

# Observer pattern
class Subject:
    def __init__(self):
        self._observers = []
    
    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)
    
    def detach(self, observer):
        if observer in self._observers:  # Fixed: Check if observer exists before removing
            self._observers.remove(observer)
    
    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

class Observer:
    def update(self, message):
        pass

class ConcreteObserver(Observer):
    def __init__(self, name):
        self.name = name
    
    def update(self, message):
        print(f"{self.name} received: {message}")

# Usage example
subject = Subject()
observer1 = ConcreteObserver("Observer 1")
observer2 = ConcreteObserver("Observer 2")

subject.attach(observer1)
subject.attach(observer2)
subject.notify("Hello Observers!")  # Both observers get notified

subject.detach(observer1)
subject.notify("Hello again!")  # Only observer2 gets notified

#############################################
# ADVANCED TESTING
#############################################

# Using unittest
import unittest

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        # Setup runs before each test method
        self.test_string = "hello world"
    
    def test_upper(self):
        self.assertEqual(self.test_string.upper(), "HELLO WORLD")
    
    def test_split(self):
        self.assertEqual(self.test_string.split(), ["hello", "world"])
        
    def tearDown(self):
        # Teardown runs after each test method
        pass

# To run tests (commented out):
# if __name__ == "__main__":
#     unittest.main()

# Using pytest fixtures (commented out as it requires pytest package)

import pytest

@pytest.fixture
def sample_data():
    return {"name": "Test", "value": 42}

def test_data_name(sample_data):
    assert sample_data["name"] == "Test"

def test_data_value(sample_data):
    assert sample_data["value"] == 42


# Mocking
from unittest.mock import Mock, patch

# Create a mock object
mock = Mock()
mock.method.return_value = "mocked result"
print(mock.method())  # "mocked result"

# Patching a function
def get_data():
    # Imagine this calls an external API
    return {"status": "error"}

# Example of patching (commented out to avoid execution errors)

# This would work in a test function
with patch('__main__.get_data') as mock_get:
    mock_get.return_value = {"status": "success"}
    result = get_data()
    assert result["status"] == "success"


#############################################
# ADVANCED PYTHON LIBRARIES
#############################################

# Working with NumPy (commented out as it requires numpy)

import numpy as np

# Create arrays
arr = np.array([1, 2, 3, 4, 5])

# Array operations
print(arr * 2)  # Element-wise multiplication
print(np.sqrt(arr))  # Element-wise square root

# Multi-dimensional arrays
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix.shape)  # (3, 3)
print(matrix.T)  # Transpose


# Data handling with Pandas (commented out as it requires pandas)

import pandas as pd

# Create a DataFrame
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 34, 29, 42],
    'City': ['New York', 'Paris', 'Berlin', 'London']
}
df = pd.DataFrame(data)

# Data manipulation
print(df.head())
print(df.describe())
print(df[df['Age'] > 30])  # Filtering

# Reading/writing data
df.to_csv('data.csv', index=False)
df_loaded = pd.read_csv('data.csv')


# Web development with Flask (commented out as it requires Flask)

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {"message": "Success", "data": [1, 2, 3, 4, 5]}
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)


# End of the Python tutorial file
print("Python tutorial completed!")
