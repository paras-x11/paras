// Create a lecture management System:
// Make sure each business logic is denoted with appropriate comments and make your code interactive and represent clean and clear output on your
// console screen.
// Adhere to the coding principles

// Define a class to represent lecture details. Include the following members and the program should handle at least details of 5 lecturers.
// Data members:
// a) Name of the lecturer
// b) Name of the subject
// c) Name of course
// d) Number of lectures

// Data functions:
// a) To assign initial values
// b) To add a lecture details
// c) To display name and lecture details

// Make sure you have to use constructor concept in it
// Make sure all naming conversion properly mention in this project work
// Make sure all method name
// Use class and object concepts
// Upload all features in develop branch after completion all features merge it with the main branch.

#include <iostream>
using namespace std;

class Lecture_Details{
    public:
    string name, subject, course;
    int lectures;

    public:

    Lecture_Details(){
        cout << "\nEnter Lecturer Name: ";
        getline(cin, name);

        cout << "Enter Subject Name: ";
        getline(cin, subject);

        cout << "Enter Course Name: ";
        getline(cin, course);

        cout << "Enter Number of lecturers: ";
        cin >> lectures;

        cin.ignore();
    }

    void display_Details(){
        cout << "\nLecturer Name: " << name << endl;
        cout << "Subject Name: " << subject << endl;
        cout << "Course Name: " << course << endl;
        cout << "Number of Lectures: " << lectures << endl;
    }
};

int main(){
    
    int i;
   
    Lecture_Details l1[5];

    for(i=0; i<5; i++){
        l1[i];
    }

    for(i=0; i<5; i++){
        l1[i].display_Details();
    }

    return 0;
}