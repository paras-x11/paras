// 1. WAP to create simple calculator using class.

#include <iostream>
using namespace std;

class calc{

    public:
    int a, b;
    
    int sum() {
        cout << "enter number 1: ";
        cin >> a;

        cout << "enter number 2: ";
        cin >> b;
        return a + b;
    }

    int subtraction() {
        cout << "enter number 1: ";
        cin >> a;

        cout << "enter number 2: ";
        cin >> b;
        return a - b;
    }

    int multiplication() {
        cout << "enter number 1: ";
        cin >> a;

        cout << "enter number 2: ";
        cin >> b;
        return a * b;
    }

    int division() {
        cout << "enter number 1: ";
        cin >> a;

        cout << "enter number 2: ";
        cin >> b;
        return a / b;
    }

    int modulo() {
        cout << "enter number 1: ";
        cin >> a;

        cout << "enter number 2: ";
        cin >> b;
        return a % b;
    }
};

int main(){

    int ch;
    calc c;

    while(1){
    cout << endl;
    cout << "1. Enter 1 for sum." << endl
         << "2. Enter 2 for substraction." << endl 
         << "3. Enter 3 for multiplication" << endl
         << "4. Enter 4 for division" << endl 
         << "5. Enter 5 for modulo" << endl
         << "0. Enter 0 for exit." << endl;

    cout << endl;
    cout << "Enter choice to perform: ";
    cin >> ch;
    
    switch (ch){

        case 1: cout << "-> Sum is: " << c.sum() << endl;
            break;

        case 2: cout << "-> Substraction is: " << c.subtraction() << endl;
            break;
    
        case 3: cout << "-> multiplication is: " << c.multiplication() << endl;
            break;
    
        case 4: cout << "-> dvision is: " << c.division() << endl;
            break;
    
        case 5: cout << "-> modulo is: " << c.modulo() << endl;
            break;

        case 0: cout << "-> Exited." << endl;
                exit (0);

        default: cout << "-> Enter valid choice. " << endl;
            break;
    
    }
    }
    return 0;
}
