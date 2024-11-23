// interface
// in english: A point where two System meets and interact.
// in java: A group of related methods with empty bodies.

interface bicycle{
    int n = 45;                             // you can create properties in interface. they are 'final' by defualt
    
    void applyBrake(int decrement);
    void speedUp(int increment); 
    
    // all methods of interface is by default abstract.
    // but in abstract class we use abstract keyword for making method abstract.
    // we can,t write body of any method in interface.
}

interface horn{
    int x = 45;

    void horn1();
    void horn2();
}

class AvonCycle implements bicycle, horn{
    int x = 5;

    public void blowHorn(){
        System.out.println("Trin.. Trin.. ");
    }

    public void applyBrake(int decrement){
        System.out.println("Applying Brake... ");
    }

    public void speedUp(int increment){
        System.out.println("Increasing Speed... ");
    }

    public void horn1(){
        System.out.println("Peep Peep... ");
    }

    public void horn2(){
        System.out.println("Poo Poo... ");
    }
}


public class interfaces {

    @SuppressWarnings("static-access")
    public static void main(String[] args) {
        
        AvonCycle a = new AvonCycle();

        a.applyBrake(1);
        // you can create properties in interface
        System.out.println(a.n);
        
        // you can't modify properties of interfaces as they are final
        // a.n = 5252;
        // System.out.println(a.n);

        // you can't modify properties of interfaces here as they are final but u can overide them in class.
        System.out.println(a.x);

        a.blowHorn();
        a.horn1();
        a.horn2();


    }
}
