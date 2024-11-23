#include<stdio.h>
#include<stdlib.h>
int row,col, element;

void search(int arr[][col],int row, int col, int element){
    int r, c, found=0;
    for(r=0; r<row; r++){
        for(c=0; c<col; c++){
            if(arr[r][c] == element){
               printf("Element %d not found at arr[%d][%d]\n",element,r,c);
               found=1;
            }
        }
    } 
    if (!found) {
        printf("Element %d not found in the array.\n", element);
    }
}

int main(){
    int r, c, ch;

    printf("\nEnter row: ");
    scanf("%d", &row);

    printf("\nEnter column: ");
    scanf("%d", &col);

    int arr1[row][col], arr2[row][col], sum[row][col], sub[row][col];

    printf("\nEnter elemnets for array 1: ");               // enter array 1.
    for(r=0; r<row; r++){
        for(c=0; c<col; c++){
            printf("\nEnter [%d][%d]: ",r, c);
            scanf("%d",&arr1[r][c]);
        }
    }
    
    printf("\nEnter elemnets for array 2: ");               // enter array 2.
    for(r=0; r<row; r++){
        for(c=0; c<col; c++){
            printf("\nEnter [%d][%d]: ",r, c);
            scanf("%d",&arr2[r][c]);
        }
    }

    printf("\nArray 1: \n");                // display array 1.
    for(r=0; r<row; r++){
        for(c=0; c<col; c++){
            printf("arr[%d][%d]: %d\t",r, c, arr1[r][c]);
        }printf("\n");
    }
    
    printf("\nArray 2: \n");                // display array 2.
    for(r=0; r<row; r++){
        for(c=0; c<col; c++){
            printf("arr[%d][%d]: %d\t",r, c, arr2[r][c]);
        }printf("\n");
    }
    
    while(1){
    printf("\n-----------------------------------------");
    printf("\nEnter 1 for search element in array 1.");
    printf("\nEnter 2 for search element in array 2.");
    printf("\nEnter 3 for sum.");
    printf("\nEnter 4 for subtraction.");
    printf("\nEnter 0 for exit.");
    
    printf("\nEnter your choice: ");
    scanf("%d",&ch);
    
    switch(ch){
        case 1: printf("\nEnter Element to search in array 1: ");
                scanf("%d",&element);
                
                search(arr1, row, col, element); 
                break;
    
        case 2: printf("\nEnter Element to search in array 2: ");
                scanf("%d",&element);
                
                search(arr2, row, col, element); 
                break;
                
        case 3: printf("\nSum is: \n");
                    for(r = 0; r < row; r++) {
                        for(c = 0; c < col; c++) {
                            sum[r][c] = arr1[r][c] + arr2[r][c];
                            printf("%d\t", sum[r][c]);
                        }
                        printf("\n");
                    }
                    break;
            
            case 4: printf("\nSubtraction is: \n");
                    for(r = 0; r < row; r++) {
                        for(c = 0; c < col; c++) {
                            sub[r][c] = arr1[r][c] - arr2[r][c];
                            printf("%d\t", sub[r][c]);
                        }
                        printf("\n");
                    }
                    break;
                
        case 5:
                break;
        
        case 0: printf("\nExited."); exit(0);
        
        default: printf("\nEnter Valid choice. \n"); break;
    }
    }
    
    return 0;
}