// import java.util.ArrayDeque;
// import java.util.ArrayList;
// import java.util.Collection;
import java.util.*;

public class arrayDeque {
    public static void main(String[] args) {
        
        ArrayDeque<Integer> ad = new ArrayDeque<>();

        ad.add(3);
        ad.add(56);
        ad.add(9);
        ad.addLast(100);
        ad.add(5);
        ad.addFirst(1);
        ad.add(89);


        System.out.println("Array Deque before addAll l1(ArrayList): ");
        for (Integer element : ad) {
                System.out.print(element + ", ");
        }

        System.out.println("\n");
        System.out.println("First element: " + ad.getFirst());
        System.out.println("Last element: " + ad.getLast());

        ArrayList<Integer> l1 = new ArrayList<>();

        l1.add(6);
        l1.add(7);
        l1.add(6);
        l1.add(9);
        l1.add(7);
        l1.add(5);
        l1.add(0, 2);
        l1.add(0, 1);
        l1.add(2, 3);

        ad.addAll(l1);

        System.out.println("\nArray Deque After addAll l1(ArrayList): ");
        for (Integer element : ad) {
            System.out.print(element + ", ");
        }

        System.out.println("\n");
        System.out.println("First element: " + ad.getFirst());
        System.out.println("Last element: " + ad.getLast());

        ad.remove(89);
        System.out.println("\nArray Deque After removing 89:  ");
        for (Integer element : ad) {
            System.out.print(element + ", ");
        }    
    }
}
