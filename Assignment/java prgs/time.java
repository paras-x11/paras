import java.time.*;

public class time {
    public static void main(String[] args) {
        
        LocalDate d = LocalDate.now();
        System.out.println("Local Date: " + d);
        
        LocalTime t = LocalTime.now();
        System.out.println("Local Time: " + t);
        
        LocalDateTime dt = LocalDateTime.now();
        System.out.println("Local Date-Time: " + dt);

        
    }
}
