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

    cout << "\nAscending Array is: \n";
    for(i=0; i<5; i++){
        cout << a[i] << "\t";
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

    cout << "\nDescending Array is: \n";
    for(i=0; i<5; i++){
        cout << a[i] << "\t";
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

    while(1){
    cout << "\n\nEnter 1 for Ascending sort \t 2 for Descending sort: ";
    cin >> ch;

    switch (ch)
    {
    case 1: A_sort<int>(a);
        break;
    
    case 2: D_sort<int>(a);
        break;

    case 0: cout << "\n-> Exited";
            exit(0);
        break;

    default: cout << "-> Enter valid choice.\n";
        break;
    }
    }

    return 0;
}