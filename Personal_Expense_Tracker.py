# %%
import csv

# %%
expenses = []

# %%
def add_expense():
    date = input("Enter the date: ")
    category = input("Enter the category: ")
    amount = input("Enter the amount: ")
    description = input("Enter the description: ")
    expenses.append({
        "date": date,
        "category": category,
        "amount": amount,
        "description": description
    })

    print("Expense added successfully")

# %%

def view_expense():
    for expense in expenses:

        print(f"Date: {expense['date']}")
        print(f"Category: {expense['category']}")
        print(f"Amount: {expense['amount']}")
        print(f"Description: {expense['description']}")

# %%

def set_budget():
    budget = float(input("Enter the budget: "))
    return budget

def track_budget(budget):
    total_expense = sum(expense['amount'] for expense in expenses )
    if total_expense > budget:
        print("You have exceeded your budget by " + str(total_expense - budget))
    else:
        print("You are within your budget by " + str(budget - total_expense))

# %%


def save_expenses():
    with open("expenses.csv", "w") as file:
        writer = csv.DictWriter(file, fieldnames=["date", "category", "amount", "description"])
        writer.writeheader()
        for expense in expenses:
            writer.writerow(expense)

def load_expenses():
    try : 
        with open("expenses.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                expenses.append(row)
    except FileNotFoundError:
        print("No expenses found")


# %%

def interactive_menu():
    load_expenses()
    budget = set_budget()

    while True:

        print("1. Add an expense")
        print("2. View expenses")
        print("3. Track budget")
        print("4. Save expenses")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expense()
        elif choice == "3":
            track_budget(budget)
        elif choice == "4":
            save_expenses()
            print("Exiting the program")
        elif choice == "5":
            break
        else:
            print("Invalid choice")


# %%
interactive_menu()


# %%
!jupyter nbconvert --to script notebook.ipynb



