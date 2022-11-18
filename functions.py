# This contains all the important functions for the main program
import os
import json
from os import system, name


def clear():
    # For Windows
    if name == 'nt':
        _ = system('cls')

    # For Mac and Linux
    else:
        _ = system('clear')


def empty_list_check(expense_list):
    if len(expense_list) == 0:
        print("Whoops! There's nothing here yet! Try adding some expenses first.")
        return True
    else:
        return False


def input_number(text):
    bad_input = True
    while bad_input:
        temp = input(text)
        try:
            temp = float(temp)
            bad_input = False
            return temp
        except:
            print("Sorry, you have to enter a number!")


def json_expense_update(expense_list):
    json_expense_list = json.dumps(expense_list)
    with open('json_expenses.txt', 'w') as f:
        f.write(json_expense_list)

    clear()
    return


def json_income_update(monthly_income):
    json_monthly_income = json.dumps(monthly_income)
    with open('json_income.txt', 'w') as f:
        f.write(json_monthly_income)

    clear()
    return


def json_savings_update(current_savings):
    json_current_savings = json.dumps(current_savings)
    with open('json_savings.txt', 'w') as f:
        f.write(json_current_savings)

    clear()
    return


def expense_edit_choice(user_edit_choice, expense_list, editor):
    match editor:
        case 1:
            print('Editing Name...\n')
            print('What would you like the new name to be?')
            expense_list[user_edit_choice][0] = input('New Name: ')
            json_expense_update(expense_list)

            clear()
            print('Name Changed!')
            input('Press Enter to continue...')
        case 2:
            print('Editing Cost...\n')
            print('What would you like the new cost to be? ')
            expense_list[user_edit_choice][1] = input_number("Cost: $")
            json_expense_update(expense_list)

            clear()
            print('Cost Changed!')
            input('Press Enter to continue...')


def review_expenses(expense_list):
    if len(expense_list) == 0:
        print("Whoops! There's nothing here yet! Try adding some expenses first.")
    else:
        print("Expenses")
        print('-----------------')
        for i in expense_list:
            print(f'Name: {i[0]}')
            print(f'Cost: ${i[1]}/month\n')
            print('=========================================\n')

    input('Press Enter to continue...')
    clear()
    return


def add_expenses(expense_list):
    print('Adding an expense...\n'
          '\n'
          'What is the name of this expense?')
    name_input = input('Name: ')

    # Get the Cost
    print('\n'
          'How much is the expense every month?')
    cost_input = input_number("Cost: $")

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

        clear()
        print("What about this expense would you like to edit?\n"
              "\n"
              f"1) Name: {expense_list[user_edit_choice][0]}\n"
              f"2) Cost: ${expense_list[user_edit_choice][1]}/month\n\n")

        editor = float(input("Selection: "))

        clear()
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


def set_current_savings():
    print("Set your current savings.")
    current_savings = float(input("How much money do you currently have saved? : $"))
    json_savings_update(current_savings)
    return current_savings


# Manipulate Data

def data_manipulation(expense_list):
    print('\n'
          'How would you like to manipulate the expense data? Please select an option below:\n'
          '1) Check the number and total of expenses\n'
          '2) Sort Expenses\n'
          '3) Find Largest Expense\n'
          '4) Find Smallest Expense\n \n'
          'Enter anything else to close'
          '\n')

    user_choice = input("Selection: ")

    match user_choice:
        case '1':
            clear()
            expense_total(expense_list)
        case '2':
            clear()
            expense_sort(expense_list)
        case '3':
            clear()
            expense_find_largest(expense_list)
        case '4':
            clear()
            expense_find_smallest(expense_list)
        case other:
            pass


def expense_total(expense_list):
    if not empty_list_check(expense_list):
        total = 0
        for i in expense_list:
            total += i[1]

        print("There are a total of " + str(len(expense_list)) + " expenses in the list.")
        print("They total $" + str(total) + "/month")
        input("Press Enter to continue...")


def expense_sort(expense_list):
    print('\n'
          'How would you like to sort the data? Please select an option below:\n'
          '1) Sort from least to greatest\n'
          '2) Sort from greatest to least\n \n'
          'Enter anything else to close'
          '\n')

    user_choice = input("Selection: ")
    clear()

    match user_choice:
        case '1':
            if len(expense_list) == 0:
                print("Whoops! There's nothing here yet! Try adding some expenses first.")
            else:
                target = 0
                sorted_list_name = []
                sorted_list_amount = []
                for i in expense_list:
                    sorted_list_name.append(i[0])
                    sorted_list_amount.append(i[1])
                sorted_list_amount.sort()
                print("Expenses Sorted!")
                print('-----------------')

                for i in range(len(expense_list)):
                    target_found = False
                    while not target_found:
                        for j in range(len(expense_list)):
                            if expense_list[j][1] == sorted_list_amount[i]:
                                target = j
                                target_found = True

                    print(f'Name: {expense_list[target][0]}')
                    print(f'Cost: ${sorted_list_amount[i]}/month\n')
                    print('=========================================\n')

            input('Press Enter to continue...')
            clear()
        case '2':
            if len(expense_list) == 0:
                print("Whoops! There's nothing here yet! Try adding some expenses first.")
            else:
                target = 0
                sorted_list_name = []
                sorted_list_amount = []
                for i in expense_list:
                    sorted_list_name.append(i[0])
                    sorted_list_amount.append(i[1])
                sorted_list_amount.sort(reverse=True)
                print("Expenses Sorted!")
                print('-----------------')

                for i in range(len(expense_list)):
                    target_found = False
                    while not target_found:
                        for j in range(len(expense_list)):
                            if expense_list[j][1] == sorted_list_amount[i]:
                                target = j
                                target_found = True

                    print(f'Name: {expense_list[target][0]}')
                    print(f'Cost: ${sorted_list_amount[i]}/month\n')
                    print('=========================================\n')

            input('Press Enter to continue...')
            clear()
        case other:
            pass


def expense_find_largest(expense_list):
    sorted_list_amount = []
    for i in expense_list:
        sorted_list_amount.append(i[1])

    largest_expense = max(sorted_list_amount)
    index = sorted_list_amount.index(largest_expense)
    print(
        f"The largest expense is {expense_list[index][0]}"
        f"which is costing ${largest_expense}/month.")

    input("Press Enter to Continue...")


def expense_find_smallest(expense_list):
    sorted_list_amount = []
    for i in expense_list:
        sorted_list_amount.append(i[1])

    smallest_expense = min(sorted_list_amount)
    index = sorted_list_amount.index(smallest_expense)
    print(
        f"The smallest expense is {expense_list[index][0]}"
        f"which is costing ${smallest_expense}/month.")

    input("Press Enter to Continue...")
