import json
import plotting
import functions
import os

list_of_expenses = []
monthly_income = 0
current_savings = 0
is_exist_expenses = os.path.exists('json_expenses.txt')
is_exist_income = os.path.exists('json_income.txt')
is_exist_savings = os.path.exists('json_savings.txt')

if is_exist_expenses:
    with open('json_expenses.txt', 'r') as r:
        list_of_expenses = json.load(r)

if is_exist_income:
    with open('json_income.txt', 'r') as r:
        monthly_income = json.load(r)

if is_exist_savings:
    with open('json_savings.txt', 'r') as r:
        current_savings = json.load(r)

end_program = False

while not end_program:
    print('Hello! Welcome to The Expense Tracker')
    print('-------------------------------------')
    print('\n'
          'What would you like to do? Please select an option below:\n'
          '1) Review Expenses\n'
          '2) Add an Expense\n'
          '3) Edit an Expense\n'
          '4) Delete an Expense\n'
          '5) Set Monthly Income\n'
          '6) Set Current Savings\n'
          '7) Calculate Savings Over Time\n'
          '8) Visualize Expense Relations\n'
          '9) Manipulate Data\n \n'
          'Enter anything else to close'
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
        case '4':
            os.system('cls')
            functions.delete_expense(list_of_expenses)
        case '5':
            os.system('cls')
            monthly_income = functions.add_income()
        case '6':
            os.system('cls')
            current_savings = functions.set_current_savings()
        case '7':
            os.system('cls')
            plotting.plot_net_income(monthly_income, list_of_expenses, current_savings)
        case '8':
            os.system('cls')
            plotting.plot_expenses(list_of_expenses)
        case '9':
            os.system('cls')
            functions.data_manipulation(list_of_expenses)
        case other:
            end_program = True
