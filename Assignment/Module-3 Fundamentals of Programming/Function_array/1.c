// 1. Write a program to find out the max number from given array using function 

#include<stdio.h>
int findMax(int arr[], int size){
    
    int max = arr[0];
    
    for(int i=1; i<size; i++){

        if(arr[i] > max){
            max = arr[i];
        } 
    }
    return max;
}

void main(){
    
    int arr[5] = {19,28,45,89,22};

    int size = sizeof(arr) / sizeof(arr[0]);

    // sizeof(arr): gives you the total size of the array in bytes (e.g., 28 bytes for an array of 7 ints)
    // sizeof(arr[0]): gives you the size of a single element in the array (e.g., 4 bytes for an int)
    // sizeof(arr) / sizeof(arr[0]): gives you the number of elements in the array (e.g., 28 bytes / 4 bytes per element = 7 elements)

    int max = findMax(arr, size);

    printf("The maximum number in the array is: %d\n", max);
}


