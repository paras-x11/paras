// 6. implement func overriding 

#include <iostream>
using namespace std;

class Phone{
    public:
    
    void Ring(){
        cout << "\nRinging Phone.";
    }
};

class SmartPhone : public Phone{
    public:
    
    void Ring(){
        cout << "\nRinging Smart Phone.";
    }
};

int main(){
    
    SmartPhone s;
    s.Ring();

    Phone p;
    p.Ring();

    return 0;
}