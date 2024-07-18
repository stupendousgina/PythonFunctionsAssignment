'''2. The Shopping List Maker
Objective: The aim of this assignment is to create a program that helps users make a shopping list.

Task 1: Write a function that lets the user add items to a list.

Task 2: Include a function to remove items from the list.

Task 3: Add a function that prints out the entire list in a formatted way.

Note: The goal of this is to be a program. The recommendation is to use a while loop that will allow the user to continue to add, remove, and print off their shopping list until they decide to "quit", also known as breaking the loop.'''
shopping_list = []

def add_items(new_item):
    global shopping_list
    shopping_list.append(new_item)

def remove_items(item_to_remove):
    global shopping_list
    shopping_list.remove(item_to_remove)

def display_items():
    global shopping_list
    print(f"Current shopping List:")
    for item in shopping_list:
        print(item)

def shopping_list_maker():
    while True:
        print("\nShopping List Helper")
        print("1. Add an item.")
        print("2. Remove an item.")
        print("3. Display your shopping list.")
        print("4. Done\n")
        action = input("Choose an option: ")
        if action == '1':
            new_item = input("Enter the new item: ")
            add_items(new_item)
        elif action == '2':
            item_to_remove = input("Enter the item to remove: ")
            if item_to_remove in shopping_list:
                remove_items(item_to_remove)
                print(f"{item_to_remove} has been removed your shopping list.")
            else:
                print(f"{item_to_remove} was not in your shopping list.")
        elif action == '3':
            display_items()
        elif action == '4':
            print("Finished with Shopping List Helper.")
            break
        else:
            print("Invalid action. Choose again.")
            continue
shopping_list_maker()

