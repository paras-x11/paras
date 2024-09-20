
class parent1 {

    public
    int x;

    parent1(){
        System.out.println("i am parent class default constructor.");
        System.out.println();
    }

    parent1(int x){
        System.out.println("i am parent class one parameter constructor with value of x: " + x);
        System.out.println();
    }

    parent1(int x, int y){
        System.out.println("i am parent class two parameter constructor with value of x: " + x);
        System.out.println();
    }
}

class child_1 extends parent1 {
    public 
    int y;

    child_1(){
        System.out.println("i am child1 class default constructor.");
        System.out.println();
    }

    child_1(int x){
        // super(x. y);
        // You can't directly call a more-parameter constructor from a less-parameter constructor in the superclass because the required parameters would be missing. 
        // You need to either provide default values or structure your constructors to handle different cases properly.
        
        // super(x, 20);
        super(x);
        System.out.println("i am child1 class one parameter constructor ");
        System.out.println();
    }

    child_1(int x, int y){
        super(x, y);
        System.out.println("i am child1 class two parameter constructor with value of y: " + y);
        System.out.println();
    }
}

class child_2 extends child_1 {
    public
    int z;

    child_2(){
        System.out.println("i am child2 class default constructor.");
        System.out.println();
    }

    child_2(int x){
        super(x, 20);
        System.out.println("i am child2 class one parameter constructor.");
        System.out.println();

    }

    child_2(int x, int y){
        super(x, y);
        System.out.println("i am child1 class two parameter constructor");
        System.out.println();
    }

    child_2(int x, int y, int z){
        super(x, y);
        System.out.println("i am child2 class three parameter constructor with value of z: "+ z);
        System.out.println();
    }
}


public class ConstructerInheritance {
    @SuppressWarnings("unused")
    public static void main(String[] args) {
        // parent1 p = new parent1();

        // child_1 c1 = new child_1();
        
        // child_2 c2 = new child_2();

        // child_1 c1 = new child_1(10, 20);

        // child_2 c2 = new child_2(10, 20, 30);

        // child_2 c2 = new child_2(10, 20);

        // child_1 c1 = new child_1(10);

        child_2 c2 = new child_2(10);





    }
}
