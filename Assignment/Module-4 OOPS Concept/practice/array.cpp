#include <iostream>
using namespace std;

int main(){
    int i, j, temp, n;

    cout << "enter size of array: ";
    cin >> n;

    int arr[n];

    for(i=0; i<n; i++){
        cin >> arr[i] ;
    }
    
    for(i=0; i<n; i++){
        cout << arr[i] << "\t" ;
    }

    cout << endl;

    for(i=0; i<n; i++){
        for(j=0; j<n; j++){

            if(arr[i] < arr[j]){
                temp = arr[j];
                arr[j] = arr[i];
                arr[i] = temp;
            }
        }        
    }
    
    for(i=0; i<n; i++){
        cout << arr[i] << "\t" ;
    }

    return 0;
}