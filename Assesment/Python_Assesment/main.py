from modules.banker import Banker
from modules.customer import Customer
from modules.file_handling import File_Handler 

terminal_width = 100
text = "WELCOME TO PYTHON BANK MANAGEMENT SYSTEM\n"
p = (terminal_width - len(text)) // 2

def display_banker_menu():
    print("\n-> Welcome To Banker's App\n")
    print(" " * p + "Banker Operation:\n")
    print(" " * p + "1. Add Customer")
    print(" " * p + "2. Search Customer")
    print(" " * p + "3. View All Customers")
    print(" " * p + "4. View Total Amount in Bank")
    print(" " * p + "5. Exit")

def banker_operation(b, f):
    try:
        while True:
            display_banker_menu()
            ch = input("Enter your choice: ")

            if ch == "1":
                try:
                    acc_no = int(input("\nEnter account number: "))
                    name = input("Enter customer name: ")
                    balance = float(input("Enter initial balance: "))
                    if balance < 1:
                        print("\n-> Enter valid balance amount.")
                        f.log_transaction(f"Attempt to add customer {acc_no} with balance {balance}")
                    else:
                        flag = b.add_customer(acc_no, {'name': name, 'balance': balance})
                        if flag[0]:
                            f.log_transaction(f"{flag[1]}")
                        else:
                            f.log_transaction(f"Attempt to add customer {acc_no} with balance {balance} but {flag[1]}")
                except Exception as e:
                    print("\n-> ", e)
                 
            elif ch == "2": 
                try:
                    acc_no = int(input("\nEnter account number to view: "))
                    b.search_customer(acc_no)
                except Exception as e:
                    print("\n-> ", e)
            
            elif ch == "3":
                b.view_all_customers()
            
            elif ch == "4":
                b.total_amount_in_bank()
            
            elif ch == "5":
                print("-> Exited From Banker App")
                break

            else:
                print("\n-> Invalid Choice.")
        
    except Exception as e:
        print(e, "\n-> Unexpected error has been occured.")

def display_customer_menu():
    print("\n-> Welcome To Customer's App\n")
    print(" " * p + "Customer Operation:\n")
    print(" " * p + "1. Withdraw Amount")
    print(" " * p + "2. Deposit Amount")
    print(" " * p + "3. View Balance")
    print(" " * p + "4. Log out")

def customer_operation(c, f):
    try:
        while True:
            display_customer_menu()
            ch = input("Enter your choice: ")

            if ch == "1":
                try:
                    amount = float(input("\nEnter amount to withdraw: "))
                    if amount < 1:
                        print("\n-> Enter valid amount.")
                        f.log_transaction(f"Customer {c.acc_no} attempted to withdrew {amount}")
                    else:
                        flag = c.withdraw(amount)
                        if flag:
                            f.log_transaction(f"Customer {c.acc_no} withdrew {amount}")
                        else:
                            f.log_transaction(f"Customer {c.acc_no} attempted to withdrew {amount}")
                except Exception as e:
                    print("\n-> ", e)
                                            
            elif ch == "2": 
                try:
                    amount = float(input("\nEnter amount to deposit: "))
                    flag = c.deposit(amount)
                    if flag:
                        f.log_transaction(f"Customer {c.acc_no} deposited {amount}")                        
                    else:
                        f.log_transaction(f"Customer {c.acc_no} attempted to deposit {amount}")
                except Exception as e:
                    print("\n-> ", e)
            
            elif ch == "3":
                try:
                    c.view_balance()
                except Exception as e:
                    print("\n-> ", e)
                
            elif ch == "4":
                print("-> Exited From Customer App")
                break

            else:
                print("\n-> Invalid Choice.")
                
    except Exception as e:
        print(e, "\n-> Unexpected error has been occured.")
    

if __name__ == "__main__":
    
    b = Banker()
    f = File_Handler()

    while True:
        print()
        print(" " * p + text)
        print(" " * p + "Choose your role:\n")
        print(" " * p + "1. Banker")
        print(" " * p + "2. Customer")
        print(" " * p + "3. View Transaction Log\n")
        print(" " * p + "4. Exit")
        ch = input("Enter your choice: ")

        if ch == "1":
            banker_operation(b, f)
            
        elif ch == "2":
            try:
                acc_no = int(input("\nEnter your account number: "))
                if acc_no in b.customers:
                    print(f"\n-> Logged in as Account no: {acc_no}, {b.customers[acc_no]}")
                    c = Customer(acc_no, b)
                    customer_operation(c, f)
                else:
                    print("\n-> Customer not found. Please ask the banker to add you.")
                    
            except Exception as e:
                print(e, "\n-> Unexpected error has been occured.")

        elif ch == "3":
            f.read_log()
        
        elif ch == "4":
            print("\n-> Exited.")
            break
        
        else:
            print("\n-> Invalid Choice.")