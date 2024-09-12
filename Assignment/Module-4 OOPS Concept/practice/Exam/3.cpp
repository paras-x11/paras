// 3. wap to swap 2 num using friend func.

#include <iostream>
using namespace std;

class num2;

class num1{
    int a=10;

    public:
    num1(int n1){
        a = n1;
    }

    friend int swapNumbers(num1, num2);
};

class num2{
    int b=20;

    public:
    num2(int n2){
        b = n2;
    }

    friend int swapNumbers(num1, num2);
};

int swapNumbers(num1 n1, num2 n2){
    
    int temp;

    cout << "\nBefore Swapping Value:\n A = " << n1.a << " \t B = " << n2.b;

    temp = n1.a;
    n1.a = n2.b;
    n2.b = temp;

    cout << "\n\nAfter Swapping Value:\n A = " << n1.a << " \t B = " << n2.b;
    
}

int main(){
    int a, b;

    cout << "Enter A: ";
    cin >> a; 

    cout << "Enter B: ";
    cin >> b; 

    num1 n1(a);

    num2 n2(b);

    swapNumbers(n1, n2);

    return 0;
}