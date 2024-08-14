import datetime

class Expense:
    def __init__(self, description, amount, payer, split_type, participants):
        self.description = description
        self.amount = amount
        self.payer = payer
        self.split_type = split_type  # 'equal', 'custom', 'percentage'
        self.participants = participants

class Group:
    def __init__(self, name):
        self.name = name
        self.members = []
        self.expenses = []

    def add_member(self, member):
        self.members.append(member)

    def add_expense(self, expense):
        self.expenses.append(expense)

    def calculate_balances(self):
        balances = {member: 0 for member in self.members}
        for expense in self.expenses:
            for participant in expense.participants:
                if expense.split_type == 'equal':
                    amount_owed = expense.amount / len(expense.participants)
                elif expense.split_type == 'custom':
                    amount_owed = expense.participants[participant]
                elif expense.split_type == 'percentage':
                    amount_owed = expense.amount * expense.participants[participant] / 100
                balances[participant] += amount_owed if participant != expense.payer else -expense.amount
        return balances

def main():
    group_name = input("Enter group name: ")
    group = Group(group_name)

    while True:
        print("\nOptions:")
        print("1. Add member")
        print("2. Add expense")
        print("3. Calculate balances")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            member_name = input("Enter member name: ")
            group.add_member(member_name)
        elif choice == "2":
            description = input("Enter expense description: ")
            amount = float(input("Enter expense amount: "))
            payer = input("Enter payer: ")
            split_type = input("Enter split type (equal, custom, percentage): ")
            if split_type == 'custom':
                participants = {}
                for member in group.members:
                    amount = float(input(f"Enter amount for {member}: "))
                    participants[member] = amount
            elif split_type == 'percentage':
                participants = {}
                for member in group.members:
                    percentage = float(input(f"Enter percentage for {member}: "))
                    participants[member] = percentage
            else:
                participants = group.members
            expense = Expense(description, amount, payer, split_type, participants)
            group.add_expense(expense)
        elif choice == "3":
            balances = group.calculate_balances()
            for member, balance in balances.items():
                print(f"{member} owes: {balance:.2f}")
        elif choice == "4":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
