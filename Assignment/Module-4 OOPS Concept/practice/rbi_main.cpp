#include <iostream>
using namespace std;

class Customer{
    public:
    string name;

    public:
    void input_name(){
        cout << "Enter Name: ";
        cin.ignore();
        getline(cin, name);
    } 

    void display_name(){
        cout << "\nName: " << name << endl;
    }
};

class Account{
    public:
    int acc_no;
    string acc_type;

    public:
    void input_acc(){
        // cout << "Enter Account Type: ";                   //if entered current acc just display basic infos.
        // cin.ignore();
        // getline(cin, acc_type);

        cout << "Enter Account number: ";
        cin >> acc_no;
    }

    void display_acc(){
        cout << "Account number: " << acc_no << endl;
    }
};

class RBI{

    public:

    void rbi_guidelines(){
        cout << "\n-> RBI guidelines: " << endl;
        cout << "Minimum interest rate is 4%, or banks are free to set any rates above it." << endl;
        cout << "Minimum balanace is 2000, or banks are free to set any limit above it." << endl;
        cout << "Maximum withdraw is 20000, or banks are free to set any limit below it." << endl;
    }

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

        if(max_w >= 0 && max_w <=20000){
            return true;
        }
        else{
            return false;
        }
    }

};

class Bank : public Customer, public Account, public RBI{
    public:
    int interest_rate, min_balance, max_withdraw, final_balance=0, deposit, withdraw;

    public:

    // admin:
    void set_interest_rate() {
        rbi_guidelines();
        cout << "\nEnter Interest rate (in %): ";
        cin >> interest_rate;

        while (!minimum_interest_rate(interest_rate)) {
            cout << "-> Minimum Interest Rate Is 4%." << endl;
            cout << "\nEnter Interest rate (in %): ";
            cin >> interest_rate;
        }

        cout << "-> Interest rate is: " << interest_rate << "%" << endl;
    }

    void set_minimum_balance() {
        cout << "\nEnter minimum balance amount: ";
        cin >> min_balance;

        while (!minimum_balance(min_balance)) {
            cout << "-> Minimum Balance Amount Is 2000." << endl;
            cout << "\nEnter minimum balance amount: ";
            cin >> min_balance;
        }

        cout << "-> Minimum balance limit is: " << min_balance << endl;
    }


    void set_maximum_withdraw() {
        cout << "\nEnter maximum withdraw limit: ";
        cin >> max_withdraw;

        while(!maximum_withdraw(max_withdraw)) {
            cout << "-> Maximum Withdraw limit Is 20000." << endl;
            cout << "\nEnter maximum withdraw limit: ";
            cin >> max_withdraw;
        }

        cout << "->Maximum withdraw limit is: " << max_withdraw << endl;
    }

    void input_details(){

        input_name();
        input_acc();

        cout << "\nEnter opening balance: ";
        cin >> final_balance;

        while (final_balance < min_balance){
            cout << "-> Minimum Balance Amount Is: " << min_balance << endl;
            cout << "\nEnter opening balane again: ";
            cin >> final_balance;
        } 

        cout << "-> Now your final balance is: " << final_balance << endl;
    }

    void deposit_money(){
        cout << "\nEnter Amount for deposit: ";
        cin >> deposit;

        final_balance = final_balance + deposit;

        cout << "-> Now your final balance is: " << final_balance << endl;
    }

    void withdraw_money() {

        cout << "\nEnter Amount for withdraw: ";
        cin >> withdraw;

        if(withdraw < 0){ cout << "-> Enter valid amount." << endl; return;}

        if (withdraw > final_balance) {
            cout << "-> Insufficient balance." << endl;
            cout << "-> Your Final Balance is: " << final_balance << endl;
            return;
        }

        if (withdraw > max_withdraw) {
            cout << "-> Maximum withdraw limit is: " << max_withdraw << endl;
            return;
        }

        while ( withdraw < max_withdraw && ((final_balance - withdraw) < min_balance) && withdraw > 0) {
            cout << "-> Your Final Balance is: " << final_balance << endl;
            cout << "-> You should keep minimum Balance " << min_balance << " after withdrawal." << endl;
            cout << "\nEnter Amount for withdraw: ";
            cin >> withdraw;
            if(withdraw < 0){cout << "-> Enter valid amount." << endl; return;}
        }

        final_balance = final_balance - withdraw;

        cout << "-> Now your final balance is: " << final_balance << endl;
    }
    
    void display_info(){
        cout << "\n-> Details of SBI bank account: " << endl;
        display_name();
        display_acc();
        cout << "Final Balance: " << final_balance << endl;
        cout << "you will get annual " << interest_rate << "%" << " interest on ur current balance: " << ((final_balance*interest_rate)/100 + final_balance) << endl;
    }
}; 

