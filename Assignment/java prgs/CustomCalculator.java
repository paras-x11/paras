// Exercise: You have to create a custom calculator with following operations:
// 1. + -> Addition
// 2. - -> Subtraction
// 3. * -> Multiplication
// 4. / -> Division

// Which throws the following exceptions:
// 1. Invalid input ex. 8 & 9
// 2. Cannot  divide by 0 Exception
// 3. Max Input Exception if any of the inputs is greater than 100000
// 4. Max multiplier reached exception - dont allow any multiplication input greater than 7000

import java.util.Scanner;

class InvalidInputException extends Exception{
    @Override
    public String toString() {
        return "Can not add 8 & 9";
    }
}

class CannotDivideByZeroException extends Exception{
    @Override
    public String toString() {
        return "Can not divide by zero.";
    }
}


class MaxInputExceptionException extends Exception{
    @Override
    public String toString() {
        return "input cannot begreater than 100000.";
    }
}

class MaxMultiplierReachedException extends Exception{
    @Override
    public String toString() {
        return "max multiplier is 7000.";
    }
}
class CustomCalc{
    public double add(int a, int b) throws InvalidInputException, MaxInputExceptionException{
        if(a > 100000 || b > 100000){
            throw new MaxInputExceptionException();
        }
        if(a==8 || b==9){
            throw new InvalidInputException();
        }
        return a+b;
    }

    public double subtraction(int a, int b) throws InvalidInputException, MaxInputExceptionException{
        if(a > 100000 || b > 100000){
            throw new MaxInputExceptionException();
        }
        return a-b;
    }
    
    public double multiply(int a, int b) throws InvalidInputException, MaxInputExceptionException, MaxMultiplierReachedException{
        if(a > 100000 || b > 100000){
            throw new MaxInputExceptionException();
        }
        if(a > 7000 || b > 7000){
            throw new MaxMultiplierReachedException();
        }
        return a*b;
    }
    
    public double division(int a, int b) throws CannotDivideByZeroException, MaxInputExceptionException{
        if(a > 100000 || b > 100000){
            throw new MaxInputExceptionException();
        }
        if(a==0 || b==0){
            throw new CannotDivideByZeroException();
        }
        return a/b;
    }

}

class input{
    int a, b;

    Scanner sc = new Scanner(System.in);

    public void Enter(){
        System.out.printf("Enter A: ");
        this.a = sc.nextInt();

        System.out.printf("Enter B: ");
        this.b = sc.nextInt();
    }

    public int getA(){
        return this.a;
    }
    
    public int getB(){
        return this.b;
    }
}

public class CustomCalculator {
    public static void main(String[] args) throws InvalidInputException, CannotDivideByZeroException, MaxInputExceptionException, MaxMultiplierReachedException{
        
        @SuppressWarnings("resource")
        Scanner sc = new Scanner(System.in);
        
        CustomCalc c = new CustomCalc();
        
        input i = new input();

        int ch = 1;

        while(ch!=0){
            try{
                System.out.println("\nEnter 1 for +\nEnter 2 for -\nEnter 3 for *\nEnter 4 for /\n");
                System.out.print("\nEnter your choice: ");
                ch = sc.nextInt();

                switch (ch) {
                    case 1: i.Enter();
                            System.out.println(c.add(i.getA(), i.getB()));
                        break;
                    
                    case 2: i.Enter();
                            System.out.println(c.subtraction(i.getA(), i.getB()));
                        break;
                    
                    case 3: i.Enter();
                            System.out.println(c.multiply(i.getA(), i.getB()));
                        break;

                    case 4: i.Enter();
                            System.out.println(c.division(i.getA(), i.getB())); 
                        break;
                        
                    case 0: System.out.println("Exited");
                        break;

                    default: System.out.println("Invalid Choice.");
                        break;
                }
            }
            catch(Exception e){
                System.out.println("Error: "+ e);
            }
        }        
    }
}
