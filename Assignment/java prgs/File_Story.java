import java.io.*;
import java.util.*;

public class File_Story {
    public static void main(String[] args) {

        File myFile = new File("file_story.txt");
        
        try{
            Scanner sc = new Scanner(myFile);

            while (sc.hasNextLine()) {
                System.out.println(sc.nextLine());
            }
            
            sc.close();
        }
        catch(FileNotFoundException e){
            e.printStackTrace();
        }
    }
}
