#include <iostream>
using namespace std;

class Personal_Info{
    public:
    string name;

    public:
    void setName(){
        cout << "Enter Your Name: ";
        cin >> name;
    }

    string getName(){
        return name;
    }
};

class Menu : public Personal_Info{
    public:
    int total_amount;

    public:
    void showMenu(){
        cout << "\n\n1) Pizzas\n";
        cout << "2) Burgers\n";
        cout << "3) Sandwich\n";
        cout << "4) Rolls\n";
        cout << "5) Biriyani\n";
    }

    void showItem(int outer_selection){
        if(outer_selection == 1){
            cout << "\n1) Alfredo smoke pizza            Rs.500";
            cout << "\n2) Fettuccini lasanga pizza       Rs.200";
            cout << "\n3) Wild mushroom meltique pizza   Rs.100";
        }

        else if (outer_selection == 2){
            cout << "\n1) Cheese burger            Rs.80";
            cout << "\n2) Crunchy VEG burger       Rs.100";
            cout << "\n3) Aloo Bechara burger      Rs.120";
        }

        else if (outer_selection == 3){
            cout << "\n1) Cheese Sandwich            Rs.50";
            cout << "\n2) Crunchy VEG sandwich       Rs.80";
            cout << "\n3) Aloo Bechara sandwich      Rs.120";
        }
        
        else if (outer_selection == 4){
            cout << "\n1) Cheese rolls            Rs.25";
            cout << "\n2) Crunchy VEG rolls       Rs.50";
            cout << "\n3) Aloo Bechara rolls      Rs.75";
        }
        
        else if (outer_selection == 5){
            cout << "\n1) Cheese biriyani            Rs.120";
            cout << "\n2) Crunchy VEG biriyani       Rs.150";
            cout << "\n3) Aloo Bechara biriyani      Rs.220";
        }

        else{   cout << "\n-> No Item"; }
        
    }

    void showItemSelection(int ch, int selection){

        if(ch == 1 ){
            if(selection == 1){ cout << "\n-> Alfredo smoke pizza.\n";  }

            else if (selection == 2){   cout << "\n-> Fettuccini lasanga pizza.\n"; }

            else if (selection == 3){   cout << "\n-> Wild mushroom meltique pizza.\n"; }
        }
        
        else if(ch == 2 ){
            if(selection == 1){    cout << "\n-> Cheese burger.\n";    }

            else if (selection == 2){   cout << "\n-> Crunchy VEG burger.\n";    }

            else if (selection == 3){   cout << "\n-> Aloo Bechara burger.\n";    }
        }

        else if(ch == 3 ){
            if(selection == 1){    cout << "\n-> Cheese sandwich.\n";    }

            else if (selection == 2){   cout << "\n-> Crunchy VEG sandwich.\n";    }

            else if (selection == 3){   cout << "\n-> Aloo Bechara sandwich.\n";    }
        }

        else if(ch == 4 ){
            if(selection == 1){    cout << "\n-> Cheese rolls.\n";    }

            else if (selection == 2){   cout << "\n-> Crunchy VEG rolls.\n";    }

            else if (selection == 3){   cout << "\n-> Aloo Bechara rolls.\n";    }
        }

        else if(ch == 5 ){
            if(selection == 1){    cout << "\n-> Cheese biriyani.\n";    }

            else if (selection == 2){   cout << "\n-> Crunchy VEG biriyani.\n";    }

            else if (selection == 3){   cout << "\n-> Aloo Bechara biriyani.\n";    }
        }
        
        else{   cout << "\n-> No Item"; }

    }

