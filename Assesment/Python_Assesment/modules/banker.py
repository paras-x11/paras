class Banker:
    def __init__(self): 
        self.customers = {}
 
    def add_customer(self, acc_no, details):

        if acc_no not in self.customers:
            self.customers[acc_no] = details
            print(f"\n-> Customer {acc_no} added successfully.")
            return True, f"Added customer {acc_no} with balance {self.customers[acc_no]['balance']}" 
        else:
            print(f"\n-> Customer {acc_no} already exists.")
            return False, f"-> Customer {acc_no} already exists."

    def search_customer(self, acc_no):
        if acc_no in self.customers:
            for keys in self.customers:
                if keys == acc_no:
                    print(f"\nAccount No: {acc_no}, Details: {self.customers[keys]}")
        else:
            print("\n-> No customers found.")

    def view_all_customers(self):
        if self.customers:
            print("\n\n-> All Customers:")
            for acc_no, details in self.customers.items():
                print(f"Account No: {acc_no}, Details: {details}")
        else:
            print("\n-> No customers found.")
    
    def total_amount_in_bank(self):
        total = 0 
        
        for vals in self.customers.values():
            total += vals['balance']
        print(f"\n-> Total amount in bank is: {total}")


