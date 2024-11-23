// 15. WAP of constructor overloading to find average of  2,3,4 numbers.

#include <iostream>
using namespace std;

class average{

    public:
    int avg(int a, int b){
        return (a + b) / 2;
    }

    int avg(int a, int b, int c){
        return (a + b + c) / 3;
    }

    int avg(int a, int b, int c, int d){
        return (a + b + c + d) / 4;
    }
};

int main(){
    
    average a;

    cout << "avg of 2 numbers: " << a.avg(45, 65) << endl;

    cout << "avg of 3 numbers: " << a.avg(56, 22, 38) << endl;;

    cout << "avg of 4 numbers: " << a.avg(95, 78, 56, 47) << endl;;

    return 0;
}