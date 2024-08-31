import java.util.Scanner;

class l1 {

    String[] books;
    int no_of_books;

    l1() {
        this.books = new String[100];
        this.no_of_books = 0;
    }

    public void addBook(String book) {
        if (isDuplicate(book)) {
            System.out.println("-> " + book + " already exists in the library.");
        } else {
            this.books[no_of_books] = book;
            no_of_books++;
            System.out.println("-> " + book + " has been added.");
        }
    }

    private boolean isDuplicate(String book) {
        for (int i = 0; i < this.no_of_books; i++) {
            if (this.books[i] != null && this.books[i].equals(book)) {
                return true;
            }
        }
        return false;
    }

    public void issueBook(String book) {
        for (int i = 0; i < this.no_of_books; i++) {
            if (this.books[i] != null && this.books[i].equals(book)) {
                System.out.println("-> The book: " + book + " has been issued.");
                this.books[i] = null;
                return;
            }
        }
        System.out.println("-> The book: " + book + " does not exist.");
    }

    public void returnBook(String book) {
        addBook(book);
    }

    public void showAvailableBooks() {
        int n = 1;
        System.out.println("\n-> Available books are: ");
        for (int i = 0; i < this.no_of_books; i++) {
            if (this.books[i] != null) {
                System.out.println((n++) + ". " + this.books[i]);
            }
        }
    }
}

public class Library {
    @SuppressWarnings("resource")
    public static void main(String[] args) {

        String str;

        Scanner sc = new Scanner(System.in);
        l1 l = new l1();

        while (true) {
            System.out.printf("\n 1 for add book \t 2 for issue book \t 3 for return book \t 4 for show available books \t 0 for exit");
            System.out.print("\n\nEnter your choice: ");
            int ch = sc.nextInt();

            switch (ch) {
                case 1:
                    System.out.print("\nEnter book: ");
                    sc.nextLine(); 
                    str = sc.nextLine();

                    l.addBook(str);
                    break;

                case 2:
                    System.out.print("Issue book: ");
                    sc.nextLine(); 
                    str = sc.nextLine();

                    l.issueBook(str);
                    break;

                case 3:
                    System.out.print("Return book: ");
                    sc.nextLine(); 
                    str = sc.nextLine();

                    l.returnBook(str);
                    break;

                case 4:
                    l.showAvailableBooks();
                    break;

                case 0:
                    return;

                default:
                    System.out.println("-> Invalid Choice.");
                    break;
            }
        }
    }
}
