public class DataTypes {

    public static void main(String[] args) {
             
        // 1 byte has 8 bit.
        // u can apply formula for byte: -(2^8)/2  to  (2^8)/2 - 1

        byte n1 = 20;                             // takes 1 byte.
        // Range: -(2^7) to (2^7)-1               // -1 because its include zero(0);
        // Range: -128 to 127
        System.out.println("Byte Example: " + n1);

       
        short n2 = 30;                            // takes 2 bytes.
        // Range: -(2^15) to (2^15)-1
        // Range: -32768 to 32767
        System.out.println("Short Example: " + n2);


        int n3 = 100;                             // takes 4 bytes.
        // Range: -(2^31) to (2^31)-1
        // Range: -2147483648 to 2147483647
        System.out.println("Int Example: " + n3);


        // for long l or L is reqiured at the end.
        long check = 100000000l;

        long n4 = 1000000L;                       // takes 8 bytes.
        // Range: -(2^63) to (2^63)-1
        // Range: -9223372036854775808 to 9223372036854775807
        System.out.println("Long Example: " + n4 + check);


        // for float f or F is reqiured at the end.
        float check2 = 100000000f;

        float n5 = 3.14f;                         // takes 4 bytes.
        // Range: approximately ±3.40282347E+38F 
        // Precision: 6-7 decimal digits
        System.out.println("Float Example: " + n5 + check2);

        // for double d or D is optional at the end.
        double check3 = 10000000000d;

        double n6 = 3.141592653589793;             // takes 8 bytes.
        // Range: approximately ±1.79769313486231570E+308
        // Precision: 15 decimal digits
        System.out.println("Double Example: " + n6 + check3);


        char n7 = 'A';                            // takes 2 bytes.
        // Range: '\u0000' (0) to '\uffff' (65,535 inclusive)
        System.out.println("Char Example: " + n7);


        Boolean n8 = true;                        // takes 1 bit.
        // Represents false as default values.
        System.out.println("Boolean Example: " + n8);
    }
}
