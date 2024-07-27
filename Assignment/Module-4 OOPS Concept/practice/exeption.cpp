#include <iostream>
using namespace std;

int main(){
    
    double n;

    cout << "enter number: ";
    cin >> n;

    try{
        if(n<=0){
            throw runtime_error("Not divided by zero.");
        }

        else{
            cout << "answer: " << 100/n;
        }
    }

    catch(exception &e){
        cout << "Exception: " << e.what() << endl;
    }
    return 0;
}