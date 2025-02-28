class BankAccount:
    def __init__(self, num, bal):
        self.num = num
        self.bal = bal
    
    def dep(self, amt):
        self.bal += amt
    
    def wth(self, amt):
        if amt <= self.bal:
            self.bal -= amt
    
    def show(self):
        print(f"Account Number: {self.num}, Balance: {self.bal}")

num = input("Enter account number: ")
bal = float(input("Enter initial balance: "))

ba = BankAccount(num, bal)

while True:
    print("\nMenu:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Show Balance")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == "1":
        deposit_amt = float(input("Enter deposit amount: "))
        ba.dep(deposit_amt)
        print(f"Deposited {deposit_amt}. New Balance: {ba.bal}")
    
    elif choice == "2":
        withdraw_amt = float(input("Enter withdrawal amount: "))
        ba.wth(withdraw_amt)
        print(f"Withdrew {withdraw_amt}. New Balance: {ba.bal}")
    
    elif choice == "3":
        ba.show()
    
    elif choice == "4":
        print("Exiting the program.")
        break
    
    else:
        print("Invalid choice. Please try again.")