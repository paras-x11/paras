// C ++ Programming Assessment Test 
 
// • Create a Project to demonstrate an Event Organiser Project which will help to manage the Events. The Project should contain all the necessary
//   requirements i.e  need to use conditional Statements, Loops, Function and also A Program should use  the concept of OOP. 
// • Give comments where it is required , for better understanding of codes. It will help you and the project evaluator. 
// • A Project should contain the following execution flow. 
// • When Execution of the main source file, the program should first ask the NAME OF THE EVENT. 
 
// 1. Example : Wedding 
 
// 2. After asking the event name , it should ask your  
// I. FIRST NAME,LAST NAME. 
// II. Number of Guests. 
// III. Number of Minutes. 
 
// 3. Once the all the Input requirement is over, you should be able to get the Event Cost Estimation. 
// Use the following rate card : 
// a. const double CostPerHour = 18.50; 
// b. const double CostPerMinute = .40; 
// c. const double CostOfDinner = 20.70; 
 
// i). GET Number of Servers. 
// (1 Server can handle 20 guests, so FIND how much server required for No. of Guests you Entered.) (use ceil() func. rounds up the nearest integer) 
 
// ii). GET COST of ONE Server. 
// Example :  
 
// Cost1 = (NumberOfMinutes / 60) * CostPerHour; 
// Cost2 = (NumberOfMinutes % 60) * CostPerMinute; 
// CostForOneServer = Cost1 + Cost2; 
 
// iii). GET COST for FOOD.  
// TotalFoodCost = NumberOfGuests * CostOfDinner; 
 
// iv). Get Average Cost Per Person 
// AverageCost = TotalFoodCost / NumberOfGuests; 
 
// v). GET TOTAL COST. 
// TotalCost = TotalFoodCost + (CostForOneServer * NumberOfServers); 
  
// vi). GET DEPOSIT AMOUNT 
// DepositAmount = TotalCost * .25; 


#include <iostream>
#include <cmath>
using namespace std;

class Event{

    protected:
    string event, name;
    int g_no, minutes;

    public:
    Event(){
        cout << "\nEnter the name of event: ";
        getline(cin, event);

        cout << "\nEnter the customer's first and last name: ";
        getline(cin ,name);

        cout << "\nEnter the number of guests: ";
        cin >> g_no;

        cout << "\nEnter the number of minutes in event: ";
        cin >> minutes;
    }

    string get_name(){
        return name;
    }

    void show(){
        cout << "\nYour Event: " << event << endl;
        cout << "Event Organizer: " << name << endl;
    }
};

class Cost : public Event{

    protected: 

    int cost1, cost2;
    double d_amt;

    const double CostPerHour = 18.50; 
    const double CostPerMinute = .40; 
    const double CostOfDinner = 20.70;

    public:

    double calculate_servent(){
        
        return ceil(g_no / 20);
    }

    double servent_cost(){

        cost1 = (minutes / 60) * CostPerHour; 
        cost2 = (minutes % 60) * CostPerMinute; 

        return ceil(cost1 + cost2);                   // One Servent Cost
    }

    double total_servent_cost(){

        return ceil(servent_cost() * calculate_servent());                    // Total Servent Cost
    }

    double food_cost(){

        return ceil(g_no * CostOfDinner);
    }

    double total_cost(){

        return ceil(total_servent_cost() + food_cost());
    }

    double deposit(){

        return ceil(total_cost() * 0.25);
    }

    void display(){

        show();

        cout << "\nNumber of required servent is: " << calculate_servent() << endl;

        cout << "\nThe cost of one servent is: " << servent_cost() << endl;
        cout << "\nThe cost of all servent is: " << total_servent_cost() << endl;

        cout << "\nThe total food cost is: " << food_cost() << endl;

        cout << "\n-> Total Event Cost is: " << total_cost() << endl;

        cout << "\n\nPlease deposit a 25\% deposit to reserve the event." << endl;
        cout << "\n-> The Deposit Needed is: " << deposit() << endl << endl;
    }
};

int main(){

    cout << "\n************************* Event Management System *************************" << endl;
    
    Cost c;

    cout << "\n\n************************* Event Estimate for: " << c.get_name() << " *************************" << endl;
    
    c.display();

    return 0;
} 


