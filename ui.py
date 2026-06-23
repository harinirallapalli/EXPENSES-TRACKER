CURRENCY = "₹"
SEPARATOR = "─" * 52
DOUBLE_SEP = "═" * 52


def fmt_currency(amount):
    return f"{CURRENCY}{amount:,.2f}"


def show_menu():
    print("\n" + DOUBLE_SEP)
    print("  Expense Tracker ")
    print(DOUBLE_SEP)
    print(" 1. Add Expense")
    print(" 2. View Expenses")
    print(" 3. Generate Report")
    print(" 4. Exit")
    print(DOUBLE_SEP)


def display_expenses(expenses):
    print("\n" + DOUBLE_SEP)
    print(" EXPENSE LIST")
    print(SEPARATOR)
    print(f"{'#':<5} {'Category':<20} {'Amount':<15} {'Date'}")
    print(SEPARATOR)

    for i, exp in enumerate(expenses, 1):
        print(
            f"{i:<5} "
            f"{exp['category']:<20} "
            f"{fmt_currency(exp['amount']):<15} "
            f"{exp['date']}"
        )

    print(DOUBLE_SEP)