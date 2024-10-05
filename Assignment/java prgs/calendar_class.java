import java.util.Calendar;
import java.util.TimeZone;

public class calendar_class {
    public static void main(String[] args) {
        
        System.out.println("Available calendar types: " + Calendar.getAvailableCalendarTypes());

        // instance of Calendar class. Calendar is abstract class
        Calendar c = Calendar.getInstance();

        System.out.println(c.getTime());
        System.out.println(c.get(Calendar.DATE));
        System.out.println(c.get(Calendar.HOUR));
        System.out.println(c.get(Calendar.MINUTE));
        System.out.println(c.get(Calendar.SECOND));
        System.out.println(c.get(Calendar.YEAR));
        System.out.println();

        System.out.print("printing time: ");
        System.out.println(c.get(Calendar.HOUR) + ":" + c.get(Calendar.MINUTE) + ":" + c.get(Calendar.SECOND));

        Calendar c1 = Calendar.getInstance();
        System.out.println("\nCurrent calendar type: " + c1.getCalendarType());
        System.out.println("Current time zone: " + c1.getTimeZone());  // by default Asia-Calcutta

        System.out.println("\n\nAfter Changing Time Zone: \n");

        Calendar c2 = Calendar.getInstance(TimeZone.getTimeZone("Asia/Singapore"));
        System.out.println("Current calendar type: " + c2.getCalendarType());
        System.out.println("Current time zone: " + c2.getTimeZone());  // by default Asia-Calcutta

        
    }
}