class SBI : public Bank {
    public:
    void sbi_details(){
        cout << "\n-> SBI's Term & Conditions: " << endl;
        cout << "SBI's annual Interest rate is: " << interest_rate << "%" << endl;
        cout << "SBI's minimum balance limit is: " << min_balance << endl;
        cout << "SBI's maximum withdraw limit is: " << max_withdraw << endl;
    }
};

class ICICI : public Bank {
public:
    void icici_details(){
        cout << "\n-> ICICI's Term & Conditions: " << endl;
        cout << "ICICI's annual Interest rate is: " << interest_rate << "%" << endl;
        cout << "ICICI's minimum balance limit is: " << min_balance << endl;
        cout << "ICICI's maximum withdraw limit is: " << max_withdraw << endl;
    }
};

class PNB : public Bank {
public:
    void pnb_details(){
        cout << "\n-> PNB's Term & Conditions: " << endl;
        cout << "PNB's annual Interest rate is: " << interest_rate << "%" << endl;
        cout << "PNB's minimum balance limit is: " << min_balance << endl;
        cout << "PNB's maximum withdraw limit is: " << max_withdraw << endl;
    }
};

int main() {
    int choice, ch;
    SBI s;
    ICICI i;
    PNB p;

    do {
        cout << "\nChoose Bank: \t 1 for SBI \t 2 for ICICI \t 3 for PNB \t 0 for exit." << endl;
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1:
                s.set_interest_rate();
                s.set_minimum_balance();
                s.set_maximum_withdraw();
                s.sbi_details();

                cout << "\n-> Create account in SBI: " << endl;  
                s.input_details();

                do {
                    cout << "\nEnter 1 to Deposit Money \t 2 to Withdraw Money \t 3 to Display Account Info \t 4 to SBI T&C \t 0 to Exit" << endl;
                    cout << "Enter your choice: ";
                    cin >> ch;

                    switch (ch) {
                        case 1:
                            s.deposit_money();
                            break;

                        case 2:
                            s.withdraw_money();
                            break;

                        case 3:
                            s.display_info();
                            break;

                        case 4:
                            s.sbi_details();
                            break;

                        case 0:
                            cout << "\n-> Exited." << endl;
                            break;

                        default:
                            cout << "\n-> Invalid choice. Please enter a valid choice." << endl;
                            break;
                    }
                } while (ch != 0);
                break;

            case 2:
                i.set_interest_rate();
                i.set_minimum_balance();
                i.set_maximum_withdraw();
                i.icici_details();

                cout << "\n-> Create account in ICICI: " << endl;  
                i.input_details();

                do {
                    cout << "\nEnter 1 to Deposit Money \t 2 to Withdraw Money \t 3 to Display Account Info \t 4 to ICICI T&C \t 0 to Exit" << endl;
                    cout << "Enter your choice: ";
                    cin >> ch;

                    switch (ch) {
                        case 1:
                            i.deposit_money();
                            break;

                        case 2:
                            i.withdraw_money();
                            break;

                        case 3:
                            i.display_info();
                            break;

                        case 4:
                            i.icici_details();
                            break;

                        case 0:
                            cout << "\n-> Exited." << endl;
                            break;

                        default:
                            cout << "\n-> Invalid choice. Please enter a valid choice." << endl;
                            break;
                    }
                } while (ch != 0);
                break;

            case 3:
                p.set_interest_rate();
                p.set_minimum_balance();
                p.set_maximum_withdraw();
                p.pnb_details();
                
                cout << "\n-> Create account in PNB: " << endl;  
                p.input_details();

                do {
                    cout << "\nEnter 1 to Deposit Money \t 2 to Withdraw Money \t 3 to Display Account Info \t 4 to PNB T&C \t 0 to Exit" << endl;
                    cout << "Enter your choice: ";
                    cin >> ch;

                    switch (ch) {
                        case 1:
                            p.deposit_money();
                            break;

                        case 2:
                            p.withdraw_money();
                            break;

                        case 3:
                            p.display_info();
                            break;

                        case 4:
                            p.pnb_details();
                            break;

                        case 0:
                            cout << "\n-> Exited." << endl;
                            break;

                        default:
                            cout << "\n-> Invalid choice. Please enter a valid choice." << endl;
                            break;
                    }
                } while (ch != 0);
                break;

            case 0:
                cout << "\n-> Exited." << endl;
                break;

            default:
                cout << "-> Enter valid choice." << endl;
                break;
        }
    } while (choice != 0);

    return 0;
}

