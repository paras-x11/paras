#include <iostream>
using namespace std;

int main(){
    int n, fact=1;

    cout << "Enter number: ";
    cin >> n;

    for(; n>0; n-- ){
        
        fact = fact * n;
    }

    cout << "factorial: "<< fact;

    return 0;
}