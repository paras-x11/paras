
public class StringConcept {
    public static void main(String[] args) {

        String name = "Paras Rana";
        name = name.toUpperCase(); 
        System.out.println(name); 
        // Explanation:
        // The variable `name` initially references the string object "Paras Rana".
        // When `name = name.toUpperCase();` is executed, it creates a new string object "PARAS RANA" with all characters in uppercase.
        // The variable `name` is then reassigned to reference this new string object.

        // Immutable Concept:
        // Strings in Java are immutable, meaning their content cannot be changed once created.
        // The `toUpperCase()` method does not modify the original string "Paras Rana".
        // Instead, it creates a new string object "PARAS RANA" with uppercase characters.
        // The original string "Paras Rana" remains unchanged in memory.

        // if string is immutable how it changed with this toUpper methods.
        // ans: 
        // The toUpperCase() method does not modify the existing string object "Hello, World!". 
        // Instead, it creates a new string object "HELLO, WORLD!" with all characters converted to uppercase.
        // The reference variable old is then reassigned to point to this new string object "HELLO, WORLD!". 
        // The original string object "Hello, World!" remains unchanged in memory.
        
        // so, how to access this old string that is unchanged in memory:
        String old = "Hello, World!";

        String new_str = old; // Store reference of original string
        
        old = old.toUpperCase(); 
        System.out.println("old: " +old); 
        System.out.println("accesing old string using new_str: " +new_str);
        
        // Explanation:
        // Here, `old` initially references the string object "Hello, World!".
        // `new_str` is assigned the same reference as `old`, so both variables initially point to the original string object.
        // After `old = old.toUpperCase();`, `old` now references the new string object "HELLO, WORLD!" created by `toUpperCase()`.
        // However, `new_str` still holds the reference to the original string object "Hello, World!".
        // This demonstrates that even though `old` was reassigned, the original string object remains accessible through `new_str`.

           
    }
}
