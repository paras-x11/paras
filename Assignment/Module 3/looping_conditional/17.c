//17. Calculate 5 numbers from user and calculate number of even and odd using of while loop 

#include<stdio.h>
void main(){
    int n=0, num[5], even=0, odd=0;

    while(n<5){
        printf("\nEnter number %d: ",n+1);
        scanf("%d",&num[n]);

        if(num[n] % 2 == 0){
            even ++;
        }
        else{
            odd ++;
        }
        n++;
    }

    printf("\n-> Even numbers: %d\n",even);
    printf("\n-> odd numbers: %d\n",odd);
   
}