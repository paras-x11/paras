// prg to calculate area of circle, rectangle and triangle using switch case:

#include <iostream>
using namespace std;

int r, l, w, b, h;

void circle(){

    int area_c;

    cout << "enter radius of circle: ";
    cin >> r;

    area_c = 3.14 * r * r;
    cout << "Area of circle is: " << area_c << endl;

}

void rectangle(){
    int area_r;

    cout << "enter length of reactangle: " ;
    cin >> l;

    cout << "enter width of reactangle: " ;
    cin >> w;

    area_r = l * w;
    cout << "Area of circle is: " << area_r << endl;

}

void triangle(){
    int area_t;

    cout << "enter base of triangle: " ;
    cin >> b;

    cout << "enter height of triangle: " ;
    cin >> h;

    area_t = (b*h) / 2;
    cout << "Area of triangle is: " << area_t << endl;

}

int main(){
    int ch;

    cout << "Enter 1 for find area of circle: " << endl;
    cout << "Enter 2 for find area of rectangle: " << endl;
    cout << "Enter 3 for find area of triangle: " << endl;

    cout << "enter your choice: ";
    cin >> ch;

    switch (ch)
    {
    case 1: circle();
        break;

    case 2: rectangle();
        break;

    case 3: triangle();
        break;
    
    default: cout << "invalid choice." << endl;
        break;
    }

    return 0;
}