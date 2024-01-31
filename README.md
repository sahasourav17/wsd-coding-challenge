# Coding Challenge - Wall Street Docs

## Problem Statement

Implement a simple banking application. A bank may have several types of accounts say current
account, saving account, salary account etc. An account may have fields like name, number, creation
date and balance etc. After starting the application, users will have 8 different choices as input from
1 to 8 through the console.
Based on the user input, the following operations will be performed

1. Create a new account
2. Display all accounts
3. Update an account
4. Delete an account
5. Deposit an amount into your account
6. Withdraw an amount from your account
7. Search for account
8. Exit

### Please consider the following constraints

Each account type may require a minimum balance to open the account.
Each account type may require to keep a minimum balance before withdrawing an amount.
No need to use any database.

### General Instructions

Programming language is optional but you may use a JAVA console application.

## Take a glimse of the solution:
```bash
╒══════════╤══════════════════════════════════════╕
│   Choice │ Function                             │
╞══════════╪══════════════════════════════════════╡
│        1 │ Create a new account                 │
├──────────┼──────────────────────────────────────┤
│        2 │ Display all accounts                 │
├──────────┼──────────────────────────────────────┤
│        3 │ Update an account                    │
├──────────┼──────────────────────────────────────┤
│        4 │ Delete an account                    │
├──────────┼──────────────────────────────────────┤
│        5 │ Deposit an amount into your account  │
├──────────┼──────────────────────────────────────┤
│        6 │ Withdraw an amount from your account │
├──────────┼──────────────────────────────────────┤
│        7 │ Search for account                   │
├──────────┼──────────────────────────────────────┤
│        8 │ Exit                                 │
╘══════════╧══════════════════════════════════════╛
Enter your choice (1-8): 1

Avaliable account types
╒════════════════╤════════════════════════╕
│ Account Type   │ Min Balance Required   │
╞════════════════╪════════════════════════╡
│ Savings        │ 1000.00 Tk.            │
├────────────────┼────────────────────────┤
│ Current        │ 500.00 Tk.             │
├────────────────┼────────────────────────┤
│ Salary         │ 0.00 Tk.               │
╘════════════════╧════════════════════════╛
Enter account type: Savings
Enter account holder's name: Sourav Saha
Enter account holder's address: Baridhara DOHS
Enter account number: 121212
Enter initial balance: 200


This account requires a minimum amount of 1000.0 Tk. 
Please increase the amount


╒══════════╤══════════════════════════════════════╕
│   Choice │ Function                             │
╞══════════╪══════════════════════════════════════╡
│        1 │ Create a new account                 │
├──────────┼──────────────────────────────────────┤
│        2 │ Display all accounts                 │
├──────────┼──────────────────────────────────────┤
│        3 │ Update an account                    │
├──────────┼──────────────────────────────────────┤
│        4 │ Delete an account                    │
├──────────┼──────────────────────────────────────┤
│        5 │ Deposit an amount into your account  │
├──────────┼──────────────────────────────────────┤
│        6 │ Withdraw an amount from your account │
├──────────┼──────────────────────────────────────┤
│        7 │ Search for account                   │
├──────────┼──────────────────────────────────────┤
│        8 │ Exit                                 │
╘══════════╧══════════════════════════════════════╛
Enter your choice (1-8): 1

Avaliable account types
╒════════════════╤════════════════════════╕
│ Account Type   │ Min Balance Required   │
╞════════════════╪════════════════════════╡
│ Savings        │ 1000.00 Tk.            │
├────────────────┼────────────────────────┤
│ Current        │ 500.00 Tk.             │
├────────────────┼────────────────────────┤
│ Salary         │ 0.00 Tk.               │
╘════════════════╧════════════════════════╛
Enter account type: Current
Enter account holder's name: Sourav Saha
Enter account holder's address: Baridhara
Enter account number: 121212
Enter initial balance: 600


Account created successfully!

```


## Setup Instructions

- Create a new python environment

  ```bash
  python3 -m venv env
  ```

- Activate the environment

  ```bash
  source env/bin/activate
  ```

- Install the dependencies
  ```bash
  pip install -r requirements.txt
  ```

## Run the Application
### Run Online: 
  https://replit.com/@sahasourav1170/wsd-coding-challenge-solution
### Run on Local Machine:
```bash
python3 solution.py
```
