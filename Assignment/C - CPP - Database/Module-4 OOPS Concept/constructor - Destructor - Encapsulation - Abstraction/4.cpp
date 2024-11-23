// 4. Write a C++ program to implement a class called Bank Account that has private member variables for account number and balance. 
// Include member functions to deposit and withdraw money from the account. 

#include <iostream>
using namespace std;

class bank{
    int ac_number, balance, d_amt, w_amt;

    public:
    void set_details(int n, int b){
        ac_number = n;
        balance = b;
    }

    void deposit(){
        cout << endl << "Enter amount to deposit: ";
        cin >> d_amt;

        balance = balance + d_amt;

        cout << endl << "-> Deposit successfull." << endl;
        cout << "-> Your current balance is: " << balance << endl;
    }

    void withdraw(){
        cout << endl << "Enter amount to withdraw: ";
        cin >> w_amt;

        if(w_amt < balance){
            balance = balance - w_amt;
            cout << endl << "-> Withdraw successfull. " << endl;
            cout << "-> Your current balance is: " << balance << endl;
        }
        else{
            cout << "-> Not enough balance. " << endl;
        }
    }
};

int main(){
    
    bank b1;

    int n, b, ch;

    cout << "Enter account number: ";
    cin >> n;

    cout << "Enter balance: ";
    cin >> b;

    b1.set_details(n, b);

    while(1){
    cout << endl << "Enter 1 for deposit. " << endl << "Enter 2 for withdraw. " << endl;
    cout << "Enter your choice: ";
    cin >> ch;

    switch (ch)
    {
    case 1: b1.deposit();
        break;

    case 2: b1.withdraw();
        break;

    case 0: cout << "-> Exited.";
            exit(0);
        break;
    
    default: cout << "-> Enter valid choice. " << endl;
        break;
    }
    }

    return 0;
}