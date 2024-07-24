// 13. Write a program to find the max number from given two numbers using friend function.

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
    friend int find_max(number1, number2);
};

class number2{
    int b;

    public:
    number2(){
        cout << "Enter B: ";
        cin >> b;
    }

    private:
    friend int find_max(number1, number2);
};

int find_max(number1 n1, number2 n2){

    if(n1.a > n2.b){
        cout << "\n-> A(" << n1.a << ") is greater than B(" << n2.b << ")";
    }
    else{
        cout << "\n-> B(" << n2.b << ") is greater than A(" << n1.a << ")";
    }   
}

int main(){
    
    number1 num1;
    number2 num2;

    find_max(num1, num2);

    return 0;
}