package shape;

public class Cylinder extends Shape{
    public Cylinder(int dim1, int dim2){
        super(dim1, dim2);
    }

    // 2(pi)rh + 2(pi)r^2
    // 2(pi)r * (h + r)         // common kadhyu
    public double area(){               
        return 2 * Math.PI * this.dim1 * (this.dim2 + this.dim1);
    }   
}
