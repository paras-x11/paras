// take element as input and give its position in array.

#include<stdio.h>

int search(int arr[], int size, int element){

    for(int i=0; i<size; i++){
        if(arr[i] == element){
            return i;
            break;
        }
    }
    // return -1;     //instead of break;
}

int main(){
    int i, n,element, position;

    printf("\nEnter the range of array: ");
    scanf("%d",&n);
    int arr[n];

    printf("\nenter %d elements: ",n);
    for(i=0; i<n; i++){
        scanf("%d",&arr[i]);
    }

    printf("\nYour Array is: ");
    for(i=0; i<n; i++){
        printf("%d\t",arr[i]);
    }

    printf("\nenter element: ");
    scanf("%d",&element);

    for(i=0; i<n; i++){
        if(arr[i] == element){
            position = i;
            break;
        }
    }

    // position = search(arr, n, element);       // for function

    if(position>=0){
        printf("\nPosition of %d is: %d",arr[i],i);
    }
    else{
        printf("\nElement not found in array.");
    } 
}