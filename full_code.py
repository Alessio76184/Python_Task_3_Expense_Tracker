# adding expenses to the list
def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})

def print_expenses(expenses):
    for expense in expenses:
        # f' allows you to integrate variables into text much neater than the str.format()
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')
    
def total_expenses(expenses):
    # map is an easy way to apply a fuction to a list without creating loops.
    # lambda a one off function used to pass a function as an argument to fuctions like map(), filter(), or sorted(). Perfect for simple operations. 
    # This will sum all expenses
    return sum(map(lambda expense: expense['amount'], expenses))
    
def filter_expenses_by_category(expenses, category):
    # creates a filter showing only expenses which result in true for a 'category' match
    return filter(lambda expense: expense['category'] == category, expenses)

def main():
    expenses = []
    while True:
        #\n is to create a new line then list potential options for the user to choose
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')
        
        choice = input('Enter your choice: ')

        if choice == '1':
            amount = float(input('Enter amount: '))
            category = input('Enter category: ')
            add_expense(expenses, amount, category)

        elif choice == '2':
            print('\nAll Expenses:')
            print_expenses(expenses)

        elif choice == '3':
            print('\nTotal Expenses: ', total_expenses(expenses))

        elif choice == '4':
            category = input('Enter category to filter: ')
            print(f'\nExpenses for {category}:')
            expenses_from_category = filter_expenses_by_category(expenses, category)
            print_expenses(expenses_from_category)

        elif choice == '5':
            print('Exiting the program.')
            break
if __name__ == '__main__':
    main()
