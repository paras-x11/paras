//Write a menu driven prg to calculate area of circle, rectangle, triangle.

#include <iostream>
using namespace std;

#define pi 3.14

inline int circle(int r){
    return pi*r*r;
}

inline int rectangle(int l, int w){
    return l*w;
}

inline int triangle(int b, int h){
    return (b*h) / 2;
}

int main(){

    int r, l, w, b, h;
    int ch;

    while(1){
    cout << "\n\nEnter 1 for find area of circle: " << endl;
    cout << "Enter 2 for find area of rectangle: " << endl;
    cout << "Enter 3 for find area of triangle: " << endl;

    cout << "\nenter your choice: ";
    cin >> ch;

    switch (ch)
    {
    case 1: cout << "\nenter radius of circle: ";
            cin >> r;

            cout << "-> Area of circle is: " << circle(r) << endl;
        break;

    case 2: cout << "\nenter length of reactangle: " ;
            cin >> l;

            cout << "enter width of reactangle: " ;
            cin >> w;

            cout << "-> Area of circle is: " << rectangle(l, w) << endl;
        break;

    case 3: cout << "\nenter base of triangle: " ;
            cin >> b;

            cout << "enter height of triangle: " ;
            cin >> h;

            cout << "-> Area of triangle is: " << triangle(b, h) << endl;
        break;

    case 0: cout << "\n-> Exited.";
            exit(0);
        break;
    
    default: cout << "\n-> invalid choice." << endl;
        break;
    }
    }
    

    return 0;
}