class NegativeRadiusException extends Exception{
    @Override
    public String toString() {
        return "Radius cannot be negative.";
    }

    @Override
    public String getMessage() {
        return "Enter valid radius";
    }
}


public class Throw_Throws {

    // we can include throws keyword with methods & when we call this type of method we need to handle the exception with try catch block in main method.

    public static int divide(int a, int b) throws ArithmeticException{              // in-built Exception
        return a/b;
    }

    public static double area(int r) throws NegativeRadiusException{                // custom Exception
        if(r < 0){
            throw new NegativeRadiusException();                                    // throw is uded for making object of exception.
        }
        return Math.PI * r * r;
    }

    public static int sum(int a, int b, int c){
        return a+b+c;
    }

    public static void main(String[] args) {

        try {
            System.out.println(divide(20, 0));              // handling method bcoz this method throws exception.
        } 
        catch (Exception e) {
            System.out.println("Exception: " + e.getMessage());    
        }

        System.out.println(sum(10, 20, 30));              // no need to handle bcoz this method doesn't throws exception.

        try {
            System.out.println(area(-5));                       // handling method bcoz this method throws exception.
        } 
        catch (Exception e) {
            System.out.println("Exception: " + e.toString());
        }


    }

    
}
