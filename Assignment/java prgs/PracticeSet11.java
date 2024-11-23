// Que 1:
interface BasicAnimal {
    void eat();
    void sleep();
}

class Monkey{
    public
    void jump(){
        System.out.println("Jump");
    }

    void bite(){
        System.out.println("Bite");
    }
}

class Human extends Monkey implements BasicAnimal {
    
    public void speak(){
        System.out.println("Speaking");
    }

    public void jump(){
        System.out.println("Jump");
    }

    public void bite(){
        System.out.println("Bite");
    }

    public void eat(){
        System.out.println("Eating");
    }

    public void sleep(){
        System.out.println("Sleeping");
    }
}

//Que 2
abstract class TelePhone{
    abstract void ring();
    abstract void lift();
    abstract void disconnect();
}

class SmartTelephone extends TelePhone{

    public void playMusic(){
        System.out.println("Playing Music...");
    }

    public void ring(){
        System.out.println("Tililik Tililik");
    }

    public void lift(){
        System.out.println("Lifting....");
    }

    public void disconnect(){
        System.out.println("Disconnecting...");
    }
}

// Que 3:

interface TVRemote{
    void cell();
    void normalFuntions();
}

interface SmartTVRemote extends TVRemote{
    void NetflixButton();
    void YoutubeButton();    
}

class TV implements TVRemote{
    void PlayMovies(){
        System.out.println("Playing Movies...");
    }

    public void cell(){
        System.out.println("Changing Cell...");
    }

    public void normalFuntions(){
        System.out.println("Functioning...");
    }
}

public class PracticeSet11 {
    public static void main(String[] args) {
        // Que 1:
        Human h = new Human();
        h.jump();
        h.bite();
        h.eat();
        h.sleep();
    
        // que 2:
        TelePhone t = new SmartTelephone();
        // t.playMusic();
        t.ring();
        t.lift();
        t.disconnect();

        //Que 3:
        TV tv = new TV();

        tv.PlayMovies();
    }
}
