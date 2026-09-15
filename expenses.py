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
while move_on == "yes":
    amount = float(input("Enter the amount spent: "))
    category = input("Enter the category of the expense: ")
    description = input("Enter a description for the expense: ")

    new_expenses = {
        "amount": amount,
        "category": category,
        "description": description
    }
    move_on = input("Do you want to add another expense? (yes/no): ")
    expenses_list.append(new_expenses   )

print(expenses_list)
