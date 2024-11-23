public class Current_Time {
    public static void main(String[] args) {
        System.out.println("\nSince jan 1 ,1970: \n");

        System.out.println("Current Mili Seconds: " + System.currentTimeMillis());

        long seconds = System.currentTimeMillis() / 1000;
        System.out.println("Seconds: " + seconds);

        long minutes = seconds / 60;
        System.out.println("Minutes: " + minutes);

        long hours = minutes / 60;
        System.out.println("Hours: " + hours);

        long days = hours / 365;
        System.out.println("Days: " + days);

        System.out.println("Years: " + System.currentTimeMillis() / 1000 / 3600 / 24 / 365);

        // is it safe to save this milliseconds in long data type:
        System.out.println("\n\nMaximum Size of long Data Type: " + Long.MAX_VALUE);
        System.out.println("Current Mili Seconds: " + System.currentTimeMillis());

    }
}
