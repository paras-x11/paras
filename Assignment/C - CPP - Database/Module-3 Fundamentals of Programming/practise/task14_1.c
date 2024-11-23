//task 14:
//1. write a user defined function to print the multiplication table of the given number.

#include<stdio.h>

void show(){
    int a, b, n, m;
    printf("\nEnter whose table you want: ");
    scanf("%d",&n);

    printf("\nEnter multiplier: ");
    scanf("%d",&m);

    for(int i=1; i<=m; i++){
        
        printf("\n%d * %d = %d",n,i,n*i);
    }

}

void main(){
   show();
}
