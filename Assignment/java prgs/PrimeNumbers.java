public class PrimeNumbers {
    public static void main(String[] args) {
        int i, j;

        for (i = 2; i <= 100; i++) {

            boolean flag = true;

            for (j = 2; j < i; j++) {
                
                if((i % j == 0)){
                    flag = false;
                    break;
                }
            }

            if(flag == true){
                System.out.println(i + "\t");
            }            
        }
    }
}
