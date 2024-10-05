public class Finally {
    public static int divide1(){
        try {
            int a = 50;
            int b = 0;                          // change the value
            int c = a/b;
            return c;
        } 
        
        catch (Exception e) {
            System.out.println(e);
        }

        // further statement does not execute when no exception is detected so it returns c end exit function.
        // but finally block will execute when no exception is detected.

        finally{
            System.out.println("Cleaning up resources.... End Of Function");
        }

        return -1;
    }

    public static void main(String[] args) {
        System.out.println(divide1());

        int x = 60;
        int y = 6;

        while (true) {
            try {
                System.out.println(x / y);
            }
            
            catch (Exception e) {
                System.out.println(e);
                break;                          // break will directly exit the loop but finally block is executed..
            }

            finally{
                System.out.println("I am finally. value of y = " + y);
            }
            y--;
        }

        // int g = 20-10;
        // System.out.println(g);
    }
    
}
