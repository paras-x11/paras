abstract class parent{
    public parent(){
        System.out.println("i am the constructor of parent class.");
    }

    public void sayHello(){
        System.out.println("Hello... ");
    }

    abstract public void greet();           

    abstract public void name();

    // abstract method: A method that is declared without implementation.

    // jyare koi method abstract hoy tyare class pn cumpulsory abstract j hoy.
    // abstract means: existing in thoughts or idea without concrete existence (khayali pulav).
    // that's why we can't make object of abstract class.
}

class child1 extends parent{
    // when u inherit the abstract class u must need to override all the abstract method of super class. or u can make this class as abstract class.
    // here i make the didn't make the class abstract so its necessary to over ride all abstract methods of super class. 

    public child1(){
        System.out.println("child1 constructor");
    }

    @Override
    public void greet(){
        System.out.println("Good Morning, ");
    }

    @Override
    public void name(){
        System.out.println("Paras ");
    }
}

abstract class child2 extends parent{
    // here i make the class abstract so its not necessary to over ride all abstract methods of super class.
    
    public void methodOfChild2(){
        System.out.println("method of child2");
    }
}

class child3 extends parent{
    // when u inherit the abstract class u must need to override all the abstract method of super class. or u can make this class as abstract class.
    // here i make the didn't make the class abstract so its necessary to over ride all abstract methods of super class. 

    public child3(){
        System.out.println("child3 constructor");
    }

    @Override
    public void greet(){
        System.out.println("Good Afternoon, ");
    }

    @Override
    public void name(){
        System.out.println("Pavan ");
    }
}


public class abstractClass {
    public static void main(String[] args) {
        
        // parent p = new parent();                 // can't make object of abstrat class

        child1 c1 = new child1();

        c1.sayHello();
        c1.greet();
        c1.name();

        // child_2 c2 = new child2();               // can't make object of abstrat class

        child3 c3 = new child3();

        c3.sayHello();
        c3.greet();
        c3.name();

        // it is possible to create refrence of abstract class. but not object 
        // (left side of = is refrence and right side is the class name jiska ham object banayege)

        parent c4 = new child1();
        c4.name();

    }
}
