// 4. Write a C++ program to implement a class called Circle that has private member variables for radius. 
// Include member functions to calculate the circle's area and circumference. 

#include <iostream>
using namespace std;

#define pi 3.14

class circle{
    private:
    int r, a, c;

    public:
    int area(int r){

        a = pi * r * r;
        return a;
    }

    int cirumference(int r){
        
        c = 2 * pi * r; 
        return c;
    }
};

int main(){
    int radius;
    circle c1;

    cout << "Enter Radius: ";
    cin >> radius;

    cout << "Area is: " << c1.area(radius) << endl;
    cout << "Circumference is: "<< c1.cirumference(radius);
    
    return 0;
}