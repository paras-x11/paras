import java.time.LocalDateTime;
import java.time.LocalTime;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.Calendar;
import java.util.Date;
import java.util.HashSet;
import java.util.Scanner;

public class Advance_java_PS {
    @SuppressWarnings("deprecation")
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        ArrayList<Integer> s = new ArrayList<>();

        System.out.print("How Many Students You Want To Insert: ");
        int n = sc.nextInt();

        System.out.println("\nEnter " + n + " Student Marks: ");

        for (int i = 0; i < n; i++) {
            int input = sc.nextInt();
            s.add(input);    
        }

        System.out.println("\n\nStudents marks are: ");
        for (Integer element : s) {
            System.out.print(element + ", ");
        }
        

        HashSet<Integer> hs = new HashSet<>();

        hs.add(0);
        hs.add(1);
        hs.add(2);
        hs.add(3);
        hs.add(4);
        hs.add(4);
        hs.add(0);

        System.out.print("\n\nElements of set: \n");
        for (Integer e : hs) {
            System.out.print(e + ", ");
        }
        

        System.out.println("\n\nDisplaying TIme: ");
        Date d = new Date();
        System.out.println("\n\nUsing Date Class: " + d.getHours() + ":" + d.getMinutes() + ":" + d.getSeconds());

        Calendar c = Calendar.getInstance();
        System.out.println("\n\nUsing Calendar Class: " + c.get(Calendar.HOUR) + ":" + c.get(Calendar.MINUTE) + ":" + c.get(Calendar.SECOND));

        // LocalTime t = LocalTime.now();
        LocalTime t = LocalTime.now().withNano(0);
        System.out.println("\n\nUsing LocalTime Class from java date and time API: " + t);

        LocalDateTime dt = LocalDateTime.now();
        DateTimeFormatter dtf = DateTimeFormatter.ofPattern("H:m:s");

        String myDate = dt.format(dtf);
        System.out.println("\n\nUsing LocalDateTime with DateTimeFormatter: " + myDate);


        sc.close();
    }
}
