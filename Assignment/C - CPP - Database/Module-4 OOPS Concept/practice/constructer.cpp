// default constructer: there is no parameter pass in constructor 
// default constructer(if not created by user): always created by compiler but not allocate memory
// default constructer(created by user): allocate memory

// constructor is normally used to assign values.

#include <iostream>
using namespace std;
class points{
    int singing, dance;

    public:
    points(){               // default constructer
        cout << "enter singing: ";
        cin >> singing;

        cout << "enter dance: ";
        cin >> dance;
    }          

    void show(){
        cout << "singing: " << singing << endl << "Dancing: " << dance << endl;
    } 
};

int main(){
    
    points p;
    p.show();

    points p1;
    p1.show();

    return 0;
}
