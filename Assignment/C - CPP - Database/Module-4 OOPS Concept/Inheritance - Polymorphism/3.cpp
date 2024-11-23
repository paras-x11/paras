// 3. Create a class person having members name and age. Derive a class student having member percentage. 
// Derive another class teacher having member salary. Write necessary member function to initialize, read and write data (Multiple Inheritance).

#include <iostream>
using namespace std;

class Person{

    string name;
    int age;

    public:
    void input(){
        cout << "Enter name: ";
        cin.ignore();
        getline(cin, name);

        cout << "Enter age: ";
        cin >> age;
    }

    void p_display(){
        cout << "\nName: " << name << endl;
        cout << "Age: " << age << endl;
    }
};

class Student : protected Person{

    int p;

    public:
    void percentage(){
        input();

        cout << "Enter percentage: ";
        cin >> p;
    }

    void s_display(){
        p_display();
        cout << "Percentage: " << p << endl; 
    }
};

class Teacher : protected Person{

    int s;

    public: 
    void salary(){
        input();

        cout << "Enter salary: ";
        cin >> s;
    }

    void t_display(){

        p_display();
        cout << "Salary: " << s << endl;
    }

};



int main(){

    Student s1;
    Teacher t1;

    cout << "Enter student Info: " << endl;
    s1.percentage();

    cout << "\nEnter Teacher Info: " << endl;
    t1.salary();

    cout << "\nStudent Info: " << endl;
    s1.s_display();

    cout << "\nTeacher Info: " << endl;
    t1.t_display();

    return 0;
}