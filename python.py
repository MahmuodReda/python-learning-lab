from tkinter import *  # Import all tkinter classes

# Define the function that runs when an item is selected
def items_selected(event):
    selected_index = Lb.curselection()  # Get the index of the selected item(s)
    print(selected_index)               # Print the index (as a tuple)
    print(Lb.get(selected_index))       # Print the actual item text

# Create the main window
top = Tk()

# Create a Listbox widget inside the window
Lb = Listbox(top)

# Insert items into the Listbox
Lb.insert(0, 'Python')      # Insert 'Python' at index 0
Lb.insert(1, 'C')           # Insert 'C' at index 1
Lb.insert(2, 'Java')        # Insert 'Java' at index 2
Lb.insert(3, 'Any other')   # Insert 'Any other' at index 3

# Add the Listbox to the window
Lb.pack()

# Bind the selection event to the handler function
Lb.bind('<<ListboxSelect>>', items_selected)

# Start the GUI event loop
top.mainloop()
