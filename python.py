#!/usr/bin/python

# -------------------------------
print("1. FOR loop with break")
# -------------------------------
# Loop through numbers 0 to 9
# Break the loop when i equals 5
for i in range(10):
    if i == 5:
        print("Breaking at", i)
        break
    print("i =", i)

print("\n-------------------------------\n")

# -------------------------------
print("2. FOR loop with continue")
# -------------------------------
# Skip printing when i equals 2
for i in range(5):
    if i == 2:
        print("continue")
        continue  # Skip this iteration
    print("i =", i)

print("\n-------------------------------\n")

# -------------------------------
print("3. FOR loop with else (no break)")
# -------------------------------
# The else block will run because the loop finishes normally (no break)
for i in range(5):
    print(i)
else:
    print("FOR loop finished without break.")

print("\n-------------------------------\n")

# -------------------------------
print("4. FOR loop with break + else")
# -------------------------------
# The else block will NOT run because the loop ends with a break
for i in range(5):
    print(i)
    if i == 3:
        break
else:
    print("FOR loop finished without break.")

print("\n-------------------------------\n")

# -------------------------------
print("5. WHILE loop with break")
# -------------------------------
# Count from 0 and break when x equals 5
x = 0
while x < 10:
    if x == 5:
        print("Breaking at", x)
        break
    print("x =", x)
    x += 1

print("\n-------------------------------\n")

# -------------------------------
print("6. WHILE loop with continue")
# -------------------------------
# Skip printing when x equals 3
x = 0
while x < 5:
    x += 1
    if x == 3:
        continue  # Skip this iteration
    print("x =", x)

print("\n-------------------------------\n")

# -------------------------------
print("7. WHILE loop with else (no break)")
# -------------------------------
# The else block runs because the loop ends normally
x = 0
while x < 3:
    print("x =", x)
    x += 1
else:
    print("WHILE loop ended normally.")

print("\n-------------------------------\n")

# -------------------------------
print("8. WHILE loop with break + else")
# -------------------------------
# The else block does NOT run because break was used
x = 0
while x < 5:
    if x == 2:
        break
    print("x =", x)
    x += 1
else:
    print("WHILE loop ended without break.")

print("\n-------------------------------\n")



# 1. FOR loop with break
# i = 0
# i = 1
# i = 2
# i = 3
# i = 4
# Breaking at 5

# -------------------------------

# 2. FOR loop with continue
# i = 0
# i = 1
# continue
# i = 3
# i = 4

# -------------------------------

# 3. FOR loop with else (no break)
# 0
# 1
# 2
# 3
# 4
# FOR loop finished without break.

# -------------------------------

# 4. FOR loop with break + else
# 0
# 1
# 2
# 3

# -------------------------------

# 5. WHILE loop with break
# x = 0
# x = 1
# x = 2
# x = 3
# x = 4
# Breaking at 5

# -------------------------------

# 6. WHILE loop with continue
# x = 1
# x = 2
# x = 4
# x = 5

# -------------------------------

# 7. WHILE loop with else (no break)
# x = 0
# x = 1
# x = 2
# WHILE loop ended normally.

# -------------------------------

# 8. WHILE loop with break + else
# x = 0
# x = 1

# -------------------------------