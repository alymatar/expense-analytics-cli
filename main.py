from datetime import date
from pathlib import Path
import math
import csv
import os

# Clear the terminal screen based on the operating system
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def pause():
    input("\nPress Enter to return to the menu...")

# Check if the amount is positive and a valid finite number
def is_valid_amount(amount):
    return amount > 0 and math.isfinite(amount)


# Prompt user for a valid positive amount
def get_valid_amount():
    while True:
        amount = input("Enter expense amount: ")
        try:
            amount = float(amount)
            if is_valid_amount(amount):
                return amount
            else:
                print("Enter a valid number greater than zero")
        except ValueError:
            print("Enter number not symbols")

# Prompt user for required text input (must be non-empty)
def get_required_text(prompt):
    while True:
        text = input(prompt).strip()
        if text == "":
            print("This field is required. Please enter a value.")
        else:
            return text

def create_expense():
    
    amount = get_valid_amount()
    category = get_required_text("Enter expense category: ")
    description = get_required_text("Enter expense description: ")
    today = date.today().isoformat()
    expenses={
        "amount": amount,
        "category": category,
        "description": description,
        "date": today
    }
    return expenses


def calculate_total(expenses):
    # Start with a total of zero
    total = 0
    # Loop through each expense
    for expense in expenses:
        # Add each amount to the total
        total += expense["amount"]
    return total

# Calculate total spending grouped by category
def calculate_category_totals(expenses):
    total_by_category = {}
    for expense in expenses:
        category = expense["category"]
        if category not in total_by_category:
            total_by_category[category] = 0
        total_by_category[category] += expense["amount"]
    return total_by_category

# Filter expenses by category (case-insensitive match)
def filter_expenses_by_category(expenses, category):
    filtered_expenses = []
    for expense in expenses:
        if category.strip().lower() == expense["category"].strip().lower():
            filtered_expenses.append(expense)
    return filtered_expenses

def display_filtered_by_category(expenses):
    if not expenses:
        print("No expenses found for this category.")
        return
    print("========= EXPENSE REPORT BY CATEGORY ==========") 
    print("Category\tDescription\tAmount\tDate" )
    for expense in expenses:                   
        print(f"{expense['category']}\t \t{expense['description']}\t \t{expense['amount']:.2f}\t{expense['date']}")
    print("================================================")
    print(f"Category total: {calculate_total(expenses):.2f}")


# Create CSV file with headers if it doesn't exist or is empty
def create_csv_file(file_path="expenses.csv"):
    headers = ["Amount", "Category", "Description", "Date"]
    path = Path(file_path)

    if not path.exists() or path.stat().st_size == 0:
        with open(path, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()

def save_expenses(expenses, file_path="expenses.csv"):
    create_csv_file(file_path)
    HEADERS = ["Amount", "Category", "Description", "Date"]
    with open(file_path, "a", newline="", encoding="utf-8") as file:
        append = csv.DictWriter(file, fieldnames=HEADERS)
        for item in expenses:
            append.writerow({
                "Amount": item["amount"],
                "Category": item["category"],
                "Description": item["description"],
                "Date": item["date"]
            })

# Load expenses from CSV file into a list of dictionaries
def load_expenses(file_path="expenses.csv"):
    expenses = []
    if not Path(file_path).exists():
        return []
    else:
        with open(file_path, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                expenses.append({
                    "amount": float(row["Amount"]),
                    "category": row["Category"],
                    "description": row["Description"],
                    "date": row["Date"]
                })

    return expenses

# Display a summary report with total and category breakdowns
def display_report(expenses):
    print("========= EXPENSE REPORT ==========")
    total = calculate_total(expenses)
    print(f"Total expenses:  {total:.2f}")

    print("Spending by category:")
    category_totals = calculate_category_totals(expenses)
    for category in category_totals:
        print(f"{category}:  {category_totals[category]:.2f}" )
    print("===================================")


# Main application loop
def main():
    print("Welcome to the Expense Tracker!")
    expenses = load_expenses()
    new_expenses = []
    while True:
        clear_screen()
        print("1. Add an expense")
        print("2. View all expenses")
        print("3. View the spending report")
        print("4. Filter expenses by category")
        print("5. Exit")

        option = input("please select an option (1-5): ")
        clear_screen()
        if option == "1":      
            while True:
                try:
                    number_of_expenses = int(input("How many expenses would you like to add? "))
                    clear_screen()
                    if number_of_expenses > 0:
                        break
                    else: 
                        print("Add a number greater than zero")
                except ValueError:
                    print("Please enter a valid number")
                    
            for i in range(number_of_expenses):
                new_expenses.append(create_expense())        
            save_expenses(new_expenses)
            expenses.extend(new_expenses)
            new_expenses.clear()
            clear_screen()                  
            print(f"{number_of_expenses} expense(s) added and saved successfully.")
            pause()
            
        elif option == "2":
            if not expenses:
                print("No expenses found. Add an expense first.")
            else:
                for expense in expenses:
                    print(f"{expense['date']} - {expense['category']}: {expense['description']} - ${expense['amount']:.2f}")
            pause()
        elif option == "3":
            display_report(expenses) 
            pause()
        elif option == "4":
            category = input("Please enter the category: ")
            filtered_expenses = filter_expenses_by_category(expenses, category)
            display_filtered_by_category(filtered_expenses)
            pause()
        elif option == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option. Please select a valid option (1-5).")

if __name__ == "__main__":
    main()














