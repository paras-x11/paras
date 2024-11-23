// 10. Write a program to concatenate the two strings using Operator Overloading 

#include <iostream>
using namespace std;

class overload{
    public:
    string str, res;

    public:
    overload(string s){
        str = s;
    }

    string operator +(overload &obj){
        res = str + obj.str;
        return res;
    }
};

int main(){
    string s1, s2;

    cout << "Enter first string: ";
    getline(cin, s1);

    cout << "Enter second string: ";
    getline(cin, s2);

    overload o1(s1);
    overload o2(s2);

    cout << "\nString is: " << o1 + o2;

    return 0;
}