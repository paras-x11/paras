/*2. Write a C program to read the value of an integer m and display the value of n is 1 when m is larger than 0, 
     n = 0 when m is 0 and n = -1 when m is less than 0.
*/

#include<stdio.h>
void main(){
    int m, n;
    
    printf("Enter the value of m: ");
    scanf("%d",&m);

    if(m > 0){
        n = 1;
        printf("n = %d",n);
    }
    
    else if(m < 0){
        n = -1;
        printf("n = %d",n);
    }

    else{
        n = 0;
        printf("n = %d",n);
    }
}