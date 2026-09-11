amount = float(input("Enter the amount spent: "))
category = input("Enter the category of the expense: ")
description = input("Enter a description for the expense: ")

expenses = {   
"amount": amount,
"category": category,
"description": description
}

amount = float(input("Enter the amount spent: "))
category = input("Enter the category of the expense: ")
description = input("Enter a description for the expense: ")

expenses2 = {
    "amount": amount,
     "category": category,
     "description": description
}

expenses_list = [expenses, expenses2]

print(expenses_list[0])
print(expenses_list[1])
