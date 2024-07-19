// Multiple inheritance has an ambiguity problem when we have same function name in both the parent and child class.

#include <iostream>
using namespace std;

class A{
    public:
    int show(){
        cout << "Class A" << endl;
    }
};

class B{
    public:
    int show(){
        cout << "Class B" << endl;
    }
};

class C : public A, public B{
    public:
    int show(){
        A::show();
        B::show();
        cout << "Class C" << endl;
    }
};

int main(){

    C c;
    c.show();

    cout << endl;
    C::A a;
    a.show();

    return 0;
}