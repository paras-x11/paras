#include <iostream>
using namespace std;

inline int factorial(int n){

    if(n==0 || n==1){
        return 1;
    }
    else{
        return n * factorial(n-1);
    }
}

int main(){
    
    int num;

    cout << "enter number: ";
    cin >> num;

    cout << "\n\n-> Factorial of " << num << " is: " << factorial(num);

    return 0;
}



// factorial(0) = 1
// factorial(n) = n * n-1 *....1
// factorial(5) = 5 * 4 * 3 * 2 * 1 = 120
// factorial(n) = n * factorial(n-1)