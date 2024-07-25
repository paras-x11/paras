// Create a lecture management System:
// Make sure each business logic is denoted with appropriate comments and make your code interactive and represent clean and clear output on your
// console screen.
// Adhere to the coding principles

// Define a class to represent lecture details. Include the following members and the program should handle at least details of 5 lecturers.
// Data members:
// a) Name of the lecturer
// b) Name of the subject
// c) Name of course
// d) Number of lecturers

// Data functions:
// a) To assign initial values
// b) To add a lecture details
// c) To display name and lecture details

// Make sure you have to use constructor concept in it
// Make sure all naming conversion properly mention in this project work
// Make sure all method name
// Use class and object concepts
// Upload all features in develop branch after completion all features merge it with the main branch.

// ?????????????????????????????    ↓

#include <iostream>
#include <string>
using namespace std;

class Lecturer {
private:
    string name;     
    string subject;   
    string course;   
    int numLectures;  

public:
    Lecturer(string n = "", string s = "", string c = "") : name(n), subject(s), course(c), numLectures(0) {}

    void setDetails(string n, string s, string c, int num) {
        name = n;
        subject = s;
        course = c;
        numLectures = num;
    }

    void displayDetails() {
        cout << "Name: " << name << endl;
        cout << "Subject: " << subject << endl;
        cout << "Course: " << course << endl;
        cout << "Number of Lectures: " << numLectures << endl;
    }
};

int main() {
    int numLecturers;

    cout << "Enter the number of lecturers (at least 5): ";
    cin >> numLecturers;
    cin.ignore();  

    if (numLecturers < 5) {
        cout << "Number of lecturers should be at least 5. Setting to 5." << endl;
        numLecturers = 5;
    }

    Lecturer* lecturers = new Lecturer[numLecturers];

    for (int i = 0; i < numLecturers; i++) {
        string name, subject, course;
        int numLectures;

        cout << "Enter the details for lecturer " << (i + 1) << ":" << endl;

        cout << "Name: ";
        getline(cin, name);

        cout << "Subject: ";
        getline(cin, subject);

        cout << "Course: ";
        getline(cin, course);

        cout << "Number of Lectures: ";
        cin >> numLectures;
        cin.ignore();  

        lecturers[i].setDetails(name, subject, course, numLectures);
        cout << "----------------------" << endl;
    }

    for (int i = 0; i < numLecturers; i++) {
        lecturers[i].displayDetails();
        cout << "----------------------" << endl;
    }

    delete[] lecturers;

    return 0;
}
