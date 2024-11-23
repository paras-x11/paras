interface camera{
    void takeSnap();
    void recordVideo();

    private void greet(){
        System.out.println("Good Morning...");
    }

    default void record4KVideo(){
        greet();
        System.out.println("Recording 4K Video...");
    }
}

interface WiFi{
    String[] getNetworks();
    void connectToNetwork(String network);
}

class CellPhone{
    void callNumber(int phoneNumber){
        System.out.println("calling... " + phoneNumber);
    }

    void pickCall(){
        System.out.println("Connecting... ");
    }
}

class SmartPhone1 extends CellPhone implements camera, WiFi{
    public void takeSnap(){
        System.out.println("Taking Snap... ");
    }

    public void recordVideo(){
        System.out.println("Recording Video... ");
    }

    // if we want override default method we can and this overridden method is executed.
    @Override
    public void record4KVideo(){
        System.out.println("Taking Snap nd Then Reording 4K Video...");
    }

    public String[] getNetworks(){
        System.out.println("Getting list of networks: ");
        String[] networkList = {"TP-Link", "D-Link", "Jio", "Airtel5G"};
        return networkList;
    }

    public void connectToNetwork(String network){
        System.out.println("connecting to network " + network);
    }
}

public class interfaces2 {
    public static void main(String[] args) {

        SmartPhone1 s = new SmartPhone1();

        s.callNumber(98980);
        s.pickCall();

        s.takeSnap();
        s.recordVideo();

        s.record4KVideo();
        // s.greet();       // throws error bcoz its private

        String[] str = s.getNetworks();

        for (String item : str) {
            System.out.println(item);
        }

        s.connectToNetwork("Airtel5G");
    }
}
