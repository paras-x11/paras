// 16. Wap to create mark-sheets of 5 students using constructor.

#include <iostream>
using namespace std;

class marksheet{
    public: 
    string name;
    int roll_no, m1, m2, m3, t;

    public:
    marksheet(string n, int r, int m, int s, int e){
        name = n;
        roll_no = r;
        m1 = m;
        m2 = s;
        m3 = e;
        t = m1 + m2 + m3;
    }

    void display(){
        cout << "\n\nRoll No.: " << roll_no << endl;
        cout << "Name: " << name << endl;
        cout << "Marks in Maths: " << m1 << endl;
        cout << "Marks in Science: " << m2 << endl;
        cout << "Marks in English: " << m3 << endl;
        cout << "Total Marks: " << t << endl << endl;
    }
};

int main(){
    int m, s, e, r;
    string n;

    marksheet* marks[5];                    //if we pass values by constructor then we make pointer object and use arrow -> for func. call

    for(int i=0; i<5; i++){

        cout << "\n\nEnter roll no.: ";
        cin >> r;

        cout << "Enter name: ";
        cin.ignore();
        getline(cin, n);

        cout << "Enter maths: ";
        cin >> m;

        cout << "Enter science: ";
        cin >> s;

        cout << "Enter english: ";
        cin >> e;

        marks[i] = new marksheet(n, r, m, s, e);
    }
    
    for(int i=0; i<5; i++){
        
        marks[i]->display();
    }

    return 0;
}

