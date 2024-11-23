// 8. Write a program to Mathematic operation like Addition, Subtraction, Multiplication, Division Of two number using different parameters 
// and Function Overloading.

#include <iostream>
using namespace std;

class calculator{

    public:
    int add(int a, int b){

        return a + b; 
    }

    int add(int a, int b, int c){
        return a + b + c;
    }

    double add(double a1, double b1){
        return a1 + b1;
    }

    double add(double a1, double b1, double c1){
        return a1 + b1 + c1;
    }


    int substraction(int a, int b){
        return a - b;
    }

    double substration(double a1, double b1){
        return a1 - b1;
    }


    int multiply(int a, int b){
        return a * b;
    }

    int multiply(int a, int b, int c){
        return a * b * c;
    }

    double multiply(double a1, double b1){
        return a1 * b1;
    }

    double multiply(double a1, double b1, double c1){
        return a1 * b1 * c1;
    }


    int division(int a, int b){
        return a / b;
    }

    double division(double a1, double b1){
        return a1 / b1;
    }    
};

int main(){
    
    calculator calc;

    int a, b, c, ch, inner_ch;
    double a1, b1, c1;

    while(1){
    cout << "\n-> Enter: 1 for addition \t 2 for substraction \t 3 for multiply \t 4 for division \t 0 to exit. " << endl;
    cout << "\nEnter your choice: ";
    cin >> ch;

    switch (ch){
        
    case 1: 
        do{
        cout << "\n-> Enter: " << endl
             << "   1 for 2 int value addition \t 2 for 2 double value addition" << endl
             << "   3 for 3 int value addition \t 4 for 3 double value addition \t 0 to go back." << endl;
        cout << "\nEnter your choice: ";
        cin >> inner_ch;

        switch (inner_ch){

        case 1: cout << "\nEnter a: ";
                cin >> a;

                cout << "Enter b: ";
                cin >> b;

                cout << endl << a << " + " << b << " = " << calc.add(a, b) << endl; 
            break;

        case 2: cout << "\nEnter a: ";
                cin >> a1;

                cout << "Enter b: ";
                cin >> b1;

                cout << endl << a1 << " + " << b1 << " = " << calc.add(a1, b1) << endl; 
            break;

        case 3: cout << "\nEnter a: ";
                cin >> a;

                cout << "Enter b: ";
                cin >> b;

                cout << "Enter c: ";
                cin >> c;

                cout << endl << a << " + " << b << " + " << c << " = " << calc.add(a, b, c) << endl; 
            break;

        case 4: cout << "\nEnter a: ";
                cin >> a1;

                cout << "Enter b: ";
                cin >> b1;

                cout << "Enter c: ";
                cin >> c1;

                cout << endl << a1 << " + " << b1 << " + " << c1 << " = " << calc.add(a1, b1, c1) << endl; 
            break;

        case 0: 
            break;
        
        default: cout << "-> Invalid choice. \n";
            break;
        }
        }while(inner_ch != 0);
    break;

    case 2: 
        do{
        cout << "\n-> Enter: 1 for 2 int value substraction \t 2 for 2 double value substraction \t 0 to go back." << endl;
        cout << "\nEnter your choice: ";
        cin >> inner_ch;

        switch (inner_ch){

        case 1: cout << "\nEnter a: ";
                cin >> a;

                cout << "Enter b: ";
                cin >> b;

                cout << endl << a << " - " << b << " = " << calc.substraction(a, b) << endl; 
            break;

        case 2: cout << "\nEnter a: ";
                cin >> a1;

                cout << "Enter b: ";
                cin >> b1;

                cout << endl << a1 << " - " << b1 << " = " << calc.substration(a1, b1) << endl; 
            break;

        case 0: 
            break;
        
        default: cout << "-> Invalid choice. \n"<< endl;
            break;
        }
        }while( inner_ch != 0);
    break;

    case 3: 
        do{
        cout << "\n-> Enter: " << endl
             << "   1 for 2 int value multiplication \t 2 for 2 double value multiplication" << endl
             << "   3 for 3 int value multiplication \t 4 for 3 double value multiplication \t 0 to go back." << endl;
        cout << "\nEnter your choice: ";
        cin >> inner_ch;

        switch (inner_ch){

        case 1: cout << "\nEnter a: ";
                cin >> a;

                cout << "Enter b: ";
                cin >> b;

                cout << endl << a << " * " << b << " = " << calc.multiply(a, b) << endl; 
            break;

        case 2: cout << "\nEnter a: ";
                cin >> a1;

                cout << "Enter b: ";
                cin >> b1;

                cout << endl << a1 << " * " << b1 << " = " << calc.multiply(a1, b1) << endl; 
            break;

        case 3: cout << "\nEnter a: ";
                cin >> a;

                cout << "Enter b: ";
                cin >> b;

                cout << "Enter c: ";
                cin >> c;

                cout << endl << a << " * " << b << " * " << c << " = " << calc.multiply(a, b, c) << endl; 
            break;

        case 4: cout << "\nEnter a: ";
                cin >> a1;

                cout << "Enter b: ";
                cin >> b1;

                cout << "Enter c: ";
                cin >> c1;

                cout << endl << a1 << " * " << b1 << " * " << c1 << " = " << calc.multiply(a1, b1, c1) << endl; 
            break;

        case 0: 
            break;
        
        default: cout << "-> Invalid choice. \n";
            break;
        }
        }while( inner_ch != 0);
    break;

    case 4: 
        do{
        cout << "\n-> Enter: 1 for 2 int value division \t 2 for 2 double value division \t 0 to go back" << endl;
        cout << "\nEnter your choice: ";
        cin >> inner_ch;

        switch (inner_ch){

        case 1: cout << "\nEnter a: ";
                cin >> a;

                cout << "Enter b: ";
                cin >> b;

                cout << endl << a << " / " << b << " = " << calc.division(a, b) << endl; 
            break;

        case 2: cout << "\nEnter a: ";
                cin >> a1;

                cout << "Enter b: ";
                cin >> b1;

                cout << endl << a1 << " / " << b1 << " = " << calc.division(a1, b1) << endl; 
            break;

        case 0: 
            break;
        
        default: cout << "-> Invalid choice. \n"<< endl;
            break;
        }
        }while( inner_ch != 0);
    break;
    
    case 0: 
        cout << "\n-> Exited. \n" << endl;
        exit(0);
    break;
    
    default: 
        cout << "\n-> Invalid Choice. \n" << endl;
    break;
    }
    }

    return 0;
}