class MyGeneric<T1, T2>{
    int value = 34;

    private T1 t1;
    private T2 t2;
    
    public MyGeneric(int value, T1 t1, T2 t2) {
        this.value = value;
        this.t1 = t1;
        this.t2 = t2;
    }
    
    public void setValue(int value) {
        this.value = value;
    }
    public int getValue() {
        return value;
    }
    
    public void setT1(T1 t1) {
        this.t1 = t1;
    }
    public T1 getT1() {
        return t1;
    }
    
    public void setT2(T2 t2) {
        this.t2 = t2;
    }
    public T2 getT2() {
        return t2;
    }
   
}



public class generics {
    public static void main(String[] args) {
       
        @SuppressWarnings({ "rawtypes", "unchecked" })
        
        MyGeneric<String, Integer> g = new MyGeneric(32, "Hello from", 65);

        String str = (String) g.getT1();
        int x =  (int) g.getT2();

        System.out.println(str + x);
    }
}
