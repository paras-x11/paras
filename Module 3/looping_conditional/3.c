// 3. WAP to take 10 no. Input from user find out below values 
// a. How many Even numbers are there 
// b. How many odd numbers are there 
// c. Sum of even numbers 
// d. Sum of odd numbers 

#include<stdio.h>
void main(){
    int n;
    int even_count=0, odd_count=0;
    int even_sum=0, odd_sum=0;

    for(int i = 1 ; i <= 10 ; i++){

    printf("\nEnter Number %d: ",i);
    scanf("%d",&n);

        if(n%2==0){
            even_count++;
            even_sum = n + even_sum;
        }
        
        else{
            odd_count++;
            odd_sum = n + odd_sum;
        }
    }
    
    printf("\ntotal even numbers: %d",even_count);
    printf("\nsum of even numbers: %d",even_sum);
    printf("\ntotal odd numbers: %d",odd_count);
    printf("\nsum of odd numbers: %d",odd_sum);
}

