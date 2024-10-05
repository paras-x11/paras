interface AnonymousInterface {
    void Method1();
    void Method2();
}
    
class Anonymous_class implements AnonymousInterface{

    public void display(){
        System.out.println("Hello.");
    }

    @Override
    public void Method1(){
        System.out.println("I am method 1");
    }

    @Override
    public void Method2(){
        System.out.println("I am method 2");
    }
}

@FunctionalInterface                            // functional interface have only one method
interface lambdaInterface{
    void OneMethod(String greet, String name);
}

class lambda_class implements lambdaInterface{
    @Override
    public void OneMethod(String greet, String name){
        System.out.println("I am Method in Lambda class.");
        System.out.println(greet + ", " + name);
    }
}

public class Lambda_Expression{
    public static void main(String[] args) {

        // // -> normal rite:
        // Anonymous_class a = new Anonymous_class();
        // a.Method1();   

        // // -> interface ni method direct calling using anonymous class:
        AnonymousInterface ai = new AnonymousInterface() {
            @Override
            public void Method1(){
                System.out.println("I am method 1");
            }

            @Override
            public void Method2(){
                System.out.println("I am method 2");
            }
        };

        ai.Method1();
        ai.Method2();

        // // dynamic method dispatch
        // lambdaInterface li = new lambda_class();
        // li.OneMethod();

        // // lambda expression: lambda works only with functional interface
        // // functional interface mate alag class bnavani jarur nthi, direk:
        lambdaInterface l = (greet, name) -> {
            System.out.println(greet + ", " + name);
        };

        l.OneMethod("Good morning", "Paras !");


    }
}