// 14. Perform 2D matrix array 

#include<stdio.h>
int size;
int search(int arr[size][size],int size, int element){
    int r, c, found=0;

    for(r=0; r<size; r++){
        for(c=0; c<size; c++){
            if(arr[r][c] == element){
               printf("arr[%d][%d]",r,c);
               // return arr[r][c];
            }
        }
    }
    return -1;
}

void main(){
    int r, c, element, position;

    printf("\nEnter size: ");
    scanf("%d", &size);

    // printf("\nEnter column: ");
    // scanf("%d", &col);

    int arr1[size][size];

    printf("\nEnter elemnets for array 1: ");               // enter array 1.
    for(r=0; r<size; r++){
        for(c=0; c<size; c++){
            printf("\nEnter [%d][%d]: ",r, c);
            scanf("%d",&arr1[r][c]);
        }
    }

    // printf("\nEnter elemnets for array 2: ");               // enter array 2.
    // for(r=0; r<row; r++){
    //     for(c=0; c<col; c++){
    //         printf("\nEnter [%d][%d]: ",r, c);
    //         scanf("%d",&arr2[r][c]);
    //     }
    // }

    printf("\nArray 1: \n");                // display array 1.
    for(r=0; r<size; r++){
        for(c=0; c<size; c++){
            printf("arr[%d][%d]=[%d]\t",r, c, arr1[r][c]);
        }printf("\n");
    }

    // printf("\nArray 2: \n");                // display array 2.
    // for(r=0; r<row; r++){
    //     for(c=0; c<col; c++){
    //         printf("%d\t",arr2[r][c]);
    //     }printf("\n");
    // }

    printf("\nEnter Element to search in array 1: ");
    scanf("%d",element);

    //position =
     search(arr1[size][size], size, element);
    

    // if(position != -1){
    //     printf("\n%d is found at position: %d",element,position);
    // }
    // else{
    //     printf("\n%d is not found.",element);
    // }  
}
