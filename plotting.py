import numpy as np
import matplotlib.pyplot as plt


def plot_test():
    x = np.arange(0, 3 * np.pi, 0.1)
    y = np.sin(x)
    plt.title("sin wave form")

    # Plot the points using matplotlib
    plt.plot(x, y)
    plt.show()


def plot_experiment():
    x = np.arange(0, 20)
    y = x * 2

    plt.plot(x, y)
    plt.xlabel("X-axis")
    plt.show()


def plot_net_income(monthly_income, expense_list, current_savings):
    future_months = int(input("How many months into the future do you want to calculate?\nMonths: "))
    monthly_money = []
    net_income = monthly_income
    for i in expense_list:
        net_income -= i[1]

    for i in range(future_months):
        monthly_money.append(net_income * i + 1)

    x = np.arange(0, future_months + 1)
    y = x * net_income + current_savings

    plt.plot(x, y)
    plt.xlabel("Months into the future")
    plt.ylabel("Money (in dollars)")
    plt.title("Savings Over Time")
    plt.show()


def plot_expenses(expense_list):
    expense_names = []
    for i in expense_list:
        expense_names.append(i[0])

    expense_amount = []
    for i in expense_list:
        expense_amount.append(i[1])

    legend_labels = []
    for i in expense_list:
        legend_labels.append(i[0] + " : $" + str(i[1]) + "/month")

    # Explode Data
    explode = []
    for i in expense_list:
        explode.append(0.0)

    # Creating Plot
    plt.rcParams["figure.figsize"] = [7.50, 3.50]
    plt.rcParams["figure.autolayout"] = True

    patches, texts = plt.pie(expense_amount, shadow=False, startangle=90)
    plt.legend(patches, legend_labels, loc="best")
    plt.axis('equal')

    # Legend

    plt.show()
