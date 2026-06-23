from storage import load_expenses, save_expenses
from expense_manager import (
    add_expense,
    calculate_total,
    calculate_average,   # FIX: was missing import
    calculate_gst,       # FIX: was missing import
    final_amount         # FIX: was missing import
)
from ui import show_menu, display_expenses

expenses = load_expenses()

while True:

    show_menu()

    choice = input("Enter Choice: ")

    if choice == "1":

        category = input("Category: ")

        try:
            amount = float(input("Amount: "))

            expenses = add_expense(
                expenses,
                category,
                amount
            )

            save_expenses(expenses)

            print("Expense Added Successfully")

        except ValueError:
            print("Invalid Amount")

    elif choice == "2":

        if expenses:
            display_expenses(expenses)
        else:
            print("No Expenses Found")

    elif choice == "3":

        if not expenses:
            print("No Expenses Found")
        else:
            total = calculate_total(expenses)
            average = calculate_average(expenses)
            gst = calculate_gst(total)
            final_total = final_amount(total, gst)

            print("\n========== EXPENSE REPORT ==========")
            print(f"Total Transactions : {len(expenses)}")
            print(f"Total Amount       : ₹{total:.2f}")
            print(f"Average Expense    : ₹{average:.2f}")
            print(f"GST (18%)          : ₹{gst:.2f}")
            print(f"Final Amount       : ₹{final_total:.2f}")

    elif choice == "4":

        print("Thank You For Using Expense Tracker")
        break

    else:
        print("Invalid Choice")