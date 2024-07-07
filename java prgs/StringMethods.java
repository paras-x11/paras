
public class StringMethods {
    public static void main(String[] args) {
        
        String name = "Paras Rana";
        System.out.println(name);

        // Prints the original string
        // int value = name.length(); // Returns the length of the string
        // System.out.println(value);

        // String lstring = name.toLowerCase(); // Converts all characters to lowercase
        // System.out.println(lstring);

        // String ustring = name.toUpperCase(); // Converts all characters to uppercase
        // System.out.println(ustring);

        // String nonTrimmedString = "     Paras Rana     "; // String with leading and trailing spaces
        // System.out.println(nonTrimmedString);

        // String trimmedString = nonTrimmedString.trim(); // Removes leading and trailing spaces
        // System.out.println(trimmedString);

        // System.out.println(name.substring(1)); // Returns substring starting from index 1
        // System.out.println(name.substring(1,5)); // Returns substring from index 1 to 5 (exclusive)

        // System.out.println(name.replace('r', 'p')); // Replaces all occurrences of 'r' with 'p'
        // System.out.println(name.replace("r", "ier")); // Replaces all occurrences of "r" with "ier"

        // System.out.println(name.startsWith("Par")); // Checks if the string starts with "Par"
        // System.out.println(name.endsWith("na")); // Checks if the string ends with "na"

        // System.out.println(name.charAt(4)); // Returns the character at index 4

        // String modifiedName = "pavan rana rana";
        // System.out.println(modifiedName.indexOf("ana")); // Returns the index of the first occurrence of "ana"
        // System.out.println(modifiedName.indexOf("ana", 8)); // Returns the index of the first occurrence of "ana" after index 8
        // System.out.println(modifiedName.lastIndexOf("ana", 7)); // Returns the last occurrence of "ana" before index 7

        // System.out.println(name.equals("Paras Rana")); // Checks if two strings are equal
        // System.out.println(name.equalsIgnoreCase("paras rana")); // Checks if two strings are equal, ignoring case

        System.out.println("I am \"escape\" sequence\t double\b quote \\ printed.");
        // Demonstrates the use of escape sequences

        System.out.println("I am \"escape\" sequence\t double\b quote \\  using r \r yes");
        // Demonstrates the use of escape sequences including carriage return

        // Contains
        System.out.println(name.contains("Rana")); // Checks if the string contains "Rana"

        // Is Empty
        String emptyString = "";
        System.out.println(emptyString.isEmpty()); // Checks if the string is empty

        // Concat
        String greeting = "Hello, ";
        String fullGreeting = greeting.concat(name); // Concatenates two strings
        System.out.println(fullGreeting);

        // Split
        String[] parts = name.split(" "); // Splits the string into an array based on spaces
        for (String part : parts) {
            System.out.println(part);
        }

        // Join
        String joinedString = String.join("-", parts); // Joins the array elements into a single string with "-" as delimiter
        System.out.println(joinedString);

        // Matches
        System.out.println(name.matches("[A-Za-z ]+")); // Checks if the string matches the given regular expression

        // To Char Array
        char[] charArray = name.toCharArray(); // Converts the string into a character array
        for (char c : charArray) {
            System.out.println(c);
        }

        // Format
        String formattedString = String.format("My name is %s and I am %d years old.", name, 20); // Formats the string with placeholders
        System.out.println(formattedString);

        // Intern
        String internedString = name.intern(); // Returns the canonical representation of the string
        System.out.println(internedString);

        // CompareTo
        System.out.println(name.compareTo("Paras Rana")); // Compares two strings lexicographically
        System.out.println(name.compareTo("paras rana")); // Compares two strings lexicographically

        // CompareToIgnoreCase
        System.out.println(name.compareToIgnoreCase("paras rana")); // Compares two strings lexicographically, ignoring case

        // RegionMatches
        String anotherName = "Paran Rana";
        System.out.println(name.regionMatches(0, anotherName, 0, 5)); // Checks if two string regions are equal

        // CodePointAt
        System.out.println(name.codePointAt(1)); // Returns the Unicode code point at the specified index

        // CodePointBefore
        System.out.println(name.codePointBefore(1)); // Returns the Unicode code point before the specified index

        // CodePointCount
        System.out.println(name.codePointCount(0, name.length())); // Returns the number of Unicode code points in the specified text range

        // OffsetByCodePoints
        System.out.println(name.offsetByCodePoints(0, 3)); // Returns the index within this String that is offset from the given index by codePointOffset code points

        // GetBytes
        byte[] byteArray = name.getBytes(); // Converts the string into a byte array
        for (byte b : byteArray) {
            System.out.println(b);
        }

        // ContentEquals
        StringBuilder sb = new StringBuilder("Paras Rana");
        System.out.println(name.contentEquals(sb)); // Checks if the string content is equal to the StringBuilder content

        // HashCode
        System.out.println(name.hashCode()); // Returns the hash code of the string

        // SubSequence
        System.out.println(name.subSequence(0, 5)); // Returns a new character sequence that is a subsequence of this sequence

        // GetChars
        char[] charArray2 = new char[5];
        name.getChars(0, 5, charArray2, 0); // Copies characters from this string into the destination character array
        for (char c : charArray2) {
            System.out.println(c);
        }

        // Repeat
        System.out.println(name.repeat(3)); // Repeats the string 3 times

        // Strip, StripLeading, StripTrailing
        String stringWithSpaces = "   Paras Rana   ";
        System.out.println("'" + stringWithSpaces.strip() + "'"); // Removes leading and trailing whitespace
        System.out.println("'" + stringWithSpaces.stripLeading() + "'"); // Removes leading whitespace
        System.out.println("'" + stringWithSpaces.stripTrailing() + "'"); // Removes trailing whitespace

        // Transform
        String transformed = name.transform(s -> s + " is a good programmer"); // Transforms the string using a function
        System.out.println(transformed);

        // DescribeConstable
        System.out.println(name.describeConstable()); // Returns an Optional containing the String instance

        // Indent
        String indentedString = "Paras\nRana";
        System.out.println(indentedString.indent(4)); // Adds indentation to each line of the string

        // Lines
        indentedString.lines().forEach(System.out::println); // Returns a Stream of lines extracted from the string
    }
}
