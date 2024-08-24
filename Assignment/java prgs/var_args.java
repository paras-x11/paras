public class var_args {

    // syntax:

    // public static void method_name(int ...arr){
    //     arr is available here as int[] arr
    // }

    static int add(int ...arr){                 // (3 dots)it creates array 
        int result = 0;
        for (int a : arr){
            result = result + a;
        }
        return result;
    }

    public static void main(String[] args){
        System.out.println(add(1,2));
        System.out.println(add(2,3,4));
        System.out.println(add(4,5,6));
        System.out.println(add(4,5,6));
        System.out.println(add(4,5,6,7));
        System.out.println(add(1,2,3,4,5,6));
    }
}

