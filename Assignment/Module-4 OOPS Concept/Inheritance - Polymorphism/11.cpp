// 11. Write a program to calculate the area of circle, rectangle and triangle 
// using Function Overloading 
// Rectangle: Area = length * breadth
// Triangle: Area = 0.5 * base * height 
// Circle: Area = π * radius^2

#include <iostream>
using namespace std;

class calculate_area{
    
    public:
    int area(int l, int w){
        cout << "\n\nArea of rectangle is: " << l * w;
    }

    int area(int b, int h, bool isTriangle){
        cout << "\nArea of Triangle is: " << 0.5 * b * h;
    }

    int area(int r){
        cout << "\nArea of circle is: " << 3.14 * r * r;
    }
};

int main(){
    
    calculate_area a;

    a.area(10, 5);

    a.area(8, 6, true);

    a.area(3);

    return 0;
}