expenses_list = []

def add_expense():
    amount = float(input("Enter the amount spent: "))
    category = input("Enter the category of the expense: ")
    description = input("Enter a description for the expense: ")

    # Create a dictionary to store the expense details
    expense = {   
        "amount": amount,
        "category": category,
        "description": description
        }
    
    expenses_list.append(expense)
    # Ask the user if they want to add another expense
    move_on = input("Do you want to add another expense? (yes/no): ")
  
# Loop to allow the user to add multiple expenses
    while move_on == "yes":
        amount = float(input("Enter the amount spent: "))
        category = input("Enter the category of the expense: ")
        description = input("Enter a description for the expense: ")

        new_expense = {
            "amount": amount,
            "category": category,
            "description": description
        }
        move_on = input("Do you want to add another expense? (yes/no): ")
        expenses_list.append(new_expense)
# Print all the expenses entered by the user
        for expense in expenses_list:
            print(expense)
def view_expenses():
# Print all the expenses in the list
    for expense in expenses_list:
        print(expense)
def total_expenses():
# Calculate the total amount spent and the total amount
    total_amount = sum(expense["amount"] for expense in expenses_list)
    print(f"Total amount spent: {total_amount}")

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
        print(f"{category}: {total}")
def delete_expense():
# delete an expense from the list
    delete_expense = input("Do you want to delete an expense? (yes/no): ")
    if delete_expense == "yes":
        expense_index = int(input("Enter the index of the expense to delete (starting from 0): "))
        if 0 <= expense_index < len(expenses_list):
            deleted_expense = expenses_list.pop(expense_index)
            print(f"Deleted expense: {deleted_expense}")
        else:
            print("Invalid index. No expense deleted.")


print("==== Welcome to the Expense Tracker! ====")
print("1. Add an expense")
print("2. View all expenses")
print("3. View total amount spent")
print("4. View total amount spent by category")
print("5. Delete an expense")
print("6. Exit")

user_choice = int(input("Please select an option (1-6): "))
allowed_choices = [1, 2, 3, 4, 5, 6]
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
if user_choice == 6:
    print("Exiting the program. Goodbye!")
    exit()

while user_choice not in allowed_choices:
    print("Invalid choice. Please select a valid option (1-6).")
    print("1. Add an expense")
    print("2. View all expenses")
    print("3. View total amount spent")
    print("4. View total amount spent by category")
    print("5. Delete an expense")
    print("6. Exit")

    user_choice = int(input("Please select an option (1-6): "))
    allowed_choices = [1, 2, 3, 4, 5, 6]
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
    if user_choice == 6:
        print("Exiting the program. Goodbye!")
        exit()