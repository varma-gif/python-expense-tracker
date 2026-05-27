expenses = []


# Add Expense
def add_expense():
    amount = input("Enter amount: ")
    category = input("Enter category: ")

    expenses.append([amount, category])

    print("Expense Added")


# View Expenses
def view_expense():
    print("\nExpenses List")

    for i in range(len(expenses)):
        print(i, expenses[i])


# Update Expense
def update_expense():
    index = int(input("Enter index number: "))

    amount = input("Enter new amount: ")
    category = input("Enter new category: ")

    expenses[index] = [amount, category]

    print("Expense Updated")


# Delete Expense
def delete_expense():
    index = int(input("Enter index number: "))

    expenses.pop(index)

    print("Expense Deleted")


# Main Program
while True:

    print("\n1.Add")
    print("2.View")
    print("3.Update")
    print("4.Delete")
    print("5.Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expense()

    elif choice == "3":
        update_expense()

    elif choice == "4":
        delete_expense()

    elif choice == "5":
        print("Program Ended")
        break

    else:
        print("Invalid Choice")