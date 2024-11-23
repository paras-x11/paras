package shape;

public class Sphere extends Shape{
    public Sphere(int dim1, int dim2){
        super(dim1, -1);
    }

    // 4(pi)r^2
    public double area(){
        return 4 * Math.PI * this.dim1 * this.dim1;
    }    
}
