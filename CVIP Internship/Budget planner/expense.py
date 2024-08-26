import datetime
import csv

def get_user_input(prompt):
    while True:
        try:
            user_input = input(prompt)
            if not user_input:
                raise ValueError("Please enter a valid value.")
            return user_input
        except ValueError:
            print("Invalid input. Please try again.")

def get_date(prompt):
    while True:
        try:
            user_input = get_user_input(prompt)
            date_object = datetime.datetime.strptime(user_input, "%Y-%m-%d")
            return date_object.date()
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

def get_float(prompt):
    while True:
        try:
            user_input = get_user_input(prompt)
            float_value = float(user_input)
            return float_value
        except ValueError:
            print("Invalid float. Please enter a valid number.")

def add_transaction(filename):
    date = get_date("Enter the transaction date (YYYY-MM-DD): ")
    amount = get_float("Enter the transaction amount: ")
    category = get_user_input("Enter the transaction category: ")
    description = get_user_input("Enter the transaction description: ")

    with open(filename, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([date, amount, category, description])

    print("Transaction added successfully!")

def view_transactions(filename):
    try:
        with open(filename, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}")
    except FileNotFoundError:
        print("Budget file not found.")

def calculate_balance(filename):
    balance = 0.0
    try:
        with open(filename, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                balance += float(row[1])
            return balance
    except FileNotFoundError:
        print("Budget file not found.")
        return 0.0

def main():
    filename = "budget.csv"
    while True:
        print("\nBudget Planner")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Calculate Balance")
        print("4. Exit")
        choice = get_user_input("Enter your choice: ")

        if choice == '1':
            add_transaction(filename)
        elif choice == '2':
            view_transactions(filename)
        elif choice == '3':
            balance = calculate_balance(filename)
            print(f"Your current balance is: {balance}")
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()