from datetime import datetime

def add_expense(expenses, category, amount):
    expense = {
        "category": category,
        "amount": amount,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    expenses.append(expense)
    return expenses


def calculate_total(expenses):
    return sum(item["amount"] for item in expenses)

def calculate_average(expenses):
    if len(expenses) == 0:
        return 0
    return calculate_total(expenses) / len(expenses)

def calculate_gst(total, gst_rate=18):
    return total * gst_rate / 100

def final_amount(total, gst):
    return total + gst