// 1. Write a program of to swap the two values using template.

#include <iostream>
using namespace std;

template <typename T> T my_swap(T a, T b){

    a = a + b;
    b = a - b;
    a = a - b;
    cout << "\nAfter swapping: \n" << "A: " << a << "\t" << "B: " << b << endl; 
}

int main(){
    
    int n1, n2;

    cout << "Enter A: ";
    cin >> n1;

    cout << "Enter B: ";
    cin >> n2;

    cout << "\nBefore swapping: \n" << "A: " << n1 << "\t" << "B: " << n2 << endl; 

    my_swap<int>(n1, n2);

    return 0;
}
