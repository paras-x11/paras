// wap to find factorial.

#include <iostream>
using namespace std;

int main(){
    int n, fact=1;

    cout << "Enter number: ";
    cin >> n;

    while(n > 0){
        fact = fact * n;
        n--; 
    }

    cout << "\nFactorial is: " << fact <<endl;
    
    return 0;
}