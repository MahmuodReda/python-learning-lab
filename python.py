
# Comprehensive example demonstrating operations on List, Tuple, Dictionary, Set, and Range
import time

# --- List Operations ---
# Lists are ordered, mutable collections that allow duplicates
print("\n=== List Operations ===")
my_list = [1, "apple", 3.5, True]
print("Original List:", my_list)

# 1. Append: Add an element to the end
my_list.append("orange")
print("After append:", my_list)

# 2. Insert: Add an element at a specific index
my_list.insert(1, 42)
print("After insert at index 1:", my_list)

# 3. Remove: Remove an element by value
my_list.remove("apple")
print("After remove 'apple':", my_list)

# 4. Pop: Remove and return element by index (default: last)
popped = my_list.pop()
print("Popped element:", popped, "List:", my_list)

# 5. Access by index
print("Element at index 0:", my_list[0])

# 6. Slice: Get a subset of the list
print("Slice [1:3]:", my_list[1:3])

# 7. Length
print("Length of list:", len(my_list))

# --- Tuple Operations ---
# Tuples are ordered, immutable collections that allow duplicates
print("\n=== Tuple Operations ===")
my_tuple = (10, "banana", False)
print("Original Tuple:", my_tuple)

# 1. Access by index
print("Element at index 1:", my_tuple[1])

# 2. Slice
print("Slice [0:2]:", my_tuple[0:2])

# 3. Length
print("Length of tuple:", len(my_tuple))

# 4. Count: Count occurrences of an element
print("Count of 'banana':", my_tuple.count("banana"))

# 5. Index: Get index of an element
print("Index of False:", my_tuple.index(False))

# Note: Tuples are immutable, so no append, remove, or modify operations

# --- Dictionary Operations ---
# Dictionaries are unordered (ordered in Python 3.7+), mutable collections of key-value pairs
print("\n=== Dictionary Operations ===")
my_dict = {"name": "Ali", "age": 25, "city": "Riyadh"}
print("Original Dictionary:", my_dict)

# 1. Add/Update a key-value pair
my_dict["job"] = "Engineer"
print("After adding job:", my_dict)

# 2. Access value by key
print("Value of 'name':", my_dict["name"])

# 3. Remove a key-value pair
del my_dict["age"]
print("After deleting 'age':", my_dict)

# 4. Get keys
print("Keys:", list(my_dict.keys()))

# 5. Get values
print("Values:", list(my_dict.values()))

# 6. Get items (key-value pairs)
print("Items:", list(my_dict.items()))

# 7. Length
print("Length of dictionary:", len(my_dict))

# --- Set Operations ---
# Sets are unordered, mutable collections of unique elements
print("\n=== Set Operations ===")
my_set = {1, 2, 3, "orange"}
print("Original Set:", my_set)

# 1. Add an element
my_set.add(4)
print("After adding 4:", my_set)

# 2. Remove an element
my_set.remove("orange")
print("After removing 'orange':", my_set)

# 3. Union with another set
other_set = {3, 4, 5}
print("Union with {3, 4, 5}:", my_set.union(other_set))

# 4. Intersection with another set
print("Intersection with {3, 4, 5}:", my_set.intersection(other_set))

# 5. Difference with another set
print("Difference with {3, 4, 5}:", my_set.difference(other_set))

# 6. Length
print("Length of set:", len(my_set))

# --- Range Operations ---
# Ranges are immutable sequences of numbers, often used in loops
print("\n=== Range Operations ===")
my_range = range(1, 5)  # Represents numbers 1, 2, 3, 4
print("Range as list:", list(my_range))

# 1. Access by index
print("Element at index 0:", my_range[0])

# 2. Slice
print("Slice [1:3]:", list(my_range[1:3]))

# 3. Length
print("Length of range:", len(my_range))

# 4. Use in a for loop
print("Looping through range:")
for num in my_range:
    print(num, end=" ")

# --- Search Time Comparison: List vs Set ---
print("\n\n=== Search Time Comparison: List vs Set ===")
# Create a large list and set with the same elements
large_list = list(range(1000000))
large_set = set(range(1000000))

# Search for an element in list
start_time = time.time()
999999 in large_list
list_time = time.time() - start_time
print("Time to search in list:", list_time, "seconds")

# Search for an element in set
start_time = time.time()
999999 in large_set
set_time = time.time() - start_time
print("Time to search in set:", set_time, "seconds")




# === List Operations ===
# Original List: [1, 'apple', 3.5, True]
# After append: [1, 'apple', 3.5, True, 'orange']
# After insert at index 1: [1, 42, 'apple', 3.5, True, 'orange']
# After remove 'apple': [1, 42, 3.5, True, 'orange']
# Popped element: orange List: [1, 42, 3.5, True]
# Element at index 0: 1
# Slice [1:3]: [42, 3.5]
# Length of list: 4

# === Tuple Operations ===
# Original Tuple: (10, 'banana', False)
# Element at index 1: banana
# Slice [0:2]: (10, 'banana')
# Length of tuple: 3
# Count of 'banana': 1
# Index of False: 2

# === Dictionary Operations ===
# Original Dictionary: {'name': 'Ali', 'age': 25, 'city': 'Riyadh'}
# After adding job: {'name': 'Ali', 'age': 25, 'city': 'Riyadh', 'job': 'Engineer'}
# Value of 'name': Ali
# After deleting 'age': {'name': 'Ali', 'city': 'Riyadh', 'job': 'Engineer'}
# Keys: ['name', 'city', 'job']
# Values: ['Ali', 'Riyadh', 'Engineer']
# Items: [('name', 'Ali'), ('city', 'Riyadh'), ('job', 'Engineer')]
# Length of dictionary: 3

# === Set Operations ===
# Original Set: {1, 2, 3, 'orange'}
# After adding 4: {1, 2, 3, 4, 'orange'}
# After removing 'orange': {1, 2, 3, 4}
# Union with {3, 4, 5}: {1, 2, 3, 4, 5}
# Intersection with {3, 4, 5}: {3, 4}
# Difference with {3, 4, 5}: {1, 2}
# Length of set: 4

# === Range Operations ===
# Range as list: [1, 2, 3, 4]
# Element at index 0: 1
# Slice [1:3]: [2, 3]
# Length of range: 4
# Looping through range:
# 1 2 3 4

# === Search Time Comparison: List vs Set ===
# Time to search in list: 0.006981372833251953 seconds
# Time to search in set: 0.0 seconds
