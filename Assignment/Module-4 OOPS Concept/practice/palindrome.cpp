#include <iostream>
using namespace std;

int main(){
    int n, rev=0, rem;

    cout << "Enter number: ";
    cin >> n;

    int temp = n;
    do{
        rem = n % 10;
        rev = rev * 10 + rem ;
        n = n / 10;
    }while(n!=0);

    cout << "Reverse number is: " << rev << endl;

    if(temp == rev){
        cout << "palindrome.";
    }
    else{
        cout << "not palindrome.";
    }
    return 0;
}