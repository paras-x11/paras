import java.util.Scanner;

class circle1{
    public int radius;

    circle1(int r){
        this.radius = r;
    }

    public double area(){
        return Math.PI * this.radius * this.radius;
    }

    public double circumference(){
        return 2 * Math.PI * this.radius;
    }
}

class cylinder extends circle1{
    public int height;

    cylinder(int r, int h){
        super(r);
        this.height = h;
    }

    public double volume(){
        return Math.PI * this.radius * this.radius * this.height;
    }
}

// M3_8 Find circumference of rectangle formula: C = 2l + 2w or 2(l+w).

//M3_7 Find area of rectangle formula: A = w*l

class rectangle{
    public int length, width;

    rectangle(int l, int w){
        this.length = l;
        this.width = w;
    }

    public double area(){
        return this.length * this.width; 
    }

    public double circumference(){
        return 2 * (this.length +  this.width);
    }
}

class cubic extends rectangle{
    int height;

    cubic(int l, int w, int h){
        super(l, w);
        this.height = h;
    }

    public double volume(){
        return 1; // volume of cubic ??
    }
}

public class PracticeSet10 {
    public static void main(String[] args) {

        int r, ch, l, w, rh;

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter radius of circle: ");
        r = sc.nextInt();

        System.out.print("Enter height of cylinder: ");
        ch = sc.nextInt();

        cylinder c = new cylinder(r, ch); 
        
        System.out.println("area of circle is: " + c.area());

        System.out.println("circumference of circle is: " + c.circumference());

        System.out.println("volume of cylinder is: " + c.volume());

        System.out.print("Enter length of rectangle: ");
        l = sc.nextInt();

        System.out.print("Enter width of rectangle: ");
        w = sc.nextInt();

        System.out.print("Enter height of cubic: ");
        rh = sc.nextInt();

        cubic c2 = new cubic(l, w, rh);

        System.out.println("area of rectangle is: " + c2.area());

        System.out.println("area of rectangle is: " + c2.circumference());

        // make getters and setters for rectangle . constructor to circle me ek bar a gaye..

        sc.close();
    }
}
