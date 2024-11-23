// WAP to get and display odd numbers using constructor and destructor.

#include <iostream>
using namespace std;

class odd{

    public:
    odd(int n){

        for(int i=0; i<=n; i++){

            if(i%2 != 0){
                cout << i << ", ";
            }
        }        
    }

    ~odd(){
        cout << "\n\nDestructor: All Resources Cleared.";
    }
};

int main(){
    int limit;

    cout << "Enter limit: ";
    cin >> limit;

    cout << "\nOdd numbers till " << limit << " are: " << endl;
    odd o(limit);    

    return 0;
}