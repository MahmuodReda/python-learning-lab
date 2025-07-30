#!/usr/bin/python

import src.Cal as firelink

while True:
    print("\nChoose a website to open:")
    print("1. Facebook")
    print("2. YouTube")
    print("3. GitHub")
    print("4. LinkedIn (Mahmood Reda)")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        firelink.firefox(firelink.facebook_link)
    elif choice == "2":
        firelink.firefox(firelink.youtube_link)
    elif choice == "3":
        firelink.firefox(firelink.github_link)
    elif choice == "4":
        firelink.firefox(firelink.linkedin_link)
    elif choice == "0":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
