import java.util.Scanner;

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
        // int i, j;
        // int[][] flats;
        // flats = new int[2][3];

        // System.out.println("enter elements of Array: ");
        // for (i=0; i < flats.length; i++) {

        //     for(j=0; j < flats[i].length; j++) {
        //         System.out.printf("Enter array element [%d][%d]: ", i, j);
        //         flats[i][j] = sc.nextInt();
        //     }
        //     System.out.println();
        // }

        // for (int[] row : flats) {
        //     for (int element : row) {
        //         System.out.print(element+ " ");
        //     }
        //     System.out.println();
        // }
        // ----------------------------------------------------------------------------------------- //
        // que 1: make array of floats and display their sum
        // float sum = 0; int i;
        // float[] array = new float[5];
        // System.out.println("enter elements of Array: ");
        // for (i=0; i < array.length; i++) {

        //     System.out.printf("Enter array element [%d]: ", i);
        //     array[i] = sc.nextFloat();
        // }
        // System.out.println("your array is: ");
        // for (i=0; i < array.length; i++) {

        //     System.out.println(array[i]);
        //     sum = sum + array[i];
        // }
        // System.out.println("sum of all element of array is: "+sum);
        
        // ----------------------------------------------------------------------------------------- //
        
        // que 2: check wether the number is in array or not.
        // int[] marks = new int[5];
        // System.out.println("enter elements of Array: ");
        // for (int i=0; i < marks.length; i++) {

        //     System.out.printf("Enter array element [%d]: ", i);
        //     marks[i] = sc.nextInt();
        // }
        
        // boolean check = false;
        
        // System.out.println("Enter element to check: ");
        // int num = sc.nextInt();
        // for(int element: marks){
        //     if(num==element){
        //         check = true;
        //         break;
        //     }
        // }
        
        // if(check){
        //     System.out.println("yes");
        // }
        // else{
        //     System.out.println("no");
        // }
        
        // ----------------------------------------------------------------------------------------- //
        
        // que 3:calculate avg marks from an array containing all marks of all student in physics using foreach loop.
        // int row;
        // float sum=0, avg;
        // System.out.println("Enter number of students: ");
        // row = sc.nextInt();
        // float[] physics = new float[row];
        
        // for(int i=0; i<row; i++){
           
        //     System.out.printf("Enter student marks [%d]: ", i);
        //     physics[i] = sc.nextInt(); 
        // }
        
        // for(float element : physics){
        //     sum = sum + element;
        // }
        // System.out.println(sum);
        
        // System.out.println(sum / physics.length);
        
        
        // ----------------------------------------------------------------------------------------- //
        // que 4: addition of 2 matrix of 2x3
        // int i, j;
        // int[][] a= new int [2][3];
        // int[][] b= new int [2][3];
        
        // System.out.println("enter elements of Array1: ");
        // for (i=0; i < a.length; i++) {

        //     for(j=0; j < a[i].length; j++) {
        //         System.out.printf("Enter array element [%d][%d]: ", i, j);
        //         a[i][j] = sc.nextInt();
        //     }
        //     System.out.println();
        // }
        
        // System.out.println("enter elements of Array2: ");
        // for (i=0; i < b.length; i++) {

        //     for(j=0; j < b[i].length; j++) {
        //         System.out.printf("Enter array element [%d][%d]: ", i, j);
        //         b[i][j] = sc.nextInt();
        //     }
        //     System.out.println();
        // }
        
        // System.out.println("Array 1: ");
        // for (i=0; i < 2; i++) {

        //     for(j=0; j < 3; j++) {
        //         System.out.printf("%d\t", a[i][j]);
        //     }
        //     System.out.println();
        // }
        
        // System.out.println("Array 2: ");
        // for (i=0; i < 2; i++) {

        //     for(j=0; j < 3; j++) {
        //         System.out.printf("%d\t", b[i][j]);
        //     }
        //     System.out.println();
        // }
        
        // System.out.println("sum is: ");
        // for (i=0; i < 2; i++) {

        //     for(j=0; j < 3; j++) {
        //         System.out.printf("%d\t", a[i][j] + b[i][j]);
        //     }
        //     System.out.println();
        // }
        
        // ----------------------------------------------------------------------------------------- //
        // que 5: reverse Array
        // int row;
        // System.out.print("Enter size of array: ");
        // row = sc.nextInt();
        // int[] array = new int[row];
        
        // for(int i=0; i<array.length; i++){
           
        //     System.out.printf("Enter element [%d]: ", i);
        //     array[i] = sc.nextInt(); 
        // }
        
        // System.out.println("Reverse array is: ");
        // for (int i = array.length - 1; i >= 0; i--) {
        //     System.out.print(array[i]);
        //     if (i > 0) {
        //         System.out.print(", ");
        //     }
        // }
        
        // ----------------------------------------------------------------------------------------- //
        // que 6: find max element in array.
        // int row;
        // int max = Integer.MIN_VALUE;           //int min = Integer.MAX_VALUE;
        // System.out.print("Enter size of array: ");
        // row = sc.nextInt();
        // int[] array = new int[row];
        
        // for(int i=0; i<array.length; i++){
           
        //     System.out.printf("Enter element [%d]: ", i);
        //     array[i] = sc.nextInt(); 
        // }
        
        // for(int element: array){                 
        //     if(element > max){                   // if ( element < min)
        //         max = element;
        //     }
        // }
        // System.out.println(max);
        
        // ----------------------------------------------------------------------------------------- //
        
        // que 7: check array is sorted(asc) or not
        int row;
        boolean isSorted = true;
        System.out.print("Enter size of array: ");
        row = sc.nextInt();
        int[] array = new int[row];
        
        for(int i=0; i<array.length; i++){
           
            System.out.printf("Enter element [%d]: ", i);
            array[i] = sc.nextInt(); 
        }
        
        for(int i=0; i<array.length-1; i++){
            if(array[i] > array[i+1]){
                isSorted=false;
                break;
            }
        }
        
        if(isSorted){
            System.out.println("array is sorted.");
        }
        else{
            System.out.println("array is not sorted.");
        }
        
        
        // ----------------------------------------------------------------------------------------- //
        sc.close();

    }

}