import java.util.*;

public class gregorian_calendar {
    public static void main(String[] args) {
        // Calendar is abstarct class so we make instance of it
        // Calendar c = Calendar.getInstance();

        // GregorianCalendar is a concrete class
        GregorianCalendar g = new GregorianCalendar();

        System.out.println("is 2020 leap year: " + g.isLeapYear(2020));
        System.out.println("is 2018 leap year: " + g.isLeapYear(2018));

        System.out.println();
        System.out.println(TimeZone.getAvailableIDs()[0]);
        System.out.println(TimeZone.getAvailableIDs()[1]);
        System.out.println(TimeZone.getAvailableIDs()[2]);
        System.out.println(TimeZone.getAvailableIDs()[3]);
        System.out.println(TimeZone.getAvailableIDs()[4]);       

    }   
}
