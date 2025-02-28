class Customer:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. Balance: {self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        elif amount > 0:
            self.balance -= amount
            print(f"Withdrew {amount}. Balance: {self.balance}")
        else:
            print("Invalid withdrawal amount.")

    def show_account_info(self):
        print(f"Account Holder: {self.name}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance}")

class Bank:
    def __init__(self):
        self.customers = {}

    def create_account(self, name, account_number, balance=0):
        self.customers[account_number] = Customer(name, account_number, balance)
        print(f"Account created for {name}.")

    def get_customer(self, account_number):
        return self.customers.get(account_number)

    def deposit(self, account_number, amount):
        customer = self.get_customer(account_number)
        if customer:
            customer.deposit(amount)
        else:
            print("Account not found.")

    def withdraw(self, account_number, amount):
        customer = self.get_customer(account_number)
        if customer:
            customer.withdraw(amount)
        else:
            print("Account not found.")

    def show_account_info(self, account_number):
        customer = self.get_customer(account_number)
        if customer:
            customer.show_account_info()
        else:
            print("Account not found.")

# Main function to interact with the Bank
def main():
    bank = Bank()

    while True:
        print("\n1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Show Account Info")
        print("5. Exit")

        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter name: ")
            account_number = input("Enter account number: ")
            balance = float(input("Enter initial balance: "))
            bank.create_account(name, account_number, balance)
        
        elif choice == '2':
            account_number = input("Enter account number: ")
            amount = float(input("Enter deposit amount: "))
            bank.deposit(account_number, amount)
        
        elif choice == '3':
            account_number = input("Enter account number: ")
            amount = float(input("Enter withdrawal amount: "))
            bank.withdraw(account_number, amount)
        
        elif choice == '4':
            account_number = input("Enter account number: ")
            bank.show_account_info(account_number)
        
        elif choice == '5':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()