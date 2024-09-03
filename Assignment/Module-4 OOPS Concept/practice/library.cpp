#include <iostream>
using namespace std;

class Library{
    public:
    int no_of_books = 0;
    string books[100];

    public:

    void addBook(string book){
        this->books[no_of_books] = book;
        no_of_books++;
        cout << "-> " + book + " has been added.\n";
    }

    void showBook(){
        for (int i = 0; i < no_of_books; i++)
        {
            cout << books[i] << "\n";   
        }
    }
};

int main(){
    
    Library l;

    l.addBook("Hello");
    l.addBook("World");

    l.showBook();
    

    return 0;
}

//switch case