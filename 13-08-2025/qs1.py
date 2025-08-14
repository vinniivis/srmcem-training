import random
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_number = self.generate_account_number()
        self.account_holder = account_holder
        self.balance = balance

    def generate_account_number(self):
        return "".join([str(random.randint(0, 9)) for _ in range(16)])

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds or invalid amount.")

    def display_balance(self):
        print(f"Account Balance: {self.balance}")

class SavingAccount(BankAccount):
    interest_rate = 4  

    def apply_interest(self):
        interest = (self.balance * self.interest_rate) / 100
        self.balance += interest
        print(f"Interest of {interest} applied. New balance: {self.balance}")



class CurrentAccount(BankAccount):
    overdraft_limit = 50000  

    def withdraw(self, amount):
        if amount > 0 and (self.balance - amount) >= -self.overdraft_limit:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Overdraft limit exceeded or invalid amount.")



if __name__ == "__main__":
    acc_type = input("Enter account type (saving/current): ").strip().lower()
    name = input("Enter account holder name: ")
    balance = float(input("Enter initial balance: "))

    if acc_type == "saving":
        account = SavingAccount(name, balance)
        print(f"Account Number: {account.account_number}")
        print(f"Interest Rate (Bank Fixed): {SavingAccount.interest_rate}%")

    elif acc_type == "current":
        account = CurrentAccount(name, balance)
        print(f"Account Number: {account.account_number}")
        print(f"Overdraft Limit (Bank Fixed): {CurrentAccount.overdraft_limit}")

    else:
        print("Invalid account type.")
        exit()

   
    while True:
        print("\nChoose operation:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Display Balance")
        if isinstance(account, SavingAccount):
            print("4. Apply Interest")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            amt = float(input("Enter amount to deposit: "))
            account.deposit(amt)

        elif choice == "2":
            amt = float(input("Enter amount to withdraw: "))
            account.withdraw(amt)

        elif choice == "3":
            account.display_balance()

        elif choice == "4" and isinstance(account, SavingAccount):
            account.apply_interest()

        elif choice == "5":
            print("Thank you for banking with us!")
            break
        else:
            print("Invalid choice.")


