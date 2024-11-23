// 1. Write a program to find the multiplication values and the cubic values using inline function 

#include <iostream>
using namespace std;

inline int multiply(int a, int b){
    return a*b;
}

inline void cube(int a, int b){
    cout << endl;
    cout << "Cube of " << a << " is: " << a*a*a << endl;
    cout << "Cube of " << b << " is: " << b*b*b << endl;
}

int main(){
    
    int a, b; 
    
    cout << "Enter a: ";
    cin >> a;

    cout << "Enter b: ";
    cin >> b;

    cout << endl;

    cout << a << " * " << b << " = " << multiply(a, b) << endl;

    cube (a, b);

    return 0;
}