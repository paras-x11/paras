// 2. Define a class to represent a bank account. Include the following members: 
// 3. Data Member:  -Name of the depositor 
//                  -Account Number 
//                  -Type of Account 
//                  -Balance amount in the account 
 
// Member Function: -To assign values 
//                  -To deposited an amount 
//                  -To withdraw an amount after checking balance 
//                  -To display name and balance 

#include <iostream>
using namespace std;

class bank{
    public:
    string name, ac_type;
    int ac_no, balance, d_amt, w_amt;

    public:
    void get_data(){
        cout << "Enter Name of depositor: ";
        cin >> name;

        cout << "Enter Account Number: ";
        cin >> ac_no;

        cout << "Enter Type of Account: ";
        cin >> ac_type;

        cout << "Enter Balance: ";
        cin >> balance;
    }

    void deposit(){
        cout << "Enter amount to deposit: ";
        cin >> d_amt;

        balance = balance + d_amt;

        cout << endl;
        cout << "Depsit Successfull. " << endl;
        cout << "now your balance is: " << balance << endl;
    }

    void withdraw(){
        cout << "Enter amount to withdraw: ";
        cin >> w_amt;

        if(w_amt < balance){
            balance = balance - w_amt;

            cout << endl;
            cout << "Withdrawal Succesfull. "<< endl;
            cout << "now your balance is: " << balance << endl;
        }
        else{
            cout << endl;
            cout << "Your Balance is: " << balance << endl;
            cout << "\"Your balance is less than your withdrawal amount\"" << endl;
        }
    }

    void display(){
        cout << "Name: " << name << endl
             << "Account Number: " << ac_no << endl
             << "Type of Account: " << ac_type << endl
             << "Current Balance: " << balance << endl;
    }

};

int main(){

    int ch;
    bank b;
    b.get_data();

    while(1){
    cout << endl;
    cout << "Enter 1 for display information. " << endl 
         << "Enter 2 for deposit. " << endl
         << "Enter 3 for withdraw. " << endl
         << "Enter 0 for exit. " << endl;
    cout << endl;

    cout <<"Enter your choice: ";
    cin >> ch;

    switch (ch){
        case 1: b.display();
            break;

        case 2: b.deposit();
            break;
        
        case 3: b.withdraw();
            break;
        
        case 0: cout << "Exited.";
            exit (0); 
        
        default: cout << "Enter valid choice." << endl;
            break;
    }
    }

    return 0;
}


