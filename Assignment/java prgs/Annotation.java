import java.time.LocalTime;

@FunctionalInterface                // we cant add more than one method in interface if this annotation is given
interface InnerAnnotation {
    void method1();
    // void method2();
}

class Super_Phone{
    void showTime(){
        System.out.println("I am in super class.");
    }
}

class Child_Phone extends Super_Phone{
    @Override                       // this annotation gives error if method is not over ridden.
    void showTime(){
        LocalTime t = LocalTime.now().withNano(0);
        System.out.println("I am in base class. " + t);
    }

    @Deprecated                     // this annotation give warning while using deprecated methods
    int sum(int a, int b){
        return a+b;
    }
}


public class Annotation {
    public static void main(String[] args) {
        
        Child_Phone p = new Child_Phone();

        p.showTime();
        System.out.println(p.sum(1, 50));

    }
}
