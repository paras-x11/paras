import java.util.Date;    // this is deprecated.

public class Current_Date {
    @SuppressWarnings("deprecation")
    public static void main(String[] args) {
        Date d = new Date();
        System.out.println(d);

        System.out.println(d.getTime());
        System.out.println(d.getDate());
        System.out.println(d.getTimezoneOffset());
        System.out.println(d.getDay());
        System.out.println(d.getYear());  // since 1900: 1900 to 2024 = 124
        System.out.println(d.getSeconds());
    }   
}
