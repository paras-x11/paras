// 3. Write a C++ program to create a class called Car that has private member variables for company, model, and year. 
// Implement member functions to get and set these variables. 

#include <iostream>
using namespace std;

class car{
    string company, model;
    int year;

    public: 
    void set_details(string c, string m, int y){

        company = c;
        model = m;
        year = y;
    }

    void display();
};

void car :: display(){
    cout << endl << "You entered: " << endl;;
    cout << "Company: " << company << endl;
    cout << "Model: " << model << endl;
    cout << "Year: " << year << endl;
}

int main(){
    
    car c1;

    string c, m;
    int y;

    cout << "Enter company: ";
    cin >> c;

    cout << "Enter Model: ";
    cin >> m;

    cout << "Enter Year: ";
    cin >> y;

    c1.set_details(c, m, y);
    c1.display();

    return 0;
}