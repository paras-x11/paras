//22. Accept 3 numbers from user using while loop and check each numbers palindrome.

#include<stdio.h>
void main(){
    int num[3], rev[3], rem, temp;

    for(int n=0; n<3; n++){
        printf("\nEnter number %d: ",n+1);
        scanf("%d",&num[n]);

        temp = num[n];
        rev[n] = 0;

        while(temp > 0){
            rem = temp % 10;
            rev[n] = rev[n]*10 + rem;
            temp = temp / 10;
        }
    }

    for(int n=0; n<3; n++){
        printf("\n");
        printf("\n-> Number is: %d \n-> Revers is: %d",num[n], rev[n]);

        if(num[n] == rev[n]){
            printf("\n-> Palindrome.");
        }
        else{
            printf("\n-> Not Palindrome.");
        }
    }

}