// 8. Write a C++ program to implement a class called Student that has private member variables for name, class, roll number, and marks. 
// Include member functions to calculate the grade based on the marks and display the student's information. 
// Accept address from each student implement using of aggregation.

#include <iostream>
using namespace std;

class address{
    public:
    string add;

    public:
    address(string str){
        add = str;
    }
};

class student{
    private: 
    address *a;
    string name;
    int Class, roll_no, marks;

    public:

    student(string n, int c, int r, int m, address *a1){
        name = n;
        Class = c;
        roll_no = r;
        marks = m;
        this->a = a1;
    }

    void display(){
        cout << "Name: " << name << endl;
        cout << "Class: " << Class << endl;
        cout << "Roll no.: " << roll_no << endl;
        cout << "Marks: " << marks << endl;
        cout << "Address: " << a->add << endl;
    }
};

int main(){
    
    address add("101, sagrampura main road, surat.");

    student s("paras", 10, 22, 100, &add);

    s.display();

    return 0;
}