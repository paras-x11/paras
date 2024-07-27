#include <iostream>
#include <string>
using namespace std;

class lecture {
private:
    string lecturer_name;
    string subject_name;
    string course_name;
    int num_lectures;

public:
    lecture(string name, string subject, string course, int num) {
        lecturer_name = name;
        subject_name = subject;
        course_name = course;
        num_lectures = num;
    }

    lecture() {}

    void setDetails() {
        cout << "Enter Lecturer Name: ";
        getline(cin, lecturer_name);

        cout << "Enter Subject Name: ";
        getline(cin, subject_name);

        cout << "Enter Course Name: ";
        getline(cin, course_name);

        cout << "Enter Number of Lectures: ";
        cin >> num_lectures;

        // Consume newline character after inputting integer
        cin.ignore();
    }

    void displayDetails() {
        cout << "Lecturer Name: " << lecturer_name << endl;
        cout << "Subject Name: " << subject_name << endl;
        cout << "Course Name: " << course_name << endl;
        cout << "Number of Lectures: " << num_lectures << endl;
    }
};

int main() {
    lecture lecturers[5] = {
        lecture("Anjana ladd", "Computer Science", "Programming", 3),
        lecture("Vinod Singh", "Mathematics", "Algebra", 2),
        lecture("Pradeep Sharma", "Physics", "Mechanics", 4),
        lecture("Deepa Mittal", "History", "World Wars", 5),
        lecture("Pranati Singh", "Biology", "Genetics", 3)
    };

    // Input details for each lecturer
    for (int i = 0; i < 5; ++i) {
        cout << "Enter additional details for Lecture " << i + 1 << ":" << endl;
        lecturers[i].setDetails();
        cout << endl;
    }

    // Display details of each lecturer
    cout << "Lecture Details:" << endl;
    for (int i = 0; i < 5; ++i) {
        cout << "Lecture " << i + 1 << ":" << endl;
        lecturers[i].displayDetails();
        cout << endl;
    }

    return 0;
}




