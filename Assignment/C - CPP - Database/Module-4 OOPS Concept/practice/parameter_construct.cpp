// parameterized constructer: in this we will pass parameter in constructor 
// if constructor is parametrized than object is also parametrized.

#include <iostream>
using namespace std;
class Add_func{
    int a, b;

    public: 
    Add_func(int n1, int n2){
        a = n1;
        b = n2;
    }

    void show(){
        cout << "Sum is: " << a+b << endl;
    }
};

int main(){

    Add_func af(10, 20);                // if constructor is parametrized than object is also parametrized.
    af.show();

    int a, b;
    cout << "enter a and b: ";
    cin >> a >> b;

    Add_func af1(a, b);
    af1.show();
    
    return 0;
}


