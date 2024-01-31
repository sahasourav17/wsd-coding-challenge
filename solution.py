import datetime
from tabulate import tabulate


class BankAccount:
    def __init__(self, acc_type, name, address, number, initial_balance=0.0):
        self.acc_type = acc_type
        self.name = name
        self.address = address
        self.number = number
        self.creation_date = datetime.datetime.now()
        self.balance = initial_balance

    def display_account_info(self):
        data = [
            ["Account Type", self.acc_type],
            ["Account Holder", self.name],
            ["Account Holder's Address", self.address],
            ["Account Number", self.number],
            ["Creation Date", self.creation_date.strftime("%Y-%m-%d %H:%M:%S")],
            ["Balance", f"{self.balance:.2f} Tk."],
        ]
        table = tabulate(data, headers=["Field", "Details"], tablefmt="fancy_grid")
        print(f"{table}\n")

    def can_withdraw(self, amount):
        MIN_BALANCES = {"Savings": 1000.0, "Current": 500.0, "Salary": 0.0}
        min_balance = MIN_BALANCES.get(self.acc_type, 0.0)
        return self.balance - amount >= min_balance


class SimpleBankingApplication:
    def __init__(self):
        self.accounts = []
        self.initialize_choices()

    MIN_BALANCES = {"Savings": 1000.0, "Current": 500.0, "Salary": 0.0}

    def initialize_choices(self):
        self.choices = {
            "1": self.create_account,
            "2": self.display_all_accounts,
            "3": self.update_account,
            "4": self.delete_account,
            "5": self.deposit_amount,
            "6": self.withdraw_amount,
            "7": self.search_account,
            "8": self.exit_application,
        }

    def create_account(self, acc_type, name, address, number, initial_balance):
        if initial_balance < self.MIN_BALANCES.get(acc_type):
            print(
                f"\n\nThis account requires a minimum amount of {self.MIN_BALANCES.get(acc_type)} Tk. \nPlease increase the amount\n\n"
            )
            return
        new_account = BankAccount(acc_type, name, address, number, initial_balance)
        self.accounts.append(new_account)
        print("\n\nAccount created successfully!\n\n")

    def display_all_accounts(self):
        if not self.accounts:
            print("\n\nNo accounts found.\n\n")
        else:
            print(f"\n=================== Accounts ===================\n")
            for account in self.accounts:
                account.display_account_info()

    def update_account(self, account_number, new_name, new_address):
        for account in self.accounts:
            if account.number == account_number:
                account.name = new_name
                account.address = new_address
                print("\n\nAccount info updated successfully!\n\n")
                return
        print("\n\nAccount not found.\n\n")

    def delete_account(self, account_number):
        for account in self.accounts:
            if account.number == account_number:
                self.accounts.remove(account)
                print("\n\nAccount deleted successfully!\n\n")
                return
        print("\n\nAccount not found.\n\n")

    def deposit_amount(self, account_number, amount):
        for account in self.accounts:
            if account.number == account_number:
                account.balance += amount
                account.display_account_info()
                return
        print("\n\nAccount not found.\n\n")

    def withdraw_amount(self, account_number, amount):
        for account in self.accounts:
            if account.number == account_number:
                if account.can_withdraw(amount):
                    account.balance -= amount
                    print(
                        f"\n\nSuccessfully {amount} Tk. withdrawn from your account. \nNew balance: {account.balance}\n\n"
                    )
                else:
                    print(
                        "\n\nNot enough money to maintain minimum balance after withdrawal.\n\n"
                    )
                return
        print("\n\nAccount not found.\n\n")

    def search_account(self, account_number):
        for account in self.accounts:
            if account.number == account_number:
                print(f"\n================ Account Info ================\n")
                account.display_account_info()
                return
        print("\n\nAccount not found.\n\n")

    def exit_application(self):
        print("\n\nExiting the application.\n\n")
        exit()

    def run_application(self):
        while True:
            try:
                options = [
                    ["1", "Create a new account"],
                    ["2", "Display all accounts"],
                    ["3", "Update an account"],
                    ["4", "Delete an account"],
                    ["5", "Deposit an amount into your account"],
                    ["6", "Withdraw an amount from your account"],
                    ["7", "Search for account"],
                    ["8", "Exit"],
                ]

                print(
                    tabulate(
                        options,
                        headers=["Choice", "Function"],
                        tablefmt="fancy_grid",
                    )
                )
                choice = input("Enter your choice (1-8): ")

                chosen_function = self.choices.get(choice)
                if chosen_function:
                    if choice == "1":
                        print("\nAvaliable account types")
                        account_options = [
                            [acc_type, f"{balance:.2f} Tk."]
                            for acc_type, balance in self.MIN_BALANCES.items()
                        ]
                        print(
                            tabulate(
                                account_options,
                                headers=["Account Type", "Min Balance Required"],
                                tablefmt="fancy_grid",
                            )
                        )

                        acc_type = input("Enter account type: ")
                        if acc_type.capitalize() not in self.MIN_BALANCES:
                            print(
                                "\nInvalid account type. Please select correct account type \n"
                            )
                            return
                        name = input("Enter account holder's name: ")
                        address = input("Enter account holder's address: ")
                        number = input("Enter account number: ")
                        initial_balance = float(input("Enter initial balance: "))
                        chosen_function(
                            acc_type, name, address, number, initial_balance
                        )

                    elif choice == "3":
                        account_number = input("Enter account number to update: ")
                        new_address = input("Enter account holder's address: ")
                        new_name = input("Enter account holder's name: ")
                        chosen_function(account_number, new_name, new_address)

                    elif choice == "4":
                        account_number = input("Enter account number to delete: ")
                        chosen_function(account_number)

                    elif choice == "5" or choice == "6":
                        account_number = input("Enter account number: ")
                        amount = float(input("Enter amount: "))
                        chosen_function(account_number, amount)

                    elif choice == "7":
                        account_number = input("Enter account number to search: ")
                        chosen_function(account_number)

                    else:
                        chosen_function()
                else:
                    print("Invalid choice. Please enter a number between 1 and 8.")
            except KeyboardInterrupt:
                print("\nKeyboardInterrupt. Exiting the application.")
                break


if __name__ == "__main__":
    bank_app = SimpleBankingApplication()
    bank_app.run_application()
