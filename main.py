import json
expenses_list = []

with open("expenses.json", "r") as file:
    expenses_list = json.load(file)
def get_expense():

def add_expense():
    amount = input("Enter the amount spent: ").strip()
    while type(amount) != float:
        try:
            amount = float(amount)
        except ValueError:
            amount = input("Invalid input. Please enter a valid number for the amount spent: ")

    category = input("Enter the category of the expense: ").strip()
    while category is "":
        print("invalid input")
        category = input("Enter the category of the expense: ").strip()
    description = input("Enter a description for the expense: ").strip()
    while description is "":
        print("invalid input")
        description = input("Enter a description for the expense: ").strip()


    # Create a dictionary to store the expense details
    expense = {   
        "amount": amount,
        "category": category,
        "description": description
        }
    
    expenses_list.append(expense)
    # Ask the user if they want to add another expense
    move_on = input("Do you want to add another expense? (yes/no): \n").lower().strip()
    with open("expenses.json", "w") as file:
        json.dump(expenses_list, file, indent=4)

# Loop to allow the user to add multiple expenses
    while move_on == "yes":
        amount = float(input("Enter the amount spent: "))
        
        category = input("Enter the category of the expense: ").strip()
        while category is "":
            print("invalid input")
            category = input("Enter the category of the expense: ").strip()
            
        description = input("Enter a description for the expense: ").strip()
    while description is "":
        print("invalid input")
        description = input("Enter a description for the expense: ").strip()

        new_expense = {
            "amount": amount,
            "category": category,
            "description": description
        }
        move_on = input("Do you want to add another expense? (yes/no): \n").lower()
        expenses_list.append(new_expense)
        with open("expenses.json", "w") as file:
                    json.dump(expenses_list, file, indent=4)
#
def view_expenses():
# Print all the expenses in the list
    for index, expense in enumerate(expenses_list, start=1):
        print(f"Expense #{index}")
        print(f"Amount: ₦{expense['amount']}")
        print(f"Category: {expense['category']}")
        print(f"Description: {expense['description']}\n")

def total_expenses():
# Calculate the total amount spent and the total amount
    total_amount = sum(expense["amount"] for expense in expenses_list)
    print(f"Total amount spent: {total_amount}\n")

def total_expenses_by_category():
# Calculate the total amount spent in each category
    category_totals = {}
    for expense in expenses_list:
        category = expense["category"]
        amount = expense["amount"]
        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount
        
    for category, total in category_totals.items():
        print(f"{category}: {total}\n")
def delete_expense():
# delete an expense from the list
    for index, expense in enumerate(expenses_list, start=1):
        print(f"Expense #{index}")
        print(f"Amount: ₦{expense['amount']}")
        print(f"Category: {expense['category']}")
        print(f"Description: {expense['description']}\n")
        
    expense_index = int(input("Enter the index of the expense to delete (starting from 1), (0 for back): "))
    if 1 <= expense_index <= len(expenses_list):
            deleted_expense = expenses_list.pop(expense_index - 1)
            with open("expenses.json", "w") as file:
                json.dump(expenses_list, file, indent=4)
                print(f"Deleted expense: {deleted_expense}")
    elif expense_index == 0:
        print("Back to menu")
    else:
        print("Invalid index. No expense deleted.\n")

while True:
    print("==== Welcome to the Expense Tracker! ====")
    print("1. Add an expense")
    print("2. View all expenses")
    print("3. View total amount spent")
    print("4. View total amount spent by category")
    print("5. Delete an expense")
    print("6. Exit\n")

    user_choice = input("Please select an option (1-6): ")
    while type(user_choice) != int:
        try:
            user_choice = int(user_choice)
        except ValueError:
            user_choice = input("Invalid input. Please enter a valid number: ")


    if user_choice == 1:
        print("You selected: Add an expense")
        add_expense()
    elif user_choice == 2:
        print("You selected: View all expenses")
        view_expenses()
    elif user_choice == 3:
        print("You selected: View total amount spent")
        total_expenses()
    elif user_choice == 4:
        print("You selected: View total amount spent by category")
        total_expenses_by_category()
    elif user_choice == 5:
        print("You selected: Delete an expense")
        delete_expense()
    elif user_choice == 6:
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option (1-6).")
