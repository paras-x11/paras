///5. WAP to print factorial of given number.

// 5 = 1*2*3*4*5 = 120

#include<stdio.h>
void main(){
    int n;
    int i=1;
    int fact=1; 

    printf("\nEnter the number: ");
    scanf("%d",&n);

    do
    {
        fact = fact * i;
        i++;
    } while (i<=n);
    
    printf("\nFactorial is: %d",fact);

}


/*
#include<stdio.h>
void main(){
    int n;
    int i=1;
    int fact = 1;

    printf("\nEnter the number: ");
    scanf("%d",&n);

    while(i<=n){
        fact = fact * i;
        i++;
    }
    printf("\nFactorial is: %d",fact);
    
}
*/

/*
#include<stdio.h>
void main(){
    int i,n;
    int fact=1;

    printf("\nEnter the number: ");
    scanf("%d",&n);

    for(i=1 ; i<=n; i++){
        fact = fact * i;
        
    }
    printf("\nFactorial is: %d",fact);
}*/


