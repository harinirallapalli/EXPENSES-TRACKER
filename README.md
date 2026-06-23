# 💰 Expense Tracker System

## 📌 Project Overview

Expense Tracker is a Python-based console application that helps users manage their daily expenses efficiently. The application allows users to add expenses, view saved records, generate financial reports, and store data permanently using a JSON file.

---

## 🚀 Features

* Add New Expenses
* View Expense Records
* Store Data in JSON File
* Generate Expense Reports
* Calculate Total Expenses
* Calculate Average Expenses
* GST Calculation (18%)
* Final Amount Calculation
* Professional Terminal Interface

---

## 📂 Project Structure

```text
expense_tracker/
│
├── main.py
├── expense_manager.py
├── storage.py
├── ui.py
├── data.json
└── README.md
```

---

## 🛠 Technologies Used

* Python 3
* JSON
* File Handling
* Functions
* Lists & Dictionaries
* Exception Handling
* Modular Programming

---

## ⚙️ Modules Description

### main.py

Controls program flow and menu operations.

### expense_manager.py

Contains expense calculations:

* Add Expense
* Calculate Total
* Calculate Average
* Calculate GST
* Calculate Final Amount

### storage.py

Handles:

* Load Expenses
* Save Expenses

### ui.py

Displays:

* Menu
* Expense List
* Formatted Currency Output

### data.json

Stores expense records permanently.

---

## ▶️ How to Run

### Step 1: Open Terminal

```bash
cd expense_tracker
```

### Step 2: Run the Program

```bash
python main.py
```

---

## 💻 Menu

```text
====================================================
                 Expense Tracker
====================================================

1. Add Expense
2. View Expenses
3. Generate Report
4. Exit

====================================================
```

---

## 📊 Sample Output

### Add Expense

```text
Enter Choice: 1

Category: Food
Amount: 500

Expense Added Successfully
```

### View Expenses

```text
====================================================
EXPENSE LIST
----------------------------------------------------
#     Category             Amount          Date
----------------------------------------------------
1     Food                 ₹500.00         2026-06-23 23:54:30
====================================================
```

### Generate Report

```text
========== EXPENSE REPORT ==========

Total Transactions : 4
Total Amount       : ₹35,530.00
Average Expense    : ₹8,882.50
GST (18%)          : ₹6,395.40
Final Amount       : ₹41,925.40
```

---

## 📚 Concepts Covered

* Python Functions
* Modular Programming
* JSON Data Storage
* File Handling
* Exception Handling
* Expense Management
* GST Calculation
* Report Generation
* Financial Data Analysis

---

## 🎯 Learning Outcomes

After completing this project, students will learn:

* How to build a console-based application
* How to store and retrieve data using JSON
* How to organize projects using modules
* How to perform financial calculations
* How to generate reports from stored data

---

👩‍💻 Developed By

Harini Rallapalli
B.Tech Student/ python developer
St. Mary's Engineering College
Batch 2026
