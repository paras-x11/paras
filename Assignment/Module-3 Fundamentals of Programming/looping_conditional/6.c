// //6. WAP to print Fibonacci series up to given numbers 

//fibonacci series: 0,1,1,2,3,5,8,13,21,.....



#include<stdio.h>
void main(){
    int a=0,b=1,temp,n,count=1;

    printf("\nenter number: ");
    scanf("%d",&n);

    printf("%d\t%d\t",a,b);
    
    while (count<=n)
    {

        temp = a + b;
        a = b;
        b = temp;

        count++;

        printf("%d\t",temp);
    }
}


/*
#include<stdio.h>
void main(){
    int a=0,b=1,temp,n,count;

    printf("\nenter number");
    scanf("%d",&n);

    printf("%d\t%d\t",a,b);

    for(count=1; count<=n; count++){
        temp =a + b;
        a = b;
        b = temp;
        printf("%d\t",temp);
    }
   
}
*/