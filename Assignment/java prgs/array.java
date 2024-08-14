import java.util.Scanner;

@SuppressWarnings("unused")
public class array {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        // ------------------------------------------------------------------------------------------ //

        // int[] marks = {98, 56, 85, 89, 45};

        // for (int i : marks) {
        //     System.out.println(i+10);
        // }

        // ------------------------------------------------------------------------------------------ //

        // int[] marks1 = new int[5];

        // System.out.println("enter elements of Array: ");
        // for (int i = 0; i < marks1.length; i++) {
        //     marks1[i] = sc.nextInt();
        // }

        // in java for-each loop is only used for read(traverse) element in array. for-each loop doesn't provide access to index. so use for loop
        // this is not pure for eacch loop. whith this we can manually keep track of the position where the input should go
        // int i=0;                  
        // for(int element: marks1){
        //     marks1[i++] = sc.nextInt();
        // }

        // System.out.println("You entered: ");
        // for (int element : marks1) {
        //     System.out.println(element);
        // }

        // -----------------------------------------2D array------------------------------------------------ //
        int i, j;
        int[][] flats;
        flats = new int[2][3];

        System.out.println("enter elements of Array: ");
        for (i=0; i < flats.length; i++) {

            for(j=0; j < flats[i].length; j++) {
                
                flats[i][j] = sc.nextInt();
            }
            System.out.println();
        }

        for (int[] row : flats) {
            for (int element : row) {
                System.out.print(element+ " ");
            }
            System.out.println();
        }
        // ----------------------------------------------------------------------------------------- //



        sc.close();

    }

}