    int calculateBill(int ch, int selection, int q){

        if(ch == 1 ){
            if(selection == 1){    total_amount = 500 * q;    }
            else if (selection == 2){    total_amount = 200 * q;    }
            else if (selection == 3){    total_amount = 100 * q;    } 
            else{   cout << "\n-> No Item"; }
            return total_amount; 
        }
        
        else if(ch == 2 ){
            if(selection == 1){    total_amount = 80 * q;    }
            else if (selection == 2){    total_amount = 100 * q;    }
            else if (selection == 3){    total_amount = 120 * q;    } 
            else{   cout << "\n-> No Item"; }
            return total_amount;
        }

        else if(ch == 3 ){
            if(selection == 1){    total_amount = 50 * q;    }
            else if (selection == 2){    total_amount = 80 * q;    }
            else if (selection == 3){    total_amount = 120 * q;    } 
            else{   cout << "\n-> No Item"; }
            return total_amount;
        }

        else if(ch == 4 ){
            if(selection == 1){    total_amount = 25 * q;    }
            else if (selection == 2){    total_amount = 50 * q;    }
            else if (selection == 3){    total_amount = 75 * q;    } 
            else{   cout << "\n-> No Item"; }
            return total_amount;
        }

        else if(ch == 5 ){
            if(selection == 1){    total_amount = 120 * q;    }
            else if (selection == 2){    total_amount = 150 * q;    }
            else if (selection == 3){    total_amount = 220 * q;    } 
            else{   cout << "\n-> No Item"; }
            return total_amount;
        }
        
        else{   cout << "\n-> No Item"; }
    }

    void showMessage(){
        cout << "\n-> Amare Tya Avva Badal Tamaro Aabhar...";
    }
};


