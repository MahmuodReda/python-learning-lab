#!/usr/bin/python

# Function to display a simple message
def display_message():
    print("Reda")

display_message()

# Function to calculate the product of two numbers
def multiply_numbers(a, b):
    return a * b

print(multiply_numbers(5, 9))

# Function to display three keyword arguments
def display_arguments(first, second, third):
    print("1", first)
    print("2", second)
    print("3", third)

display_arguments(first="e", third=5, second=quit)

# Function to display contents of a list
def print_list(items):
    unused_variable = 5  # Can be removed if not needed
    print(items)

sample_list = ["hg", "25"]
print_list(sample_list)

# Function that accepts any number of positional arguments
def show_args(*args):
    print(type(args))  # Shows it's a tuple
    print(args)

show_args("s", "e")

# Will print 'None' because print_list doesn't return anything
print(print_list(sample_list))

# Function that accepts any number of keyword arguments
def show_kwargs(**kwargs):
    print(kwargs)

show_kwargs(language="Python")

# Demonstration of variable scope (local variable)
global_value = 8

def demonstrate_local_scope():
    local_value = 9
    print(local_value)
    print(id(local_value))

demonstrate_local_scope()
print(global_value)
print(id(global_value))

# Using 'global' keyword to change global variable
global_value = 8

def modify_global_variable():
    global global_value
    global_value = 9
    print(global_value)
    print(id(global_value))

modify_global_variable()
print(global_value)
print(id(global_value))

# Importing and using a function from a custom module
import src.Cal as Calculator
import importlib

print(Calculator.sum(5, 3))  # Assumes sum(a, b) is defined in src/Cal.py

# Dynamically importing a module (Google Text-to-Speech)
print(importlib.import_module("gtts"))
