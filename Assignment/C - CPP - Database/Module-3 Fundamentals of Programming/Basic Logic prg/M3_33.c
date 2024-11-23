//M3_33 C Program to Read Integer and Print First Three Powers (N^1, N^2, N^3).

#include<stdio.h>
#include<math.h>
void main(){
    int a, a1, a2, a3;

    printf("\nEnter the number: ");
    scanf("%d",&a);
    
    /*
    a1 = a;
    printf("\n1st power of number n^1 is: %d",a1);

    a2 = a * a;
    printf("\n2nd power of number n^2 is: %d",a2);

    a3 = a * a * a;
    printf("\n3rd power of number n^3 is: %d",a3);
    */
    
    a1 = pow(a,1);
    printf("\n1st power of number n^1 is: %d",a1);

    a2 = pow(a,2);
    printf("\n2nd power of number n^2 is: %d",a2);

    a3 = pow(a,3);
    printf("\n3rd power of number n^3 is: %d",a3);
    
}




