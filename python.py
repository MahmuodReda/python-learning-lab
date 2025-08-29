#!/user/bin/python
import threading   # Import threading library to create threads
from time import sleep   # Import sleep function to pause execution

# Task 1 function
def task1():
    while True:  # Infinite loop
        print("Task 1")   # Print message
        sleep(1)          # Pause for 1 second

# Task 2 function
def task2():
    while True:  # Infinite loop
        print("Task 2")   # Print message
        sleep(1)          # Pause for 1 second

# Create and start threads
t1 = threading.Thread(target=task1)   # Create thread for task1
t2 = threading.Thread(target=task2)   # Create thread for task2

t1.start()  # Start thread 1
t2.start()  # Start thread 2

# Main thread work
while True:  
    print("Main Thread")   # Print message for main thread
    sleep(1)               # Pause for 1 second
