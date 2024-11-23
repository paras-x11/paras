import shape.*;

public class UsingShapePackage {
    public static void main(String[] args) {

        Square s = new Square(10, 0);
        Rectangle r = new Rectangle(10, 20);
        Circle1 c = new Circle1(10, 20);
        Cylinder cy = new Cylinder(10, 20);
        Sphere sp = new Sphere(10, 20);

        System.out.println(s.area());
        System.out.println(r.area());
        System.out.println(c.area());
        System.out.println(cy.area());
        System.out.println(sp.area());
    }
}
