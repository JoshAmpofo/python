"""
Project 3: Building an Expense Tracker using Lambda functions
"""


def add_expense(expenses: float, amount: float, category: str):
    """
    Collect and add expense to tracker

    Args:
        expenses (float): expense
        amount (float): expense amount
        category (str): category of expense
    """
    expenses.append({'amount': amount, 'category': category})


def print_expenses(expenses: float) -> str:
    """
    Print expenses logged by user

    Args:
        expenses (float): expenses logged by user to be printed to screen
    """
    for expense in expenses:
        print(f"Amount: {expense['amount']}, Category: {expense['category']}")


def total_expenses(expenses: float) -> float:
    """
    Calculate and return the total expenses amount

    Args:
        expenses (float): expenses to calculate the sum
    
    Return:
        float: sum of expenses
    """
    return sum(map(lambda expense: expense['amount'], expenses))


def filter_expenses_by_category(expenses: float, category: str):
    """
    Filter and select expenses by their category

    Args:
        expenses (float): expenses.
        category (str): expense categories
    """
    return filter(lambda expense: expense['category'] == category, expenses)


def main():
    """
    Driver function
    """
    expenses = []
    while True:
        print('\nExpense Tracker\n')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter exxpenses by category')
        print('5. Exit')
        
        choice = input('\nEnter your choice: ')
        
        if choice == '1':
            amount = float(input('Enter amount: '))
            category = input('Enter category: ')
            add_expense(expenses, amount, category)
            print('\nExpense added!')
        
        elif choice == '2':
            print('\nAll Expenses:')
            print_expenses(expenses)
        
        elif choice == '3':
            print('\nTotal Expenses: ', total_expenses(expenses))
        
        elif choice == '4':
            category = input('Enter category to filter: ')
            print(f'\nExpenses for {category}: ')
            expenses_from_category = filter_expenses_by_category(expenses, category)
            print_expenses(expenses_from_category)
        
        elif choice == '5':
            print('Exiting the program. Goodbye!\n')
            break


if __name__ == '__main__':
    main()