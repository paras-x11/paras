// for proper input take reference from file: Module 3 -> basic logic prg -> M3_3.c    
    
import java.util.Scanner;

class properties{
    private
    int r;
    float a, p;
    float pi = 3.14f;

    public 
    void setRadius(int radius){
        r = radius;
    }
    
    int getRadius(){
        return r;
    }

    void setArea(float area){
        a = area;
    }
    
    float getArea(){
        return a;
    }

    void setPerimeter(float perimeter){
        p = perimeter;
    }
    
    float getPerimeter(){
        return p;
    }

    void checkArea(float a1){

        if(a1 == pi*r*r){
            System.out.println("Area " +a+ " according to radius " +r+ " is correct.");
            System.out.println("okay..");
        }
        else{
            System.out.println("Area " +a+ " according to radius " +r+ " is not correct.");
            System.out.println("not okay..");
        }
    }

    void checkPerimeter(float p1){

        if(p1 == 2*pi*r){
            System.out.println("Perimeter " +p+ " according to radius " +r+ " is correct.");
            System.out.println("okay..");
        }
        else{
            System.out.println("Perimeter " +p+ " according to radius " +r+ " is not correct.");
            System.out.println("not okay..");
        }
    }
};

public class Circle {

    public static void main(String[] args) {
        
        int radius; 
        float area, perimeter;

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter radius: ");
        radius = sc.nextInt();

        System.out.print("Enter area: ");
        area = sc.nextFloat();

        System.out.print("Enter perimeter: ");
        perimeter = sc.nextFloat();

        properties p = new properties();

        p.setRadius(radius);
        p.setArea(area);;
        p.setPerimeter(perimeter);

        System.out.println("Radius is: " + p.getRadius());
        System.out.println("Area is: " + p.getArea());
        System.out.println("Perimeter is: " + p.getPerimeter());

        System.out.println();
        p.checkArea(area);

        System.out.println();
        p.checkPerimeter(perimeter);

        sc.close();
    }
}


