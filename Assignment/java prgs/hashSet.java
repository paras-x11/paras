import java.util.HashSet;

public class hashSet {
    public static void main(String[] args) {

        HashSet<Integer> myHashSet = new HashSet<>(6,0.5f);

        myHashSet.add(8);
        myHashSet.add(3);
        myHashSet.add(10);
        myHashSet.add(5);
        myHashSet.add(9);
        myHashSet.add(12);
        myHashSet.add(12);

        // Hashset: hash means it uses hashing techniqe to sort the element and set means it takes unique values.
        // Hashing Technique: f(x) = x % 10 = position. 
        // if element is 11 then f(11) = 11 % 10 = 1; so 11 is stored at 1 position.
        // then if 21; f(21) = 21 % 10 = also 1; so 21 is stored at 1 pa6i ni je pn empty space hase tya store thase 21. *no need to going deep*

        System.out.println(myHashSet);

    }
}
