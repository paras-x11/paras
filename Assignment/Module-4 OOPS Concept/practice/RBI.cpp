// All the banks operating in India are controlled by RBI. RBI has set a well defined guideline 
// (e.g. minimum interest rate, minimum balance allowed, maximum withdrawal limit etc) which all banks must follow. 

// For example, suppose RBI has set minimum interest rate applicable to a saving bank account to be 4% annually; 
// however, banks are free to use 4% interest rate or to set any rates above it.

// Write a program to implement bank functionality in the above scenario.

// Note: Create few classes namely Customer, Account, RBI (Base Class) and few derived classes (SBI, ICICI, PNB etc). 
// Assume and implement required member variables and functions in each class.


#include <iostream>
using namespace std;

class Customer{
    public:
    string name;

    public:
    void input_customer(){
        cout << "Enter Name: ";
        getline(cin, name);
    } 

    void display_name(){
        cout << "\n\nName: " << name << endl;
    }
};

class Account{
    public:
    int acc_no;                                             //acc_type;

    public:
    void input_acc(){
        // cout << "Enter Account Type: ";                   //if entered current acc just display basic infos.
        // cin >> acc_type;

        cout << "Enter Account number: ";
        cin >> acc_no;
    }

    void display_acc(){
        cout << "Account number: " << acc_no << endl;
    }
};

class RBI{

    public:
    bool minimum_interest_rate(int int_r){

        if(int_r >= 4 && int_r <=100){
            return true;
        }
        else{
            return false;
        }
    }

    bool minimum_balance(int min_b){

        if(min_b >= 2000){
            return true;
        }
        else{
            return false;
        }
    }

    bool maximum_withdraw(int max_w){

        if(max_w >= 1 && max_w <=10000){
            return true;
        }
        else{
            return false;
        }
    }

};

class SBI : public Customer, public Account, public RBI{
    public:
    int interest_rate, min_balance, max_withdraw, final_balance=0, deposit, withdraw;

    public:

    void input_details(){
        display_name();
        display_acc();
    }

    // SBI admin:
    void set_interest_rate(){

        cout << "\nEnter SBI's Interest rate(in %): ";
        cin >> interest_rate;

        if(!minimum_interest_rate(interest_rate)){
            do{
                cout << "Minimum Interest Rate Is 4%." << endl;
                cout << "\nEnter SBI's Interest rate(in %): ";
                cin >> interest_rate;
            } while(!minimum_interest_rate(interest_rate));
        }
    }

    void set_minimum_balance(){

        cout << "\nEnter SBI's minimum balance amount: ";
        cin >> min_balance;

        if(!minimum_balance(min_balance)){
            do{
                cout << "\nMinimum Balance Amount Is 2000." << endl;
                cout << "\nEnter SBI's minimum balance amount: ";
                cin >> min_balance;
            } while(!minimum_balance(min_balance));
        }
    }

    void set_maximum_withdraw(){

        cout << "\nEnter SBI's maximum withdraw amount: ";
        cin >> max_withdraw;

        if(!minimum_balance(max_withdraw)){
            do{
                cout << "\nMinimum Balance Amount Is 10000." << endl;
                cout << "\nEnter SBI's maximum withdraw amount: ";
                cin >> max_withdraw;
            } while(!minimum_balance(max_withdraw));
        }
    }

    // SBI customer:
    void deposit_money(){
        cout << "Enter Amount for deposit: ";
        cin >> deposit;

        if(!minimum_balance(deposit)){
            do{
                cout << "\nMinimum Balance Amount Is 2000." << endl;
                cout << "\nEnter SBI's minimum balance amount: ";
                cin >> deposit;
            } while(!minimum_balance(deposit));
        }

        final_balance = final_balance + deposit;

        cout << "Now your final balance is: " << final_balance << endl;
    }

    void withdraw_money() {
        cout << "Enter Amount for withdraw: ";
        cin >> withdraw;

        if (withdraw > final_balance) {
            cout << "Insufficient balance." << endl;
            do{
                cout << "Enter Amount for withdraw: ";
                cin >> withdraw;
            } while(withdraw < final_balance);
        }
        if (withdraw < final_balance){
            do{
                cout << "Maximum Withdraw Amount is 10000." << endl;
                cout << "\nEnter Amount for withdraw: ";
                cin >> withdraw;
            } while(!maximum_withdraw(withdraw));

            final_balance = final_balance - withdraw;

            while (!minimum_balance(final_balance)) {
                cout << "Minimum Balance Amount after withdrawal is 2000." << endl;
                cout << "\nEnter Amount for withdraw: ";
                cin >> withdraw;
            }

            cout << "Now your final balance is: " << final_balance << endl;
        }
    }

}; 

// class ICICI : public Customer, public Account, public RBI{};

// class PNB : public Customer, public Account, public RBI{};

int main(){
    
    SBI customer;
    customer.input_details();
    customer.set_interest_rate();
    customer.set_minimum_balance();
    customer.set_maximum_withdraw();
    customer.deposit_money();
    customer.withdraw_money();
    
    return 0;
}




//    void set_minimum_balance(){

//         cout << "\nEnter SBI's minimum balance amount: ";
//         cin >> min_balance;

//         if(!minimum_balance(min_balance)){
//             do{
//                 cout << "Minimum Balance Amount Is 2000." << endl;
//                 cout << "\nEnter SBI's minimum balance amount: ";
//                 cin >> min_balance;
//             } while(!minimum_balance(min_balance));
//         }
//     }

//     void set_maximum_withdraw(){

//         cout << "\nEnter SBI's maximum withdraw amount: ";
//         cin >> max_withdraw;

//         if(!minimum_balance(max_withdraw)){
//             do{
//                 cout << "Minimum Balance Amount Is 10000." << endl;
//                 cout << "\nEnter SBI's maximum withdraw amount: ";
//                 cin >> max_withdraw;
//             } while(!minimum_balance(max_withdraw));
//         }
//     }
// Hint:

// Class Customer

// {

// //Personal Details

// // Few functions

// }

// Class Account

// {

// // Account Detail

// // Few functions

// }

// Class RBI

// {

// Customer c; //hasA relationship Account a; hip //hasA relations

// Public double GetInterestRate()

// { }

// Public double GetWithdrawalLimit

// () { }

// }

// Class SBI: public RBI

// {

// //Use RBI functionality or defin

// e own functionality.

// }

// Class ICICI: public RBI

// {

// //Use RBI functionality or defin

// e own functionality.

// }