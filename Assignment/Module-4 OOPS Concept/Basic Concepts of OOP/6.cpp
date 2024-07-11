// 6. WAP to create a class called person that has private member variables for name, age and country.
// implement member function to set and get the values of these variables.

#include <iostream>
using namespace std;

class person{
    string name, age, country;
    
    public:
    void get_details(){
        cout << "Enter name: ";
        cin >> name;
        
        cout << "Enter age: ";
        cin >> age;
        
        cout << "Enter country: ";
        cin >> country;
    }
    
    void display(){
        cout << endl;
        cout << "Name: " << name << endl;
        cout << "Age: " << age << endl;
        cout << "Country: " << country << endl;
    }
};

int main()
{   
   person p;
   
   p.get_details();
   p.display();
    
    return 0;
}

/*
#include <iostream>
using namespace std;

class person{
    string name, country;
    int age;
    
    public:
    void set_details(string n, int a, string c){
        name = n;
        age = a;
        country = c;
    }
    
    void display(){
        cout << endl;
        cout << "Name: " << name << endl;
        cout << "Age: " << age << endl;
        cout << "Country: " << country << endl;
    }
};

int main()
{   
    person p;
    string n, c;
    int a;
   
    cout << "Enter name: ";
    cin >> n;
        
    cout << "Enter age: ";
    cin >> a;
        
    cout << "Enter country: ";
    cin >> c;
        
    p.set_details(n, a, c);
    p.display();
    
    return 0;
}
*/