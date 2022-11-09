class Expense:
    amount = None
    name = None

    def __init__(self, expense_name, expense_amount):
        self.name = expense_name
        self.amount = expense_amount