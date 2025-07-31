#!/usr/bin/python
import os
import pyautogui
import time

# Safely get the Desktop path
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# Ensure Desktop directory exists
if not os.path.exists(desktop_path):
    os.makedirs(desktop_path)

# Define the file path
filename = os.path.join(desktop_path, "contact_info.txt")

# Write your info
name = "Mahmood Reda"
email = "mr4141705@gmail.com"

with open(filename, "w", encoding="utf-8") as file:
    file.write(f"Name: {name}\n")
    file.write(f"E-mail: {email}\n")

print(f"✅ File created at: {filename}")

# Open file automatically using pyautogui
time.sleep(2)
pyautogui.press("win")
time.sleep(3)
pyautogui.write(r"C:\Users\MAHMOOD_REDA\Desktop\contact_info.txt", interval=0.05)
time.sleep(2)
pyautogui.press("enter")

