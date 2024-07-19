// accessing private member outside the scope:
#include <iostream>
using namespace std;

class rohit{
    private:
    int money1 = 900;

    private:
    friend int f1(rohit);
};

class paras{
    private:
    int money2 = 1100;

    private:
    friend int f2(paras);
};

int f1(rohit r){

    return r.money1;
}

int f2(paras p){

    return p.money2;
}


int main(){
    int m;
    rohit r1;
    paras p1;

    cout << "money 1 is: " << f1(r1) << endl;
    cout << "money 2 is: " << f2(p1) << endl;

    m  = f1(r1) + f2(p1);
    cout<<"\nTotal: "<< m;

    return 0;
}