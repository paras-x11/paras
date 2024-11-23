// fibonacci series: 0,1,1,2,3,5,8,13,21,54

#include <iostream>
using namespace std;

int main(){
    int n, a=0, b=1;
    int temp=0, count=2;

    cout << "enter number: ";
    cin >> n;

    cout << a << "," << b;
    // while(count <= n){

    //     temp = a + b;
    //     a = b;
    //     b = temp;
    //     count++;
    //     cout << "," << temp;
    // }

    for(int i=2; i<n; i++){
        temp = a + b;
        a = b;
        b = temp;
        cout << "," << temp;
    }
    return 0;
}