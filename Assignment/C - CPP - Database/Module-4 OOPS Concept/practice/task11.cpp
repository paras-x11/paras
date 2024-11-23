//wap to multiply 3 numbers using constructor.

#include <iostream>
using namespace std;

class multiply{

    public:
    multiply(int a, int b, int c){
        cout << "\nMultiplication of "<< a << ", " << b << " and " << c << " is: " << a*b*c;
    }
};

int main(){

    int a, b, c;

    cout << "Enter 3 numbers: ";
    cin >> a >> b >>c;

    multiply m(a, b, c);
    

    return 0;
}