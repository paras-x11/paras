
class myThread2 extends Thread {
    
    myThread2(String name){
        super(name);
    }

    public void run(){
        // int i = 0;
        while (true) { //(i < 200) {
            System.out.println("Thank You! " + this.getName());
            // i++;
        }
    }
}

public class ThreadPriorities {
    public static void main(String[] args) {
        myThread2 t1 = new myThread2("Paras-1");
        myThread2 t2 = new myThread2("Paras-2");
        myThread2 t3 = new myThread2("Paras-3");
        myThread2 t4 = new myThread2("Paras-4");
        myThread2 t5 = new myThread2("Paras-5 {Most Important}");


        t1.start();
        t2.start();
        t3.start();
        t4.start();
        t5.start();

        t5.setPriority(Thread.MAX_PRIORITY);

        t5.setPriority(Thread.MIN_PRIORITY);
        t5.setPriority(Thread.MIN_PRIORITY);
        
        t5.setPriority(Thread.NORM_PRIORITY);
        t5.setPriority(Thread.NORM_PRIORITY);

        // System.out.println("t1 id: " + t1.threadId());
        // System.out.println("t1 name: " + t1.getName());

        // System.out.println("t2 id: " + t2.threadId());
        // System.out.println("t2 name: " + t2.getName());
    
        // System.out.println("t3 id: " + t3.threadId());
        // System.out.println("t3 name: " + t3.getName());
    
        // System.out.println("t4 id: " + t4.threadId());
        // System.out.println("t4 name: " + t4.getName());

        // System.out.println("t5 id: " + t5.threadId());
        // System.out.println("t5 name: " + t5.getName());
    
    }   
}
