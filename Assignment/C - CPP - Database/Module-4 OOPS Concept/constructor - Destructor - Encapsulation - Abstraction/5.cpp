// 5. Write a C++ program to create a class called Triangle that has private member variables for the lengths of its three sides. 
// Implement member functions to determine if the triangle is equilateral, isosceles, or scalene.

// equilateral: all 3 sides are equal.
// isosceles: any 2 sides are equal.
// scalene: each side is different.

#include <iostream>
using namespace std;

class triangle{
    int a, b, c;

    public:

    void set_details(int s1, int s2, int s3){
        
        a = s1;
        b = s2;
        c = s3;
    }

    void check(){

        if( a+b <= c || b+c <= a || a+c <= b){

            cout << "\n-> Triangle is not formed.";
        }
        else{

            if( a == b && b == c){
                cout << "\n-> Triangle is equilateral.";
            }

            else if( a == b || b == c || a == c){
                cout << "\n-> Triangle is isosceles.";
            }

            else{
                cout << "\n-> Triangle is scalene.";
            }
        }
    }

};

int main(){
    
    triangle t;

    int a, b, c;

    cout << "Enter side 1: ";
    cin >> a;

    cout << "Enter side 2: ";
    cin >> b;

    cout << "Enter side 3: ";
    cin >> c;

    t.set_details(a, b, c);

    t.check();

    return 0;
}

