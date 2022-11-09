import json

import functions
import os
import expense

list_of_expenses = []
isExist = os.path.exists('json_data.txt')

if isExist:
    with open('json_data.txt','r') as r:
        list_of_expenses = json.load(r)

end_program = False

while not end_program:
    print('Hello! Welcome to The Expense Tracker')
    print('-------------------------------------')
    print('\n'
          'What would you like to do? Please select an option below:\n'
          '1) Review Expenses\n'
          '2) Add an Expense\n'
          '3) Edit an Expense\n'
          '4) Delete an Expense\n \n'
          'Press any other button to close'
          '\n')

    user_choice = input("Selection: ")

    match user_choice:
        case '1':
            os.system('cls')
            functions.review_expenses(list_of_expenses)
        case '2':
            os.system('cls')
            functions.add_expenses(list_of_expenses)
        case '3':
            os.system('cls')
            functions.edit_expenses(list_of_expenses)
        case other:
            end_program = True
