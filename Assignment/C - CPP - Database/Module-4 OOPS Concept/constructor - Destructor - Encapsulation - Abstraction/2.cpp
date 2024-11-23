// 2. Write a program of Addition, Subtraction, Division, Multiplication using constructor. 

#include <iostream>
using namespace std;

class calc{
    int a, b, c;

    public:
    calc(){

        cout << "\nenter a: ";
        cin >> a;

        cout << "enter b: ";
        cin >> b;
    }

    void printValues() {
        cout << "a = " << a << ", b = " << b << endl;
    }
    
    int sum(){
        return a+b;
    }

    int sub(){
        return a-b;
    }

    int multiplication(){
        return a*b;
    }

    int division(){
        return a/b;
    }

    int modulo(){
        return a%b;
    }   
};

int main(){
    int ch;

    calc c;

    while(1){
        cout <<endl
             << "enter 1 for sum." << endl 
             << "enter 2 for substraction." << endl
             << "enter 3 for multiplication" << endl 
             << "enter 4 for division." << endl 
             << "enter 5 for modulo." << endl
             << "enter 0 for exit." <<endl << endl;

        cout << "enter your choice: ";
        cin >> ch;

        c.printValues();

        switch (ch)
        {
        case 1: cout << "-> Sum is: " << c.sum() << endl;
            break;

        case 2: cout << "-> Substraction is: " << c.sub() << endl;
            break;
        
        case 3: cout << "-> Multiplication is: " << c.multiplication() << endl;
            break;
        
        case 4: cout << "-> Division is: " << c.division() << endl;
            break;
        
        case 5: cout << "-> Modulo is: " << c.modulo() << endl;
            break;

        case 0: cout << "-> Exited.";
                exit (0);
            break;
        
        default: cout << "Enter valid choice." << endl;
            break;
        }
        
    }

    return 0;
}