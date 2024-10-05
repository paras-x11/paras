class myThreadRunnable1 implements Runnable{
    @Override
    public void run(){
        int i = 0;

        while(i < 20){
            System.out.println("Thread 1");
            System.out.println("Eat!");
            i++;
        }
    }
}

class myThreadRunnable2 implements Runnable{
    @Override
    public void run(){
        int i = 0;

        while(i < 20){
            System.out.println("Thread 2");
            System.out.println("Sleep!");
            i++;
        }
    }
}

class myThreadRunnable3 implements Runnable{
    @Override
    public void run(){
        int i = 0;

        while(i < 20){
            System.out.println("Thread 3");
            System.out.println("Code!");
            i++;
        }
    }
}



public class runnable {
    public static void main(String[] args) {
        
        myThreadRunnable1 bullet1 = new myThreadRunnable1();
        Thread gun1 = new Thread(bullet1); 

        myThreadRunnable2 bullet2 = new myThreadRunnable2();
        Thread gun2= new Thread(bullet2); 

        myThreadRunnable3 bullet3 = new myThreadRunnable3();
        Thread gun3 = new Thread(bullet3); 

        gun1.start();
        gun2.start();
        gun3.start();

        // start method runnable interface me nahi hai is liye thread ka object bana ke usme runnable pass krna pdta hai..
    
    }
}
