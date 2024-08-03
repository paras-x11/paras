// We want to store the information of different vehicles. Create a class named Vehicle with two data member named mileage and price.

// Create its two subclasses:
// *Car with data members to store ownership cost, warranty (by years), seating capacity and fuel type (diesel or petrol).
// *Bike with data members to store the A number of cylinders, number of gears, cooling type(air, liquid or oil), wheel type(alloys or spokes) 
// and fuel tank size(in inches) 

// Make another two subclasses Audi and Ford of Car, each having a data member to store the model type. 
// Make two subclasses Bajaj and TVS, each having a data member to store the make-type.

// Now, store and print the information of an Audi and a Ford car (i.e. model type, ownership cost, warranty, seating capacity, fuel type, mileage and price.) 
// Do the same for a Bajaj and a TVS bike

#include <iostream>
using namespace std;

class Vehicle{
    public:
    int mileage, price;

    public:
    void basic_input(){
        cout << "\n\nEnter Mileage: ";
        cin >> mileage;

        cout << "Enter price: ";
        cin >> price;
    }

    void basic_display(){
        cout << "\nMileage is: " << mileage << endl;
        cout << "Price is: " << price << endl;
    }
};

class Car : public Vehicle{
    public:
    int ownership_cost, warranty, seats;
    string fuel;

    public:
    void car_input(){

        basic_input();
        cout << "Enter ownership cost: ";
        cin >> ownership_cost;

        cout << "Enter warranty(in yeras): ";
        cin >> warranty;

        cout << "Enter seating capacity: ";
        cin >> seats;

        cout << "Enter fuel type(diesel or petrol): ";
        cin.ignore();
        getline(cin, fuel);
    }

    void car_display(){

        basic_display();
        cout << "Ownership cost: " << ownership_cost << endl;

        cout << "Warranty: " << warranty << endl;

        cout << "Seating capacity: " << seats << endl;

        cout << "Fuel type: " << fuel << endl;
   }
};

class Bike : public Vehicle{

    public:
    int cylinders, gears, fuel_tank_size;
    string cooling_type, wheel_type;

    public:
    void bike_input(){

        basic_input();
        cout << "Enter cylinders: ";
        cin >> cylinders;

        cout << "Enter gears: ";
        cin >> gears;

        cout << "Enter cooling type(air, liquid or oil): ";
        cin.ignore();
        getline(cin, cooling_type);

        cout << "Enter wheel type(alloys or spokes): ";
        cin.ignore();
        getline(cin, wheel_type);

        cout << "Enter fuel tank size(in inches): ";
        cin >> fuel_tank_size;
    }

    void bike_display(){

        basic_display();
        cout << "Cylinders: " << cylinders << endl;

        cout << "Gears: " << gears << endl;

        cout << "Cooling type(air, liquid or oil): " << cooling_type << endl;

        cout << "Wheel type(alloys or spokes): " << wheel_type << endl;
        
        cout << "Enter fuel tank size(in inches): " << fuel_tank_size << endl;
    }
};

class Audi : public Car{
    public:
    string audi_model;

    public:
    void input_car_audi(){

        car_input();

        cout << "Enter model type: ";
        getline(cin, audi_model);
    }

    void display_car_audi(){

        car_display();
        
        cout << "Model type: " << audi_model << endl;
    }
};

class Ford : public Car{
    public:
    string ford_model;

    public:
    void input_car_ford(){

        car_input();

        cout << "Enter model type: ";
        getline(cin, ford_model);
    }

    void display_car_ford(){

        car_display();
        
        cout << "Model type: " << ford_model << endl;
    }
};

class Bajaj : public Bike{
    public:
    string bajaj_model;

    public:
    void input_bike_bajaj(){

        bike_input();

        cout << "Enter model type: ";
        getline(cin, bajaj_model);
    }

    void display_bike_bajaj(){

        bike_display();
        
        cout << "Model type: " << bajaj_model << endl;
    }
};

class TVS : public Bike{
    public:
    string tvs_model;

    public:
    void input_bike_tvs(){

        bike_input();

        cout << "Enter model type: ";
        getline(cin, tvs_model);
    }

    void display_bike_tvs(){

        bike_display();
        
        cout << "Model type: " << tvs_model << endl;
    }
};

int main(){
    
    int ch;
    Audi a;
    Ford f;
    Bajaj b;
    TVS t;

    do{
    cout << "\nEnter 1 for CAR AUDI. \t Enter 2 for CAR FORD. " << endl << "Enter 3 for bike BAJAJ. \t Enter 4 for bike TVS. " << endl;
    cout << "Enter your choice: ";
    cin >> ch;

    switch(ch){

    case 1: cout << "\nEnter  details for car Audi: " << endl;

            a.input_car_audi();
            cout << endl;

            cout << "\n------------------------------------------------" << endl;
            cout << "\n-> Details for car Audi: " << endl;

            a.display_car_audi();
            cout << endl;
        break;

    case 2: cout << "\nEnter  details for car Ford: " << endl;

            f.input_car_ford();
            cout << endl;

            cout << "\n------------------------------------------------" << endl;
            cout << "\n-> Details for car Ford: " << endl;

            f.display_car_ford();
            cout << endl;
        break;

    case 3: cout << "\nEnter  details for bike Bajaj: " << endl;

            b.input_bike_bajaj();
            cout << endl;

            cout << "\n------------------------------------------------" << endl;
            cout << "\n-> Details for bike Bajaj: " << endl;

            b.display_bike_bajaj();
            cout << endl;
        break;

    case 4: cout << "\nEnter  details for bike TVS: " << endl;

            t.input_bike_tvs();
            cout << endl;

            cout << "\n------------------------------------------------" << endl;
            cout << "\n-> Details for bike TVS: " << endl;

            t.display_bike_tvs();
            cout << endl;
        break;
    
    case 0: cout << "\n-> Exited.";
        exit(0);
        break;

    default: cout << "\n-> Enter Valid Choice(1 to 4)." << endl;
        break;   
    }
    }while(ch != 0);
    return 0;
}