// 12. Program of Armstrong Number in C Using For Loop & While Loop 
// 1, 153 -> 1^3 + 5^3 + 3^3, 370, 371, 407

#include<stdio.h>
#include<math.h>
void main(){
    int n, sum=0, temp, rem;

    printf("Enter number: ");
    scanf("%d",&n);

    n = abs(n);
    temp = n;

    while(n != 0){
        rem = n % 10;
        sum += rem * rem * rem;
        n = n / 10;
    }

    if(sum==0){
        printf("\n-> you entered zero.");
    }
    else if(temp==sum){
        printf("\nSUm is: %d\n",sum);
        printf("\n-> %d is armstrong Number.",temp);
    }
    else{
        printf("\nSUm is: %d\n",sum);
        printf("\n-> %d is not armstrong Number.",temp);   
    }

   
}