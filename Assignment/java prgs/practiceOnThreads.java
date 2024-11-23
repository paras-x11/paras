class th1 extends Thread{
    public void run(){
        // int i = 0;
        while (true) {
            try {
                Thread.sleep(200);
            } 
            catch (InterruptedException e) {
                e.printStackTrace();
            }
            System.out.println("Good Morning!");
            // i++;
        }
    }    
}

class th2 extends Thread{
    public void run(){
        // int i = 0;
        // while (true) {
        //     try {
        //         Thread.sleep(200);
        //     } 
        //     catch (InterruptedException e) {
        //         e.printStackTrace();
        //     }
        //     System.out.println("Welcome!");
        //     // i++;
        // }
    }    
}

public class practiceOnThreads {
    public static void main(String[] args) {
        th1 t1 = new th1();
        th2 t2 = new th2();

        t1.setPriority(6);
        t2.setPriority(9);

        System.out.println("t1 priority: " + t1.getPriority());
        System.out.println("t2 priority: " + t2.getPriority());

        System.out.println("t2 state: " + t2.getState());
        t2.start();
        System.out.println("t2 state: " + t2.getState());

        System.out.println("t2 state: " + Thread.currentThread().getState());

        
        // t1.start();
        // t2.start();
    }   
}
