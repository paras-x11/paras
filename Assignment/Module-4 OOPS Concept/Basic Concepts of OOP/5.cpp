// 5. WAP  to create class called rectangle that has private member variables for length and width.
// Implement member function to calculate the rectangle's area and perimeter.

#include <iostream>
using namespace std;

class rectangle{
    int l, w;
    
    public:
    int area(int l, int w){
        return l * w;
    }
    
    int perimeter(int l, int w){
        return 2 * (l + w);
    }
};

int main()
{   
    rectangle r1;
    int length, width;
    
    cout << "Enter length of rectangle: ";
    cin >> length;
    
    cout << "Enter width of rectangle: ";
    cin >> width;
    
    cout << endl;
    cout << "Area of rectangle is: " << r1.area(length, width) << endl;
    cout << "Perimeter of rectangle is: " << r1.perimeter(length, width) << endl;
    
    return 0;
}

