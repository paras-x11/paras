// task 15:
// 2. wap to accept 2 number & find the GCD using loop of 2 numbers.

//        2 |24            2 | 36                               2 | 24 | 36
//        2 |12            2 | 18                               2 | 12 | 18
//        2 | 6            3 |  9                               2 |  6 |  9
//        3 | 3            3 |  3                               3 |  3 |  9
//          | 1              |  1                               3 |  1 |  3
//                                                                |    |  1

// GCD of 24 and 36 is 2 × 2 × 3 = 12               // LCM of 24 and 36 is 2 x 2 x 2 x 3 x 3 = 72

// GCD (a,b) = (a*b) / lcm(a,b);                    // LCM (a,b) = |a*b| / GCD(a,b);

#include<stdio.h>
void main(){
    int a , b, gcd=1, lcm;

    printf("\nEnter a: ");
    scanf("%d",&a);
    
    printf("\nEnter b: ");
    scanf("%d",&b);

    for(int i=1; i<=a && i<=b ; i++){

        if(a % i == 0 && b % i == 0){
            
            gcd = i;
            // printf("%d\t",i);
        }
    }

    lcm = (a*b) / gcd;

    printf("\nGCD of %d and %d is: %d",a,b,gcd);   

    printf("\n\nLCM of %d and %d is: %d",a,b,lcm);   
}

