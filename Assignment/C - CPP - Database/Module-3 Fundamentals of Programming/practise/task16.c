//task 16: 1.WAP to read n number of values in an array and display them in reverse order.       ex: 2,5,7 o/p: 7,5,2;

//2. WAP to find the sum of all elements of the array.    ex: 2,3,5 o/p:10

#include<stdio.h>
void main(){
    int i, n, sum=0;

    printf("\nEnter the range of array: ");
    scanf("%d",&n);
    int arr[n];

    printf("\nEnter %d element: ",n);
    for(i=0; i<n; i++){
        scanf("%d",&arr[i]);
    }

    printf("\nYour Array is: \n");
    for(i=0; i<n; i++){
        printf("  %d\t",arr[i]);
    }

    // printf("\nReversed Array is: \n");
    // for(i=n-1; i>=0; i--){
    //     printf("  %d\t",arr[i]);
    // } 

    printf("\nReversed Array is: \n");
    for(i=1; i<=n; i++){
        printf("  %d\t",arr[n-i]);
    }

    for(i=0; i<n; i++){
        sum += arr[i]; 
    } 
    printf("\n\nSum of all Array element is: %d",sum);
}