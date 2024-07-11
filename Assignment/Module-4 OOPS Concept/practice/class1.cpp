// #include <iostream>
// using namespace std;

// class emp{
//     public:
//     int id;
//     string name;

//     public:
//     void getData(){
//         cout << "enter id: ";
//         cin >> id;

//         cout << "enter name: ";
//         cin >> name;
//     }

//     void show(){
//         cout << "id: " << id << "\n" << "name: " << name << endl;
//     }
// };

// int main(){

//     emp e, e2;
//     e.getData();                         // dot(.) is a member access operator
//     e2.getData();

//     e.show();    
//     e2.show();

//     return 0;
// }

#include <iostream>
using namespace std;

class student{
    private:
    int roll_no;
    string name;

    public:
    int set_rollno(int no){
        roll_no = no;
    }

    int set_name(string nm){
        name = nm;
    }

    void show(){
        cout << "roll no: " << roll_no<< "\n" << "name: " << name << endl;
    }
};

int main(){

    student st, st2;

    st.set_rollno(21);
    st.set_name("krishna");
    st.show();
    
    return 0;
}