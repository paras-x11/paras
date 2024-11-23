import java.time.*;
import java.time.format.DateTimeFormatter;

public class Date_Time_Formatter {
    public static void main(String[] args) {

        LocalDateTime dt = LocalDateTime.now(); 
        System.out.println(dt);
        
        DateTimeFormatter dtf = DateTimeFormatter.ofPattern("dd-MM/yyyy");      // custom format  --more on oracle java doc
        String myDate = dt.format(dtf);     // creating date string using date time format
        System.out.println(myDate);

        DateTimeFormatter dtf2 = DateTimeFormatter.ISO_LOCAL_DATE;      // pre-defined format
        String myDate2 = dt.format(dtf2);     
        System.out.println(myDate2);

        DateTimeFormatter dtf3 = DateTimeFormatter.ofPattern("dd-MM/yyyy -- E H:m a");      // custom format  --more on oracle java doc
        String myDate3 = dt.format(dtf3);     // creating date string using date time format
        System.out.println(myDate3);

    }
}
