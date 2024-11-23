// 7. Write a C++ Program to illustrates the use of Constructors in multilevel inheritance.

#include <iostream>
using namespace std;

class student{
    protected:
    int roll_no;

    public:
    student(){
        cout << "Enter roll number: ";
        cin >> roll_no;
    }

    void show_no(){
        cout << "\nRoll no.: " << roll_no << endl;
    }
};

class test : public student{

    protected:
    int sub1, sub2;

    public:
    test(){

        cout << "Enter marks for subject 1: ";
        cin >> sub1;

        cout << "Enter marks for subject 2: ";
        cin >> sub2;
    }

    void show_marks(){
        show_no();
        cout << "Marks 1: " << sub1 << endl;
        cout << "Marks 2: " << sub2 << endl;
    }
};

class result : public test{

    int total;

    public:
    result(){
        
        show_marks();
        total = sub1 + sub2;
        cout << "Total marks: " << total << endl;
    }
};

int main(){
    
    result r;

    return 0;
}