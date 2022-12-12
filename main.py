class BankAccount(object):
    defaultAccNumber = 1

    def __init__(self, name, balance = 0):
        self.name = name
        self.balance = balance
        self.defaultAccNumber = BankAccount.defaultAccNumber
        BankAccount.defaultAccNumber = BankAccount.defaultAccNumber + 1

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient Funds!!")
        else:
            self.balance -= amount

    def get_balance(self):
        return self.balance

if __name__ == '__main__':
    print("""
        Menu:
        1. Deposit.
        2. Withdraw.
        3. Get Balance.
    """)
    menu_selection = int(input())
    myObj = BankAccount('Ben', 1000)
    myObj1 = BankAccount('Jake', 2000)
    myObj2 = BankAccount('Tyler', 3000)
    myObj3 = BankAccount('Jimmy', 4000)
    myObj4 = BankAccount('Sam', 5000)

    if menu_selection == 1:
        print("Enter the amount to be deposited.")

    elif menu_selection == 2:
        print("Enter money to be withdrawn.")

    elif menu_selection == 3:
        print(f"The available balance : Rs.{}")

    else:
        print("Please enter a valid input from menu!!")
