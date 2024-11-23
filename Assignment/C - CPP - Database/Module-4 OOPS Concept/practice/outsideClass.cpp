// function body defining outside the class
// syntax: return_type className :: member_function_name()

#include <iostream>
using namespace std;

class emp{
    public:
    int id;
    string name;

    public:
    void getData();
    void show();
    
};

void emp :: getData(){
    cout << "enter id: ";
    cin >> id;

    cout << "enter name: ";
    // cin >> name;
    cin.ignore();
    getline(cin, name);
}

void emp :: show(){
    cout << "id: " << id << "\n" << "name: " << name << endl;
}

int main(){

    emp e, e2;
    e.getData();
    e2.getData();               // dot(.) is a member access operator

    e.show();    
    e2.show();

    return 0;
}