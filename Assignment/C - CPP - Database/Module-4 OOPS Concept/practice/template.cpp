// //template function syntax:

// #include <iostream>
// using namespace std;

// template <typename T> T name(T a, T b){
//     return a+b;
// };

// int main(){
    
//     cout << name  (4.5, 5.5);
//     return 0;
// }

//template class syntax:

#include <iostream>
using namespace std;

template <typename T> 
class name{
    public:
    name(T a, T b){
        cout << a+b;
    }
};

int main(){
    
    name <double> n (4, 5);
    return 0;
}