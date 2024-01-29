import datetime


class BankAccount:
    def __init__(self, acc_type, name, address, number, initial_balance=0.0):
        self.acc_type = acc_type
        self.name = name
        self.address = address
        self.number = number
        self.creation_date = datetime.datetime.now()
        self.balance = initial_balance

    def display_account_info(self):
        print(f"Account Type: {self.acc_type}")
        print(f"Account Holder: {self.name}")
        print(f"Account Number: {self.number}")
        print(f"Account Holder's Address: {self.address}")
        print(f"Creation Date: {self.creation_date}")
        print(f"Balance: {self.balance}")
        print()


class SimpleBankingApplication:
    def __init__(self):
        self.accounts = []
        self.initialize_choices()

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
        new_account = BankAccount(acc_type, name, address, number, initial_balance)
        self.accounts.append(new_account)
        print("Account created successfully!")

    def display_all_accounts(self):
        if not self.accounts:
            print("No accounts found.")
        else:
            for account in self.accounts:
                account.display_account_info()

    def update_account(self, account_number, new_name, new_address):
        for account in self.accounts:
            if account.number == account_number:
                account.name = new_name
                account.address = new_address
                print("Account info updated successfully!")
                return
        print("Account not found.")

    def delete_account(self, account_number):
        pass

    def deposit_amount(self, account_number, amount):
        pass

    def withdraw_amount(self, account_number, amount):
        pass

    def search_account(self, account_number):
        pass

    def exit_application(self):
        print("Exiting the application.")
        exit()

    def run_application(self):
        while True:
            print("1. Create a new account")
            print("2. Display all accounts")
            print("3. Update an account")
            print("4. Delete an account")
            print("5. Deposit an amount into your account")
            print("6. Withdraw an amount from your account")
            print("7. Search for account")
            print("8. Exit")

            try:
                choice = input("Enter your choice (1-8): ")

                chosen_function = self.choices.get(choice)
                if chosen_function:
                    if choice == "1":
                        acc_type = input("Enter account type: ")
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
