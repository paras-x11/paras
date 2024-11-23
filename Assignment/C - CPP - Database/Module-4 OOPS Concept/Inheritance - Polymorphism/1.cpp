// 1. Assume a class cricketer is declared. Declare a derived class batsman from cricketer. 
// Data member of batsman. Total runs, Average runs and best performance. 
// Member functions input data, calculate average runs, Display data. (Single Inheritance).

#include <iostream>
using namespace std;

class Cricketer{

    protected:
    int age;
    string name;

    public: 

    void get(){
        cout << "Enter cricketer's name: ";
        getline(cin, name);
        
        cout << "Enter cricketer's age: ";
        cin >> age;
    }

    void display(){
        cout << "\nName: " << name << endl;
        cout << "Age: " << age << endl;
    }
};

class batsman : public Cricketer{
    int t_runs, t_match, avg_runs, best_score;

    public:
    void input(){

        get();
        cout << "Enter total match played: ";
        cin >> t_match;

        cout << "Enter total run: ";
        cin >> t_runs;
        
        cout << "Enter best sore: ";
        cin >> best_score;            
    }

    void caclulate(){

        avg_runs = t_runs / t_match;
        cout << "Average run: " << avg_runs << endl;
    }
  
    void show(){
        display();
        cout << "Total match played: " << t_match << endl;
        cout << "Total run: " << t_runs << endl;
        cout << "Best score is: " << best_score << endl << endl;
        caclulate();
    }
};

int main(){
    
    batsman b;
    b.input();
    b.show();

    return 0;
}