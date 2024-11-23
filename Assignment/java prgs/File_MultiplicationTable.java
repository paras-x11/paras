import java.io.*;

public class File_MultiplicationTable {
    public static void main(String[] args) {
        
        File myFile = new File("File_MultiplicationTable.txt");

        try {
            if (myFile.createNewFile()) {
                System.out.println("File is created. " + myFile.getName());
            }
            else{
                System.out.println("File Already exist. " + myFile.getName());
            }   
        } 
        catch (IOException e) {
            e.printStackTrace();
        }



        String table = "";

    
        for (int n = 1; n < 10; n++) {
            
            for (int i = 1; i <= 10; i++) {
                table += n + " x " + n + " = " + n*i;
                table += "\n";            
            }
            table += "\n";
            table += "\n";                        
        }

        // System.out.println(table);


        // // this will over write the all existing content
        // try {
        //     FileWriter writeFile = new FileWriter("File_MultiplicationTable.txt");               
            
        //     writeFile.write(table);
        //     writeFile.close();
        // } 

        // catch (IOException e) {
        //     e.printStackTrace();
        // }

        

        // // this will append to existing content
        try {
            FileWriter writeFile = new FileWriter("File_MultiplicationTable.txt", true);        // append mode
            
            writeFile.write(table);
            System.out.println("Append Succesfully. ");
            writeFile.close();
        } 

        catch (IOException e) {
            e.printStackTrace();
        }



        // To clear the contents of a file in Java and make it empty, you can use the FileWriter class with the default constructor or 
        // by specifying the file path with the append flag set to false. This will overwrite the existing file, effectively clearing its content.
        
        // String filePath = "File_MultiplicationTable.txt"; // Specify your file path

        // try {
        //     // Create a FileWriter without the append flag
        //     FileWriter writer = new FileWriter(filePath, false); // false to overwrite the file
        //     writer.write(""); // Write an empty string to clear the content
        //     writer.close();
        //     System.out.println("File cleared successfully.");
        // } 
        // catch (IOException e) {
        //     e.printStackTrace();
        // }
    }
}

