// constructor overloading: program having more than one constructor

// copy constructor: creates same copy of already existing constructor in the program.
// Syntax: class_name (const class_name &object_name)

#include <iostream>
using namespace std;
class values{
    public:
    int num1, num2;

    public:
    values(){
        cout << "enter num1 and num2: ";
        cin >> num1 >> num2;
    }

    values(int a, int b){
        num1 = a;
        num2 = b;
    }

    values(const values &obj){
        num1 = obj.num1;
        num2 = obj.num2;
    }

    void show(){
        cout << "num1 is: " << num1 << endl << "num2 is: " << num2 << endl;
    }
};
int main(){

    values v1;
    v1.show();

    values v2(10,20);
    v2.show();

    values v3 = v1;
    v3.show();

    

    return 0;
}