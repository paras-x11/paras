#include <iostream>
using namespace std;

class A{
    public:

    class B{
        public:

        class C{
            public:
            void show(){
                cout << "i m in class C. \n";
            }
        };

        void show(){
            cout << "i m in class B. \n";
        }
    };

    void show(){
        cout << "i m in class A. \n";
    }
};

int main(){
    A a;
    a.show();

    A::B obj;
    obj.show();

    A::B::C obj2;
    obj2.show();

    return 0;
}