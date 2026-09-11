amount = float(input("Enter the amount spent: "))
category = input("Enter the category of the expense: ")
description = input("Enter a description for the expense: ")

expenses = {   
"amount": amount,
"category": category,
"description": description
}

move_on = input("Do you want to add another expense? (yes/no): ")
expenses_list = [expenses]

print(expenses_list[0])
if move_on == "yes":
    amount = float(input("Enter the amount spent: "))
    category = input("Enter the category of the expense: ")
    description = input("Enter a description for the expense: ")

    expenses2 = {
        "amount": amount,
        "category": category,
        "description": description
    }
    expenses_list.append(expenses2)

print(expenses_list)

