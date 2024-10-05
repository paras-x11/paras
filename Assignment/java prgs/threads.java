class Thread1 extends Thread{                       // cooking:

    @Override
    public void run(){
        int i = 0;

        while(i < 20){
            System.out.println("My Cooking Thread 1 Is Running");
            System.out.println("I Am Happy!");
            i++;
        }
    }
}

class Thread2 extends Thread{                       // chatting:

    @Override
    public void run(){
        int i = 0;

        while(i < 20){
            System.out.println("Thread 2 for Chatting.");
            System.out.println("I Am Sad!");
            i++;
        }
    }
}

class Thread3 extends Thread{                       // coding:

    @Override
    public void run(){
        int i = 0;

        while(i < 20){
            System.out.println("Thread 3 Running For Coding.");
            System.out.println("Eat Sleep Code!");
            i++;
        }
    }
}

public class threads {
    public static void main(String[] args) {
        Thread1 t1 = new Thread1();
        Thread2 t2 = new Thread2();
        Thread3 t3 = new Thread3();

        t1.start();
        t2.start();
        t3.start();

        System.out.println(t1.threadId());
        System.out.println(t2.threadId());
        System.out.println(t3.threadId());

    }
}