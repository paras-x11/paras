public class PracticeSet10 {
    
    public class circle{
        public int radius;

        circle(int r){
            this.radius = r;
        }

        public double area(){
            return Math.PI*this.radius*this.radius;
        }
    }

    public class cylinder extends circle{
        public int height;

        cylinder(int r, int h){
            super(r);
            this.height = h;
        }

        public double volume(){
            return Math.PI*this.radius*this.radius*this.height;
        }
    }

    public static void main(String[] args) {
        
        
    }
}
