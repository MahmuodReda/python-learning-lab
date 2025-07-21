#!/user/bin/python

# Example demonstrating different data types in Python

# 1. Integer: Represents whole numbers without a decimal part
integer_example = 42
print("Integer:", integer_example, "Type:", type(integer_example))

# 2. Float: Represents numbers with a decimal point
float_example = 3.14
print("Float:", float_example, "Type:", type(float_example))

# 3. String: Represents a sequence of characters enclosed in single or double quotes
string_example = "Hello, Python!"
print("String:", string_example, "Type:", type(string_example))

# 4. List: Ordered, mutable collection of items
list_example = [1, "apple", 3.5, True]
print("List:", list_example, "Type:", type(list_example))

# 5. Tuple: Ordered, immutable collection of items
tuple_example = (10, "banana", False)
print("Tuple:", tuple_example, "Type:", type(tuple_example))

# 6. Dictionary: Unordered collection of key-value pairs
dict_example = {"name": "Ali", "age": 25, "city": "Riyadh"}
print("Dictionary:", dict_example, "Type:", type(dict_example))

# 7. Set: Unordered collection of unique items
set_example = {1, 2, 3, 3, "orange"}  # Note: Duplicate 3 is ignored
print("Set:", set_example, "Type:", type(set_example))

# 8. Boolean: Represents True or False values
boolean_example = True
print("Boolean:", boolean_example, "Type:", type(boolean_example))

# 9. Complex: Represents numbers with real and imaginary parts
complex_example = 3 + 4j
print("Complex:", complex_example, "Type:", type(complex_example))

# 10. Range: Represents an immutable sequence of numbers, often used in loops
range_example = range(1, 5)  # Represents numbers from 1 to 4
print("Range:", list(range_example), "Type:", type(range_example))



# Integer: 42 Type: <class 'int'>
# Float: 3.14 Type: <class 'float'>
# String: Hello, Python! Type: <class 'str'>
# List: [1, 'apple', 3.5, True] Type: <class 'list'>
# Tuple: (10, 'banana', False) Type: <class 'tuple'>
# Dictionary: {'name': 'Ali', 'age': 25, 'city': 'Riyadh'} Type: <class 'dict'>
# Set: {'orange', 1, 2, 3} Type: <class 'set'>
# Boolean: True Type: <class 'bool'>
# Complex: (3+4j) Type: <class 'complex'>
# Range: [1, 2, 3, 4] Type: <class 'range'>