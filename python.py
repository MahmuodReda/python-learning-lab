#!/user/bin/python# Check if a character is in a string
name = "Mahmoud"

print("M" in name)      # True
print("z" in name)      # False
print("a" not in name)  # False



fruits = ["apple", "banana", "orange"]

print("banana" in fruits)      # True
print("grape" not in fruits)   # True

x=10
y=10
print("x is y:", x is y)  # True 
print("id(x):", id(x))
print("id(y):", id(y))


y=20
print("x is y:", x is y)  # False 
print("id(x):", id(x))
print("id(y):", id(y))


# Define lists
a = [1, 2, 3]
b = a              # b points to the same list as a
c = [1, 2, 3]      # c is a new list with the same content
d = [1, 2, 3, 4]   # d has different content

# Compare with 'is' (identity)
print("a is b:", a is b)  # True - same object
print("a is c:", a is c)  # False - different objects, same values
print("a is d:", a is d)  # False - different objects

# Compare with '==' (equality)
print("a == c:", a == c)  # True - same content
print("a == d:", a == d)  # False - different content

# Compare with 'is not'
print("a is not c:", a is not c)  # True

# Print memory addresses using id()
print("id(a):", id(a))
print("id(b):", id(b))
print("id(c):", id(c))
print("id(d):", id(d))



# True
# False
# False
# True
# True
# x is y: True
# id(x): 140734356339416
# id(y): 140734356339416
# x is y: False
# id(x): 140734356339416
# id(y): 140734356339736
# a is b: True
# a is c: False
# a is d: False
# a == c: True
# a == d: False
# a is not c: True
# id(a): 1680602288512
# id(b): 1680602288512
# id(c): 1680605064064
# id(d): 1680605060224
