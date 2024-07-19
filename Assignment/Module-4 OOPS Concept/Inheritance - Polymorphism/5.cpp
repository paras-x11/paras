// 5. Assume that the test results of a batch of students are stored in three different classes. Class Students are storing the roll number. 
// Class Test stores the marks obtained in two subjects and class result contains the total marks obtained in the test. 
// The class result can inherit the details of the marks obtained in the test and roll number of students. (Multilevel Inheritance).

#include <iostream>
using namespace std;

class student{
    protected:
    int roll_no;

    public:
    void get_no(){
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
    void get_marks(){

        get_no();
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
    void show_result(){
        
        get_marks();
        show_marks();
        total = sub1 + sub2;
        cout << "Total marks: " << total << endl;
    }
};

int main(){
    
    result r;

    r.show_result();

    return 0;
}