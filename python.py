#!/user/bin/python
# n="xxxxs"
# print(list(n))



# Ask the user for their name
name = input("What's your name? ")

# Ask the user for their age (as string)
age = input("How old are you? ")

# Convert the age from string to integer
age = int(age)

# Add 12 years to the current age
future_age = age + 12

# Print the result with the user's name
print("Hello " + name +" in 12 years you will be "+ str(future_age)+ " years old!")

