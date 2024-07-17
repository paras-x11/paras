// 6. Write a C++ program to implement a class called Employee that has private member variables for name, employee ID, and salary.
// Include member functions to calculate and set salary based on employee performance. Using of constructor.

#include <iostream>
using namespace std;

class Employee{
    int e_id, salary, p_rate, net_salary;
    string name;

    public:

    Employee(){

        cout << "Enter Employee id: ";
        cin >> e_id;

        cout << "Enter Employee name: ";
        cin >> name;

        cout << "Enter Employee's basic salary: ";
        cin >> salary;  

        cout << "Enter Employee's performance (out of 10): ";
        cin >> p_rate;
    }

    int count(){
        net_salary = salary + ((salary * p_rate) / 100);
        return net_salary;
    }

    void display(){

        cout << "\n \nEmployee id: " << e_id << endl;

        cout << "Employee name: " << name << endl;

        cout << "Employee's basic salary: " << salary << endl;

        cout << "\nEmployee's performance (out of 10): " << p_rate << endl;

        cout << "Employee's net salary is: " << count();
    }

};

int main(){
    
    Employee e;

    e.display();

    return 0;
}