#include <iostream>
using namespace std;

class Calculator {
    int a, b, c;
    bool useThreeNumbers;

public:
    Calculator() {
        int choice;
        cout << "Do you want to input numbers? (Enter 1 for Yes, 0 for No): ";
        cin >> choice;
        if (choice == 0) {
            exit(0);
        }

        cout << "Do you want to input 2 numbers or 3 numbers? (Enter 2 or 3): ";
        cin >> choice;

        if (choice == 3) {
            useThreeNumbers = true;
            cout << "Enter a: ";
            cin >> a;

            cout << "Enter b: ";
            cin >> b;

            cout << "Enter c: ";
            cin >> c;
        } else {
            useThreeNumbers = false;
            cout << "Enter a: ";
            cin >> a;

            cout << "Enter b: ";
            cin >> b;
        }
    }

    void printValues() {
        if (useThreeNumbers) {
            cout << "a = " << a << ", b = " << b << ", c = " << c << endl;
        } else {
            cout << "a = " << a << ", b = " << b << endl;
        }
    }

    int sum() {
        return useThreeNumbers ? a + b + c : a + b;
    }

    int subtract() {
        return useThreeNumbers ? a - b - c : a - b;
    }

    int multiply() {
        return useThreeNumbers ? a * b * c : a * b;
    }

    int divide() {
        if (b != 0 && (!useThreeNumbers || c != 0)) {
            return useThreeNumbers ? a / b / c : a / b;
        } else {
            cout << "Error: Division by zero is not allowed." << endl;
            return 0; // Return 0 or any error code as appropriate
        }
    }

    int modulo() {
        if (b != 0 && (!useThreeNumbers || c != 0)) {
            return useThreeNumbers ? a % b % c : a % b;
        } else {
            cout << "Error: Modulo by zero is not allowed." << endl;
            return 0; // Return 0 or any error code as appropriate
        }
    }
};

int main() {
    int choice;
    while (true) {
        Calculator calculator;

        while (true) {
            cout << endl
                 << "Enter 1 for Sum" << endl
                 << "Enter 2 for Subtraction" << endl
                 << "Enter 3 for Multiplication" << endl
                 << "Enter 4 for Division" << endl
                 << "Enter 5 for Modulo" << endl
                 << "Enter 0 to Exit" << endl
                 << endl;

            cout << "Enter your choice: ";
            cin >> choice;

            calculator.printValues();

            switch (choice) {
                case 1:
                    cout << "Sum is: " << calculator.sum() << endl;
                    break;

                case 2:
                    cout << "Subtraction is: " << calculator.subtract() << endl;
                    break;

                case 3:
                    cout << "Multiplication is: " << calculator.multiply() << endl;
                    break;

                case 4:
                    cout << "Division is: " << calculator.divide() << endl;
                    break;

                case 5:
                    cout << "Modulo is: " << calculator.modulo() << endl;
                    break;

                case 0:
                    cout << "Exited." << endl;
                    exit(0);
                    break;

                default:
                    cout << "Enter a valid choice." << endl;
                    break;
            }
        }
    }

    return 0;
}
