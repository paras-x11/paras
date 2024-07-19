// 4. Write a C++ Program display Student Mark sheet using Multiple inheritance.

#include <iostream>
using namespace std;

class student_info{

    protected:
    int sid, std;
    string name;
    char div; 

    public:
    void input_info(){

        cout << "Enter Student id: ";
        cin >> sid;

        cout << "Enter Student's name: ";
        cin.ignore();
        cin >> name;

        cout << "Enter Student's standard: ";
        cin >> std;

        cout << "Enter Student's division: ";
        cin >> div;
    }

    void display_info(){

        cout << "\nStudent id: " << sid << endl;
        cout << "Name: " << name << endl;
        cout << "Standard: " << std << endl;
        cout << "Division: " << div << endl;
    }
};

class marks{

    protected:
    int m, s, e;

    public:
    void input_marks(){

        cout << "Maths: ";
        cin >> m;

        cout << "Science: ";
        cin >> s;

        cout << "English: ";
        cin >> e;
    } 

    void display_marks(){

        cout << "\nObtained marks: " << endl;
        cout << "Maths: " << m << endl;

        cout << "Science: " << s << endl;

        cout << "English: " << e << endl;
    }
};

class marksheet : protected student_info, protected marks{

    public:
    void input(){

        cout << "\nEnter Student information: " << endl;
        input_info();

        cout << "\nEnter marks: " << endl;
        input_marks();
    }

    float percentage(){

        return ( (m + s + e) * 100.0 ) / 300.0;
    }

    void display(){

        cout << "\nStudent Marksheet: " << endl;
        display_info();
        display_marks();

        cout << "\nTotal Marks is: " << m+s+e << endl;
        cout << "Percentage is: " << percentage() << "%" << endl << endl;
    }
};

int main(){
    
    marksheet ms;

    ms.input();
    
    ms.display();

    return 0;
}