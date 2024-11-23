
import calc.test_access_modifier;

class using extends test_access_modifier{
    void meth2(){
        System.out.println(x);
        System.out.println(y);
        // System.out.println(z);
        // System.out.println(a);

        // we can only use public protected in sub classes.
    }
}

public class access_modifier_check {
    public static void main(String[] args) {

        test_access_modifier c = new test_access_modifier();
        System.out.println(c.x);
        // System.out.println(c.y);
        // System.out.println(c.z);
        // System.out.println(c.a);
        // we only use public modifier in world
    }
}

// Access Levels:

// Modifier    Class   Package     Subclass    World
// public	      Y        Y	       Y	      Y
// protected	  Y	       Y	       Y	      N
// no modifier	  Y	       Y	       N	      N
// private	      Y	       N	       N          N 
