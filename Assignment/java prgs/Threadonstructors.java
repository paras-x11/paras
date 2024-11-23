class myRunnable1 implements Runnable{
    myRunnable1(runnable r, String name){
        super();                                                            // ??
    }

    public void run(){
        System.out.println("i am runnable");
    }
}

class myThread1 extends Thread {
    
    myThread1(String name){
        super(name);
    }

    myThread1(ThreadGroup g, String name){              // ?? thread group ??
        super(g, name);
    }

    public void run(){
        System.out.println("Thank You!");
    }
}




public class Threadonstructors {
    public static void main(String[] args) {
        myThread1 t1 = new myThread1("paras");
        myThread1 t2 = new myThread1("second");

        myRunnable1 r1 = new myRunnable1(null, "runnable bhai");
        Thread t3 = new Thread(r1);

        myThread1 t4 = new myThread1(null, "fourth");

        t1.start();
        t2.start();
        t3.start();
        t4.start();

        System.out.println("t1 id: " + t1.threadId());
        System.out.println("t1 name: " + t1.getName());

        System.out.println("t2 id: " + t2.threadId());
        System.out.println("t2 name: " + t2.getName());
    
        System.out.println("t3 id: " + t3.threadId());
        System.out.println("t3 name: " + t3.getName());
    
        System.out.println("t4 id: " + t4.threadId());
        System.out.println("t4 name: " + t4.getName());
    
    }   
}
