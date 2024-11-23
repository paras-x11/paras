// 2. Write a program of to sort the array using templates 

#include <iostream>
using namespace std;

template <typename T> 
class sort{
    private:
    T i, j, temp;

    public:
    T A_sort(T a[5]){

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

    T D_sort(T a[5]){

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
};

int main(){
    sort<int> s;
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
    case 1: s.A_sort(a);
        break;
    
    case 2: s.D_sort(a);
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