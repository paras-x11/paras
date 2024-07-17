// 2. Write a C++ Program to find Area of Rectangle using inheritance.

#include <iostream>
using namespace std;

class Reactangle{
    protected:
    int l, w;

    protected:
    void input(){
        cout << "Enter length: ";
        cin >> l;

        cout << "Enter width: ";
        cin >> w;

    }

};

class Area : protected Reactangle{

    int a;

    public:
    void calculate(){

        input();

        a = l * w;

        cout << "Area of ractangle is: " << a ;

    }
};

int main(){

    Area a1;
    a1.calculate();
    

    return 0;
}