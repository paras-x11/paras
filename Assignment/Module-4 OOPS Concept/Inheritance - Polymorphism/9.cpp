// 9. Write a Program of Two 1D Matrix Addition using Operator Overloading 

#include <iostream>
using namespace std;

class overload{
    public:
    int i, arr[5], res[5];

    public:
    overload(int a[5]){
        for(i=0; i<5; i++){
            arr[i] = a[i];
        }
    }

    int operator +(overload &obj){
        for(i=0; i<5; i++){
            res[i] = arr[i] + obj.arr[i];
        }

        cout << "\n\nAddition: ";
        for(i=0; i<5; i++){
            cout << res[i] << "\t";
        }
    }
    
};

int main(){
    int i, a1[5], a2[5];
    
    cout << "Enter array1: ";
    for(i=0; i<5; i++){
        cin >> a1[i];
    }

    cout << "\nEnter array2: ";
    for(i=0; i<5; i++){
        cin >> a2[i];
    }

    cout << "\nArray1:   ";
    for(i=0; i<5; i++){
        cout << a1[i] << "\t";
    }

    cout << "\nArray2:   ";
    for(i=0; i<5; i++){
        cout << a2[i] << "\t";
    }

    overload o1(a1);
    overload o2(a2);

    o1 + o2;

    return 0;
}