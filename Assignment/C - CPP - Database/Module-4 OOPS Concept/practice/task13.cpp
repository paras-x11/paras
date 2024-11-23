//Wap to print fibonacci series using parameterized constructor.

#include <iostream>
using namespace std;

class fibonacci{

    int a=0, b=1, c;

    public:
    fibonacci(int n){

        cout << a << ", " << b << ", ";

        while(n>0){

            c = a + b;
            a = b;
            b = c;

            cout << c << ", ";
            n--;            
        }        
    }
};

int main(){

    int n;

    cout << "Enter number: ";
    cin >> n;

    fibonacci f(n);

    return 0;
}