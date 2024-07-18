'''1. The Calculator App
Objective: The aim of this assignment is to build a basic calculator that can perform addition, subtraction, multiplication, and division.

Task 1: Create functions for each arithmetic operation.

Task 2: Use inputs to ask the user what operation they want to perform, and what numbers they want to use.

Task 3: Ensure your code can handle division by zero and other potential errors. So if you divide by 0, there is error handling set up to prevent an error from showing in the console.
'''

def add(numbers):
    for num in numbers[1:]:
        if len(numbers) < 3:
            total = numbers[0]
            total += num
            print(f"{numbers[0]}", num, sep=" + ", end="")
            print(f" = {total}")
            totals.append(total)     
        else:
            total = totals[0] if len(totals) < 1 else totals[-1]
            total = sum(numbers)
            print(f"{totals[-1]}", f"{numbers[-1]}", sep=" + ", end="")
            print(f" = {total}") 
            totals.append(total)
        return total

def subtract(numbers):
    for num in numbers[1:]:
        if len(numbers) < 3:
            difference = numbers[0]
            difference -= num
            print(f"{numbers[0]}", num, sep=" - ", end="")
            print(f" = {difference}")
            differences.append(difference)
        else:
            difference = differences[0] if len(differences) < 1 else differences[-1]
            difference -= numbers[-1]
            print(f"{differences[-1]}", f"{numbers[-1]}", sep=" - ", end="")
            print(f" = {difference}")
            differences.append(difference)
        return difference

def multiply(numbers):
    for num in numbers[1:]:
        if len(numbers) < 3:
            product = numbers[0]
            product *= num
            print(f"{numbers[0]}", num, sep=" * ", end="")
            print(f" = {product}")
            products.append(product)
        else:
            product = products[0] if len(products) < 1 else products[-1] 
            product *= numbers[-1]
            print(f"{products[-1]}", f"{numbers[-1]}", sep=" * ", end="")
            print(f" = {product}")
            products.append(product)
        return product

def divide(numbers):
    for i, num in enumerate(numbers[1:]):
        if len(numbers) < 3:
            quotient = numbers[0]
            quotient /= num
            quotients.append(quotient)
            print(f"{numbers[0]}", num, sep=" / ", end="")
            print(f" = {quotient}")    
        else:
            quotient = quotients[i-1] if numbers[1] > 0 else numbers[0]
            quotient /= numbers[-1] 
            print(f"{quotients[-1]}", f"{numbers[-1]}", sep=" / ", end="")
            print(f" = {quotient}")
            quotients.append(quotient)
        return quotient
            
numbers = []
totals = []
differences = []
products = []
quotients = []

operation_input = input("\nEnter the operation you want to calculate with: (Type 'add', 'subtract', 'multiply' or 'divide') ").lower()

accepted_answers = ['add', 'subtract', 'multiply', 'divide']

while True:

    try:
        if operation_input not in accepted_answers:
            print("\nInvalid operation. Try again.")
            operation_input = input("\nEnter the operation you want to calculate with: (Type 'add', 'subtract', 'multiply' or 'divide') ").lower()
        elif operation_input in accepted_answers:
            user_numbers = input("\nEnter a number or 'done' to finish: ").lower()
            if user_numbers == 'done':
                break
            elif user_numbers == 0 and operation_input == 'divide':
               continue
            else:
                values = int(user_numbers)
                numbers.append(values)
            
        if operation_input == 'add':
            add(numbers)
        elif operation_input == 'subtract':
            subtract(numbers)
        elif operation_input == 'multiply':
            multiply(numbers)
        elif operation_input == 'divide':
            divide(numbers)

    except ValueError:
        print("Invalid Input. Enter a number or 'done' to finish. ")
        continue
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed. Try a different number.")
        continue

    

    

