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


// #include <iostream>
// #include <string>
// using namespace std;

// class lecture {
// private:
//     string lecturer_name;
//     string subject_name;
//     string course_name;
//     int num_lectures;

// public:
//     lecture(string name, string subject, string course, int num) {
//         lecturer_name = name;
//         subject_name = subject;
//         course_name = course;
//         num_lectures = num;
//     }

//     lecture() {}

//     void setDetails() {
//         cout << "Enter Lecturer Name: ";
//         getline(cin, lecturer_name);

//         cout << "Enter Subject Name: ";
//         getline(cin, subject_name);

//         cout << "Enter Course Name: ";
//         getline(cin, course_name);

//         cout << "Enter Number of Lectures: ";
//         cin >> num_lectures;

//         // Consume newline character after inputting integer
//         cin.ignore();
//     }

//     void displayDetails() {
//         cout << "Lecturer Name: " << lecturer_name << endl;
//         cout << "Subject Name: " << subject_name << endl;
//         cout << "Course Name: " << course_name << endl;
//         cout << "Number of Lectures: " << num_lectures << endl;
//     }
// };

// int main() {
//     lecture lecturers[5] = {
//         lecture("Anjana ladd", "Computer Science", "Programming", 3),
//         lecture("Vinod Singh", "Mathematics", "Algebra", 2),
//         lecture("Pradeep Sharma", "Physics", "Mechanics", 4),
//         lecture("Deepa Mittal", "History", "World Wars", 5),
//         lecture("Pranati Singh", "Biology", "Genetics", 3)
//     };

//     // Input details for each lecturer
//     for (int i = 0; i < 5; ++i) {
//         cout << "Enter additional details for Lecture " << i + 1 << ":" << endl;
//         lecturers[i].setDetails();
//         cout << endl;
//     }

//     // Display details of each lecturer
//     cout << "Lecture Details:" << endl;
//     for (int i = 0; i < 5; ++i) {
//         cout << "Lecture " << i + 1 << ":" << endl;
//         lecturers[i].displayDetails();
//         cout << endl;
//     }

//     return 0;
// }




