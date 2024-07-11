// constructor overloading: program having more than one constructor.

#include <iostream>
using namespace std;

class rectangle{
    public:
    int length, width;

    public: 
    rectangle();
    rectangle(int, int);
    rectangle(const rectangle &obj);
    int area();
    int perimeter(){
        return 2 * (length + width);
    }
};

rectangle :: rectangle(){                                   // default constructor body outside class
    cout << "enter length: ";
    cin >> length;

    cout << "enter width: ";
    cin >> width;
}  

rectangle :: rectangle(int l, int w){                       // parameterized constructor body outside class
    length = l;
    width = w;
}

rectangle :: rectangle(const rectangle &obj){               // copy constructor body outside class
    length = obj.length;
    width = obj.width;
}

int rectangle :: area(){
    return length * width;
}

int main(){

    rectangle r1;
    cout << endl << "r1: Area with default constructor r1: " << r1.area() << endl;
    cout << "r1: Perimeter with default constructor r1: " << r1.perimeter() << endl;

    rectangle r2(10,2);
    cout << endl << "r2: Area with parameterized constructor r2: " << r2.area() << endl;
    cout << "r2: Perimeter with parameterized constructor r2: " << r2.perimeter() << endl;

    rectangle r3 = r1;
    cout << endl << "r3: Area with copy from default constructor r1: " << r3.area() << endl;
    cout << "r3: Perimeter with copy from default constructor r1: " << r3.perimeter() << endl;

    rectangle r4 = r2;
    cout << endl << "r4: Area with copy from default constructor r2: " << r4.area() << endl;
    cout << "r4: Perimeter with copy from default constructor r2: " << r4.perimeter() << endl;
    
    return 0;
}