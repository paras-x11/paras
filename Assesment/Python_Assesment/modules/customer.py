class Customer:
    def __init__(self, acc_no, banker):
        self.acc_no = acc_no
        self.b = banker 

    def withdraw(self, amount):
        if self.acc_no in self.b.customers:
            if amount < self.b.customers[self.acc_no]['balance'] and amount > 0:
                self.b.customers[self.acc_no]['balance'] -= amount
                print(f"Withdrew {amount}. New balance: {self.b.customers[self.acc_no]['balance']}")
                return True
            else:
                print("Insufficient funds.")
                return False
        else:
            print(f"\n-> Customer {self.acc_no} not found.")

    def deposit(self, amount):
        if amount > 0:
            if self.acc_no in self.b.customers:
                self.b.customers[self.acc_no]['balance'] += amount
                print(f"Deposited {amount}. New balance: {self.b.customers[self.acc_no]['balance']}")
                return True
            else:
                print(f"Customer {self.acc_no} not found.")
                return False
        else:
            print("\n-> Enter valid amount.")

    def view_balance(self):
        if self.acc_no in self.b.customers:
            print(f"Account balance for {self.acc_no}: {self.b.customers[self.acc_no]['balance']}")
        else:
            print(f"Customer {self.acc_no} not found.") 