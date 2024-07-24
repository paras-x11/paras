// 12. Write a program to swap the two numbers using friend function without using third variable 

#include <iostream>
using namespace std;

class number2;

class number1{
    int a;

    public:
    number1(){
        cout << "Enter A: ";
        cin >> a;
    }

    private:
    friend int swap(number1, number2);
};

class number2{
    int b;

    public:
    number2(){
        cout << "Enter B: ";
        cin >> b;
    }

    private:
    friend int swap(number1, number2);
};

int swap(number1 n1, number2 n2){


    cout << "\nBefore Swapping: \n";
    cout << "A: " << n1.a << "\t" << "B: " << n2.b << endl;

    n1.a = n1.a + n2.b;
    n2.b = n1.a - n2.b;
    n1.a = n1.a - n2.b;

    cout << "\nAfter Swapping: \n";
    cout << "A: " << n1.a << "\t" << "B: " << n2.b;
}

int main(){
    
    number1 num1;
    number2 num2;

    swap(num1, num2);

    return 0;
}