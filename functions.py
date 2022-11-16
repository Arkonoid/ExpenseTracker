# This contains all the important functions for the main program
import os
import json


def json_expense_update(expense_list):
    json_expense_list = json.dumps(expense_list)
    with open('json_expenses.txt', 'w') as f:
        f.write(json_expense_list)

    os.system('cls')
    return


def json_income_update(monthly_income):
    json_monthly_income = json.dumps(monthly_income)
    with open('json_income.txt', 'w') as f:
        f.write(json_monthly_income)

    os.system('cls')
    return


def expense_edit_choice(user_edit_choice, expense_list, editor):
    match editor:
        case 1:
            print('Editing Name...\n')
            print('What would you like the new name to be?')
            expense_list[user_edit_choice][0] = input('New Name: ')
            json_expense_update(expense_list)

            os.system('cls')
            print('Name Changed!')
            input('Press Enter to continue...')
        case 2:
            print('Editing Cost...\n')
            print('What would you like the new cost to be?')
            expense_list[user_edit_choice][1] = int(input("New Cost: $"))
            json_expense_update(expense_list)

            os.system('cls')
            print('Cost Changed!')
            input('Press Enter to continue...')


def review_expenses(expense_list):
    if len(expense_list) == 0:
        print("Whoops! There's nothing here yet! Try adding some expenses first.")
        input('Press Enter to continue...')
    else:
        print("Expenses")
        print('-----------------')
        for i in expense_list:
            print(f'Name: {i[0]}')
            print(f'Cost: ${i[1]}/month\n')
            print('=========================================\n')

    input('Press Enter to continue...')
    return


def add_expenses(expense_list):
    print('Adding an expense...\n'
          '\n'
          'What is the name of this expense?')
    name_input = input('Name: ')

    # Get the Cost
    print('\n'
          'How much is the expense every month?')
    cost_input = float(input('Cost: $'))

    added_expense = [name_input, cost_input]
    expense_list.append(added_expense)

    # Update JSON
    json_expense_update(expense_list)

    print("Expense Added!")
    input("Press Enter to continue...")
    return


def edit_expenses(expense_list):
    if len(expense_list) == 0:
        print("You need to add some expenses before you can edit them!")
        input("Press Enter to continue...")
    else:
        print("Editing an expense...\n")

        for i in expense_list:
            print(f'{expense_list.index(i) + 1}) Name: {i[0]} || Cost: ${i[1]}/month')

        print("Enter the number of the expense you would like to edit.")
        user_edit_choice = int(input("Selection: ")) - 1

        os.system('cls')
        print("What about this expense would you like to edit?"
              ""
              f"1) Name: {expense_list[user_edit_choice][0]}"
              f"2) Cost: ${expense_list[user_edit_choice][1]}/month")

        editor = float(input("Selection: "))

        os.system('cls')
        expense_edit_choice(user_edit_choice, expense_list, editor)


def delete_expense(expense_list):
    if len(expense_list) == 0:
        print("You need to add some expenses before you can delete them!")
        input("Press Enter to continue...")
    else:
        print("Deleting an expense...\n")

        for i in expense_list:
            print(f'{expense_list.index(i) + 1}) Name: {i[0]} || Cost: ${i[1]}/month')

        print("Enter the number of the expense you would like to delete.")
        user_delete_choice = int(input("Selection: ")) - 1

        confirmation = False

        while not confirmation:
            print('Are you sure? (y/n)')
            user_confirmation = input('Selection: ')

            if user_confirmation == 'y' or user_confirmation == 'Y':
                confirmation = True
                expense_list.remove(expense_list[user_delete_choice])
                json_expense_update(expense_list)
                input("Expense Deleted\nPress Enter to continue...")
            elif user_confirmation == 'n' or user_confirmation == 'N':
                confirmation = True
                input("Aborting deletion\nPress Enter to continue...")
            else:
                print("Incorrect choice. Please choose 'y' or 'Y' for Yes/'n' or 'N' for No")


def add_income():
    print("Set your monthly income.")
    monthly_income = int(input("How much do you make a month? (Rounded to nearest dollar): $"))
    json_income_update(monthly_income)
    return monthly_income


def print_monthly_income(monthly_income):
    print(f'${monthly_income}')
    return


def calculate_net_income(monthly_income, expense_list):
    net_income = monthly_income

    for i in expense_list:
        net_income = float(net_income) - float(i[1])

    print("The net income after expenses is: $" + str(net_income))
