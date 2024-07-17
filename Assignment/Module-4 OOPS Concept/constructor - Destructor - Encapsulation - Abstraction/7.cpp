// 7. Write a C++ program to implement a class called Date that has private member variables for day, month, and year. 
// Include member functions to set and get these variables, as well as to validate if the date is valid. 

#include <iostream>
using namespace std;

class Date{

    int d, m, y;

    public:

    Date(){

        cout << "Enter Day: ";
        cin >> d;

        cout << "Enter Month: ";
        cin >> m;

        cout << "Enter Year: ";
        cin >> y;
    }

    void check(){

        if( d <= 31 && m <= 12 && y > 0){
            
            if( ((m==1 || m==3 || m==5 || m==7 || m==8 || m==10 || m==12) && (d<=31)) || ((m==4 || m==6 || m==9 || m==11) && (d<=30)) ){
                cout << "\n-> Date: " << d << "/" << m << "/" << y;                
            }

            else if(m==2){

                if( (y % 4 == 0 && ( y % 400 == 0 || y % 100 != 0)) && d <= 29 ){
                   cout << "\n-> Date: " << d << "/" << m << "/" << y;                
                }
                else if(d <= 28){
                    cout << "\n-> Date: " << d << "/" << m << "/" << y;                
                }
                else{
                    cout << "\n-> Date is not valid.";
                }
            }

            else{
                cout << "\n-> Date is not valid.";
            }        
        }

        else{
            cout << "\n-> Date is not valid.";
        }
    }
};

int main(){

    Date d;

    d.check();   

    return 0;
}