//2. WAP to accept 5 numbers from user and display all numbers.

#include<stdio.h>
void main(){
    int a,b,c,d,e;

    printf("\nEnter Number 1: ");
    scanf("%d",&a);

    printf("\nEnter Number 2: ");
    scanf("%d",&b);

    printf("\nEnter Number 3: ");
    scanf("%d",&c);

    printf("\nEnter Number 4: ");
    scanf("%d",&d);

    printf("\nEnter Number 5: ");
    scanf("%d",&e);

    printf("\n1st nuber is: %d",a);
    printf("\n2nd nuber is: %d",b);
    printf("\n3rd nuber is: %d",c);
    printf("\n4th nuber is: %d",d);
    printf("\n5th nuber is: %d",e);
}


/*
#include<stdio.h>
void main(){
    int n, number[5];

    for(n = 1 ; n <= 5 ; n++){
        printf("\nEnter number %d: ",n);
        scanf("%d",&number[n]);
    } 

    for(n = 1 ; n <= 5 ; n++){
        printf("\nyou entered: %d",number[n]);
    }  
}
*/

