// 11. WAP to accept 5 numbers from user and display in reverse order using for loop and array.

#include<stdio.h>
#include<string.h>
void main(){
    int i, arr[5];

    printf("\nEnter elements of array: ");
    for(i=0; i<5; i++){
        scanf("%d",&arr[i]);
    }

    printf("\n-> Array elements are: \n");                //display Array 1.
    for(i=0; i<5; i++){
            printf("   %d\t", arr[i]);
    }

    printf("\n-> Array elements in reverse order are: \n");                //display reversed Array.
    for(i=0; i<5; i++){
            printf("   %d\t", arr[4-i]);
    }

    printf("\n-> Array elements in reverse order are: \n");                //display reversed Array.
    for(i=4; i>=0; i--){
            printf("   %d\t", arr[i]);
    }
}


