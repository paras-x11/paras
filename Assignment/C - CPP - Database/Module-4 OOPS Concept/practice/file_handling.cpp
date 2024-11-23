#include <iostream>
#include <fstream>

using namespace std;

int main(){

    int roll_no, marks;
    string name;

    ofstream fout;          // for write data.
    ifstream fin;           // for read data.

    cout << "Enter Roll Number: ";
    cin >> roll_no;

    cout << "Enter Student Name: ";
    cin.ignore();
    getline(cin, name);

    cout << "Enter Marks: ";
    cin >> marks;

    fout.open("D:\\paras\\Assignment\\Module-4 OOPS Concept\\practice\\file.txt");      //for insert data

    fout << "\nRoll no: " << roll_no << endl;
    fout << "Name: " << name << endl;
    fout << "Marks: " << marks << endl;

    fout.close();


    fout.open("D:\\paras\\Assignment\\Module-4 OOPS Concept\\practice\\file.txt", ios::app);        // app for append
    
    fout << "\n\nline 4" << endl;
    fout << "line 5" << endl;
    fout << "line 6" << endl;

    fout.close();


    fin.open("D:\\paras\\Assignment\\Module-4 OOPS Concept\\practice\\file_handling.cpp");       // for read file data

    string line;
    cout << endl;
    while (getline(fin, line)) {
        cout << line << endl;
    }

    fin.close();

    fin.open("D:\\paras\\Assignment\\Module-3 Fundamentals of Programming\\practise\\file_handle.txt");

    string str;
    cout << endl;
    while (getline(fin, str)) {
        cout << str << endl;
    }

    fin.close();

    fin.open("D:\\paras\\Assignment\\Module-4 OOPS Concept\\practice\\file.txt");       // for read file data
    
    string line1;
    cout << endl;
    while (getline(fin, line1)) {
        cout << line1 << endl;
    }

    fin.close();


    return 0;
}