# we will store a dict with category as a key and expense as a value
user_expenses = {}


def add_expense(amount, category):
    if category.lower() not in list(user_expenses.keys()):
        user_expenses[category] = 0

    user_expenses[category.lower()] += amount

def view_total_spent():
    total_spent = 0

    for amount in user_expenses.values():
        total_spent += amount

    print(total_spent)

def view_per_category_expense():
    for category, amount in user_expenses.items():
        print(f"You have spent {amount} on {category} as of now.")

close_expense_book = False

while not close_expense_book:
    user_option = input("""What do u wanna do? 1,2,3 or 4?
    1.leave the program
    2.add expenses
    3.view per category expense
    4.view total expenses\n""")

    if user_option == "1":
        close_expense_book = True
    elif user_option == "2":
        amt_of_exp = int(input("how much did u spend? \n"))
        cat_of_exp = input("what did u spent the money on? \n")
        add_expense(amt_of_exp,cat_of_exp)
        print("Successfully added your expenses to the category.")
    elif user_option == "3":
        view_per_category_expense()
    elif user_option == "4":
        view_total_spent()
    else:
        print("This is not a valid output, PLEASE try again.")





