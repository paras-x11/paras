class Phone {
    void showtime() {
        System.out.println("Time...");
    }
    void on(){
        System.out.println("Turning On Phone...");
    }
}

class SmartPhone extends Phone {
    void music() {
        System.out.println("playing music...");
    }
    void on(){
        // super.on();
        System.out.println("Turning On Smart Phone...");
    }
}

public class DynamicMethodDispatch {
    public static void main(String[] args) {
        // SmartPhone obj = new Phone();        //Not Allowed

        Phone p = new Phone();
        p.showtime();
        p.on();
        // p.music();

        Phone obj = new SmartPhone();
        System.out.println();
        obj.showtime();
        obj.on();
        // obj.music();

        SmartPhone obj2 = new SmartPhone();
        System.out.println();
        obj2.on();
        obj2.music(); 
        obj2.showtime();
    }
}

// Dynamic Method Dispatch:

// super -> method1
//          method2     ...(i)

// sub   -> method2     ...(ii)  (overridden) 
//          method3

// scenerio 1: super obj = new sub()
//             obj.method2()       -> (ii) is called(method of object)
//             obj.method3()       -> not allowed

// scenerio 2: sub obj = new super()       -> Not Allowed


// super obj = new sub();

// yaha, super class ka refrence ban raha he, aur sub class ka object ban raha he..
// super class ke refrence se sub class ka object ban sakta hai, par
// sub class ke refrence se super class ka object nahi ban sakta.
// sub obj = new super()       -> Not Allowed