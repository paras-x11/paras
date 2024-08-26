class Animal {
    void sound() {
        System.out.println("The animal makes a sound");
    }
}

class Dog extends Animal {
    @Override
    void sound() {
        System.out.println("The dog barks");
    }
}

public class method_overriding {
    public static void main(String[] args) {
        Animal myDog = new Animal();
        myDog.sound();  // Outputs: "The dog barks"
    }
}


// Yes, in Java, when a method is overridden, only one version of the method is executed during runtime, and that is the version of the method 
// in the subclass if the object is an instance of the subclass.

// To execute both the sound() method from the Animal class and the sound() method from the Dog class, you can modify the Dog class to
// explicitly call the sound() method of the Animal class using the super keyword.

// class Dog extends Animal {
//     @Override
//     void sound() {
//         // Call the Animal's sound method through a new Animal instance
//         new Animal().sound();  // Outputs: "The animal makes a sound"
//         System.out.println("The dog barks");
//     }
// }


// method overriding means same method in diff scopes and overloading means same name but diff parameter in same scope 