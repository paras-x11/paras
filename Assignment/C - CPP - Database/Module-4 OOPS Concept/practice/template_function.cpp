// 2. Write a program of to sort the array using templates 

#include <iostream>
using namespace std;

template <typename T> T A_sort(int a[5]){

    T i, j, temp;

    for(i=0; i<5; i++){
        for(j=0; j<5; j++){

            if(a[i] < a[j]){
                
                temp = a[j];
                a[j] = a[i];
                a[i] = temp;
            }
        }
    }

}

template <typename T> T D_sort(int a[5]){

    T i, j, temp;

    for(i=0; i<5; i++){
        for(j=0; j<5; j++){

            if(a[i] > a[j]){
                
                temp = a[j];
                a[j] = a[i];
                a[i] = temp;
            }
        }
    }
}

int main(){
    
    int i, ch, a[5];

    cout << "Enter array values: ";
    for(i=0; i<5; i++){
        cin >> a[i];
    }

    cout << "\nArray is: \n";
    for(i=0; i<5; i++){
        cout << a[i] << "\t";
    }

    A_sort<int>(a);
    
    cout << "\nAscending Array is: \n";
    for(i=0; i<5; i++){
        cout << a[i] << "\t";
    }


    D_sort<int>(a);
    
    cout << "\nDescending Array is: \n";
    for(i=0; i<5; i++){
        cout << a[i] << "\t";
    }

    
    cout << "\nOriginal Array is: \n";
    for(i=0; i<5; i++){
        cout << a[i] << "\t";
    }

    return 0;
}