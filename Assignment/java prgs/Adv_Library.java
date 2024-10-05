// Create a library management system which is capable of issuing books to the students.
// Book should have info like:
// 1. Book name
// 2. Book Author
// 3. Issued to
// 4. Issued on
// User should be able to add books, return issued books, issue books
// Assume that all the users are registered with their names in the central database

// baki...

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.Scanner;

class a_library{
    
    int no_of_books;
    String[] name;
    String[] book_name;
    String[] book_author;
    
    LocalDate d = LocalDate.now();
    DateTimeFormatter df = DateTimeFormatter.ofPattern("dd-MM-yyyy");
    String date = d.format(df);

    a_library(){
        this.no_of_books = 0;
        this.book_name = new String[100];
        this.book_author = new String[100];
    }

    public String getDate(){
        return date;
    }

    public void addBook(String book, String author){
        if(!isDuplicate(book)){
            this.book_name[no_of_books] = book;
            this.book_author[no_of_books] = author;
            no_of_books++;
            System.out.println("-> " + book + " by " + author + " has been added on " + getDate());
        }
        else{
            System.out.println("-> " + book + " already exists in the library.");
        }
    }

    public boolean isDuplicate(String book){
        for (int i = 0; i < no_of_books; i++) {
            if(this.book_name[i].equals(book)){
                return true;
            }
        }
        return false;
    }

    public void issueBook(String book) {
        for (int i = 0; i < no_of_books; i++) {
            if (this.book_name[i] != null && this.book_name[i].equals(book)) {
                System.out.println("-> " + book + " has been issued.");
                this.book_name[i] = null;
                this.book_author[i] = null;
                return;
            }
        }
        System.out.println("-> " + book + " is not available in the library.");
    }

    public void returnBook(String book, String author){
        addBook(book, author);
    }

    public void showAvailableBooks(){
        for (int i = 0; i < no_of_books; i++) {
            if (this.book_name[i] != null) {
                System.out.println("-> " + book_name[i] + " by " + book_author[i]);  
            }  
        }
    }


}
public class Adv_Library {
    public static void main(String[] args) {
        String book, author, name=null;

        System.out.println(name);              // delete this line

        Scanner sc = new Scanner(System.in);
        a_library l = new a_library();

        while (true) {
            System.out.printf("\n 1 for add book \t 2 for issue book \t 3 for return book \t 4 for show available books \t 0 for exit");
            System.out.print("\n\nEnter your choice: ");
            int ch = sc.nextInt();

            switch (ch) {
                case 1:
                    System.out.print("\nEnter book: ");
                    sc.nextLine(); 
                    book = sc.nextLine();
                    
                    System.out.print("\nEnter author: ");
                    author = sc.nextLine();

                    l.addBook(book, author);
                    break;

                case 2:
                    System.out.print("Issue book: ");
                    sc.nextLine(); 
                    book = sc.nextLine();

                    l.issueBook(book);
                    break;

                case 3:
                    System.out.print("\nEnter book: ");
                    sc.nextLine(); 
                    book = sc.nextLine();
                    
                    System.out.print("\nEnter author: ");
                    author = sc.nextLine();

                    l.addBook(book, author);
                    break;

                case 4: l.showAvailableBooks();
                    break;

                case 0:
                    return;

                default:
                    System.out.println("-> Invalid Choice.");
                    break;
            }        
            sc.close();
        }
    }
}
