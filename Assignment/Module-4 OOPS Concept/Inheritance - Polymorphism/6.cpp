#include <iostream>
using namespace std;

// Base class
class Base {
private:
    int privateVar = 1;
protected:
    int protectedVar = 2;
public:
    int publicVar = 3;


    // Public function to access private variable
    int getPrivate() {
        return privateVar;
    }

    // Public function to access protected variable
    int getProtected() {
        return protectedVar;
    }

    // Public function to access public variable
    int getPublic() {
        return publicVar;
    }
};

// Derived class with private inheritance
class DerivedPrivate : private Base {
public:
    void display() {
        // Error: Can't access private or protected members directly
        // cout << "Private member in DerivedPrivate: " << privateVar << endl;
        // cout << "Protected member in DerivedPrivate: " << protectedVar << endl;

        // Accessing public member
        cout << "Public member in DerivedPrivate: " << publicVar << endl;
    }
};

// Derived class with protected inheritance
class DerivedProtected : protected Base {
public:
    void display() {
        // Error: Can't access private members directly
        // cout << "Private member in DerivedProtected: " << privateVar << endl;

        // Accessing protected member
        cout << "Protected member in DerivedProtected: " << protectedVar << endl;

        // Accessing public member
        cout << "Public member in DerivedProtected: " << publicVar << endl;
    }
};

// Derived class with public inheritance
class DerivedPublic : public Base {
public:
    void display() {
        // Error: Can't access private members directly
        // cout << "Private member in DerivedPublic: " << privateVar << endl;

        // Accessing protected member
        cout << "Protected member in DerivedPublic: " << protectedVar << endl;

        // Accessing public member
        cout << "Public member in DerivedPublic: " << publicVar << endl;
    }
};

int main() {
    DerivedPrivate derivedPrivate;
    cout << "Access from DerivedPrivate:" << endl;
    derivedPrivate.display();
    cout << endl;

    DerivedProtected derivedProtected;
    cout << "Access from DerivedProtected:" << endl;
    derivedProtected.display();
    cout << endl;

    DerivedPublic derivedPublic;
    cout << "Access from DerivedPublic:" << endl;
    derivedPublic.display();

    return 0;
}
