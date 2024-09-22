package calc;

public class test_access_modifier {
    public int x = 1;
    protected int y = 2;
    int z = 3;
    private int a = 4;

    public void meth1(){
        System.out.println(x);
        System.out.println(y);
        System.out.println(z);
        System.out.println(a);
    }

    public static void main(String[] args) {
        System.out.println("i am main method of test_access_modifier ");
    }
}
