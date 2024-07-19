// ~

#include <iostream>
using namespace std;

class student{
    int sid;
    string name;

    public:
    student(){
        cout << "Enter student id: ";
        cin >> sid;

        cout << "Enter name: ";
        cin >> name;
    }

    void show(){
        cout << "\nStudent id: " << sid << endl;
        cout << "Student name: " << name << endl;
    }

    ~student(){

        cout << "\n-> I am Destructor.";
    }
};

int main(){
    
    student s;
    s.show();

    return 0;
}