int main(){

    char choice;
    int ch, inner_ch, q;

    Menu m;

    do{
        m.setName();
        cout << "-> Hello, " << m.getName();

        cout << "\n\nWhat would you like to order: ";
        cout << "\n\n-------------------------- Menu --------------------------";
        m.showMenu();

        cout << "\nPlease enter your choice: ";
        cin >> ch;

        switch (ch)
        {
            case 1: m.showItem(ch);
                    cout << "\n\nPlease enter which pizza you would like to have: ";
                    cin >> inner_ch;

                    cout << "\n-> You have selected ";
                    m.showItemSelection(ch, inner_ch);
                    
                    switch (inner_ch)
                    {
                        case 1: cout << "\nPlease Enter Quantity: ";
                                cin >> q;

                                m.showItemSelection(ch, inner_ch);

                                cout << "Your Total Bill Is: " << m.calculateBill(ch, inner_ch, q);                        
                            break;

                        case 2: cout << "\nPlease Enter Quantity: ";
                                cin >> q;

                                m.showItemSelection(ch, inner_ch);

                                cout << "Your Total Bill Is: " << m.calculateBill(ch, inner_ch, q);                        
                            break;

                        case 3: cout << "\nPlease Enter Quantity: ";
                                cin >> q;

                                m.showItemSelection(ch, inner_ch);

                                cout << "Your Total Bill Is: " << m.calculateBill(ch, inner_ch, q);                        
                            break;
                        
                        default: cout << "\n-> Inavlid choice.";
                            break;
                    }
                break;

                 case 2: m.showItem(ch);
                    cout << "\n\nPlease enter which burgers you would like to have: ";
                    cin >> inner_ch;

                    cout << "\n-> You have selected ";
                    m.showItemSelection(ch, inner_ch);
                    
                    switch (inner_ch)
                    {
                        case 1: cout << "\nPlease Enter Quantity: ";
                                cin >> q;

                                m.showItemSelection(ch, inner_ch);

                                cout << "Your Total Bill Is: " << m.calculateBill(ch, inner_ch, q);                        
                            break;

                        case 2: cout << "\nPlease Enter Quantity: ";
                                cin >> q;

                                m.showItemSelection(ch, inner_ch);

                                cout << "Your Total Bill Is: " << m.calculateBill(ch, inner_ch, q);                        
                            break;

                        case 3: cout << "\nPlease Enter Quantity: ";
                                cin >> q;

                                m.showItemSelection(ch, inner_ch);

                                cout << "Your Total Bill Is: " << m.calculateBill(ch, inner_ch, q);                        
                            break;
                        
                        default: cout << "\n-> Inavlid choice.";
                            break;
                    }
                break;

                 case 3: m.showItem(ch);
                    cout << "\n\nPlease enter which sandwich you would like to have: ";
                    cin >> inner_ch;

                    cout << "\n-> You have selected ";
                    m.showItemSelection(ch, inner_ch);
                    
                    switch (inner_ch)
                    {
                        case 1: cout << "\nPlease Enter Quantity: ";
                                cin >> q;

                                m.showItemSelection(ch, inner_ch);

                                cout << "Your Total Bill Is: " << m.calculateBill(ch, inner_ch, q);                        
                            break;

                        case 2: cout << "\nPlease Enter Quantity: ";
                                cin >> q;

                                m.showItemSelection(ch, inner_ch);

                                cout << "Your Total Bill Is: " << m.calculateBill(ch, inner_ch, q);                        
                            break;

                        case 3: cout << "\nPlease Enter Quantity: ";
                                cin >> q;

                                m.showItemSelection(ch, inner_ch);

                                cout << "Your Total Bill Is: " << m.calculateBill(ch, inner_ch, q);                        
                            break;
                        
                        default: cout << "\n-> Inavlid choice.";
                            break;
                    }
                break;

             case 4: m.showItem(ch);
                    cout << "\n\nPlease enter which rolls you would like to have: ";
                    cin >> inner_ch;

                    cout << "\n-> You have selected ";
                    m.showItemSelection(ch, inner_ch);
                    
                    switch (inner_ch)
                    {
                        case 1: cout << "\nPlease Enter Quantity: ";
                                cin >> q;

                                m.showItemSelection(ch, inner_ch);

                                cout << "Your Total Bill Is: " << m.calculateBill(ch, inner_ch, q);                        
                            break;

                        case 2: cout << "\nPlease Enter Quantity: ";
                                cin >> q;

                                m.showItemSelection(ch, inner_ch);

                                cout << "Your Total Bill Is: " << m.calculateBill(ch, inner_ch, q);                        
                            break;

                        case 3: cout << "\nPlease Enter Quantity: ";
                                cin >> q;

                                m.showItemSelection(ch, inner_ch);

                                cout << "Your Total Bill Is: " << m.calculateBill(ch, inner_ch, q);                        
                            break;
                        
                        default: cout << "\n-> Inavlid choice.";
                            break;
                    }
                break;

                 case 5: m.showItem(ch);
                    cout << "\n\nPlease enter which biriyani you would like to have: ";
                    cin >> inner_ch;

                    cout << "\n-> You have selected ";
                    m.showItemSelection(ch, inner_ch);
                    
                    switch (inner_ch)
                    {
                        case 1: cout << "\nPlease Enter Quantity: ";
                                cin >> q;

                                m.showItemSelection(ch, inner_ch);

                                cout << "Your Total Bill Is: " << m.calculateBill(ch, inner_ch, q);                        
                            break;

                        case 2: cout << "\nPlease Enter Quantity: ";
                                cin >> q;

                                m.showItemSelection(ch, inner_ch);

                                cout << "Your Total Bill Is: " << m.calculateBill(ch, inner_ch, q);                        
                            break;

                        case 3: cout << "\nPlease Enter Quantity: ";
                                cin >> q;

                                m.showItemSelection(ch, inner_ch);

                                cout << "Your Total Bill Is: " << m.calculateBill(ch, inner_ch, q);                        
                            break;
                        
                        default: cout << "\n-> Inavlid choice.";
                            break;
                    }
                break;
            
            default: cout << "\n-> Invalid Choice.";
                break;
        }

        m.showMessage();

        cout << "\n\n-> Would you like to order anything else(y / n): ";
        cin >> choice;

    } while(choice =='y' || choice == 'Y');

    return 0;
}