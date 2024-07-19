//WAP to check wether a given number is even or odd using if else.

#include <iostream>
using namespace std;

int main(){
    int n;

    cout << "enter number: ";
    cin >> n;
    if(n>0){
        if(n % 2 == 0){
            cout << "\n" << n << " is even number." << endl;
        }
        else{
            cout << "\n" << n << " is odd number." << endl;
        }
    }
    else{
        cout << "\nzero is not even nor odd.";
    }
    return 0;
}