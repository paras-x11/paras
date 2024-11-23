//checkin in same class ans same package

// for world and subclass go to access_modifier_check.java in java prgs

package calc;

class c1{
    public int x = 1;
    protected int y = 2;
    int z = 3;
    private int a = 4;

    public void meth1(){
        System.out.println(x);
        System.out.println(y);
        System.out.println(z);
        System.out.println(a);

        // in same class we can use all access specifier
    }
}

public class access_modifier {
    public static void main(String[] args) {
        c1 c = new c1();

        System.out.println(c.x);
        System.out.println(c.y);
        System.out.println(c.z);

        c.meth1();

        // System.out.println(c.a);
        // we can't use private in same package
    }
}

// Access Levels:

// Modifier    Class   Package     Subclass    World
// public	      Y        Y	       Y	      Y
// protected	  Y	       Y	       Y	      N
// no modifier	  Y	       Y	       N	      N
// private	      Y	       N	       N          N 