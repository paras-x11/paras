// 13. WAP to accept 5 numbers from user and check entered number is even or odd using of array 

#include<stdio.h>
void main(){
    int i, arr[5];
   
    printf("\nEnter 5 element.");
    for(i=0; i<5; i++){
        printf("\nEnter number %d: ",i+1);
        scanf("%d",&arr[i]);
    }

    printf("\nYour array is: \n");
    for(i=0; i<5; i++){
        printf("%d\t ",arr[i]);
    }

    for(i=0; i<5; i++){
        if(arr[i] % 2 == 0){
            printf("\n%d is even",arr[i]);
        }
        else{
            printf("\n%d is odd",arr[i]);
        }
    }
}