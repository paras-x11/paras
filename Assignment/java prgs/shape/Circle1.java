package shape;

public class Circle1 extends Shape{
    public Circle1(int dim1, int dim2){
        super(dim1, -1);
    }

    public double area(){
        return Math.PI * this.dim1 * this.dim1;
    }    
}
