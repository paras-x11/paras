// import java.util.ArrayList;
// import java.util.Set;
// import java.util.TreeSet;
import java.util.*;

public class Linked_List{
    public static void main(String[] args) {
        // ArrayList;
        // Set;
        // TreeSet;

        LinkedList<Integer> l1 = new LinkedList<>();
        LinkedList<Integer> l2 = new LinkedList<>();

        l1.add(6);
        l1.add(7);
        l1.add(6);
        l1.add(9);
        l1.add(7);
        l1.add(5);
        l1.add(0, 2);
        l1.add(0, 1);
        l1.add(2, 3);

        l2.add(51);
        l2.add(52);
        l2.add(53);
        l2.add(55);
        l2.add(3, 54);

        // l1.addAll(l2);
        l1.addAll(0, l2);

        System.out.println("Check value is in collection or not: " + l1.contains(27));

        System.out.println("Index of 5: " + l1.indexOf(5));

        System.out.println("Index of 5: " + l1.indexOf(6));
        System.out.println("LAst Index of 5: " + l1.lastIndexOf(6));


        for (int i = 0; i < l1.size(); i++) {
            System.out.print(l1.get(i) + ", ");
        }

        l1.remove(8);

        l1.set(8,4);

        l1.addLast(11);

        l1.addFirst(50);

        System.out.println("\n\nAfter Modification: ");
        for (int i = 0; i < l1.size(); i++) {
            System.out.print(l1.get(i) + ", ");
        }

        System.out.println("\nBefore Clear: ");
        for (Integer Element : l2) {
            System.out.print(Element + ", ");
        }

        System.out.println("\nAfter Clear: ");
        l2.clear();
        for (Integer Element : l2) {
            System.out.print(Element + ", ");
        }

    }   
}
