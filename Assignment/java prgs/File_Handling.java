import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

@SuppressWarnings("unused")
public class File_Handling {
    public static void main(String[] args) {

        // File myFile = new File("File_Handling.txt");             // for creating file...
        // try {
        //     myFile.createNewFile();
        // } 
        // catch (IOException e) {
        //     System.out.println("Unable to create this file.");
        //     e.printStackTrace();
        // }
        // System.out.println(myFile.getAbsolutePath());



        // try {                                                     // for writing file
        //     FileWriter fileWriter = new FileWriter("File_Handling.txt");
        //     fileWriter.write("This is first file from our java course.\nok bye.");
        //     fileWriter.close();
        // } 
        // catch (IOException e) {
        //     e.printStackTrace();
        // }




        // File readFile = new File("File_Handling.txt");        // for reading file
        
        // Scanner sc;
        // try {
        //     sc = new Scanner(readFile);

        //     while (sc.hasNextLine()) {
        //         System.out.println(sc.nextLine());
        //     }
            
        //     sc.close();
        // } 
        // catch (FileNotFoundException e) {
        //     e.printStackTrace();
        // }




        // File myFile2 = new File("File_Creating.txt");             // for creating file...
        // try {
        //     if(myFile2.createNewFile()){
        //         System.out.println("File is created " + myFile2.getName());
        //     }
        //     else{
        //         System.out.println("File is already available.");
        //     }
        // } 
        // catch (IOException e) {
        //     System.out.println("Unable to create this file.");
        //     e.printStackTrace();
        // }


        
        File myFile2 = new File("File_creating.txt");                // for deleting file
        if (myFile2.delete()) {
            System.out.println("File is deleted. " + myFile2.getName());
        }
        else{
            System.out.println("Some problem occured.");
        }


    }
}
