// 14. Perform 2D matrix array 
#include <stdio.h>
#include<stdlib.h>

int r, c, row, col, element;

void search(int arr[][col], int row, int col, int element){
    int flag=0;
    
    for(r=0; r<row; r++){
        for(c=0; c<col; c++){
            if(arr[r][c] == element){
                printf("\n-> %d is found at position [%d][%d]\n",element, r, c);
                flag = 1;
            }
        }
    }
    if(!flag){
        printf("\n-> %d is not found in array.\n",element);
    }
}
int main(){
    int ch;
    
    printf("\nenter row: ");
    scanf("%d",&row);
    printf("\nenter column: ");
    scanf("%d",&col);
    
    int arr1[row][col], arr2[row][col], mul[row][col];
    
    printf("\nenter element for array 1: ");                // enter array 1
    for(r=0; r<row; r++){
        for(c=0; c<col; c++){
            scanf("%d",&arr1[r][c]);
        }
    }
    
    printf("\nenter element for array 2: ");                // enter array 2
    for(r=0; r<row; r++){
        for(c=0; c<col; c++){
            scanf("%d",&arr2[r][c]);
        }
    }
    
    printf("\narray 1: \n");                        // display array 1
    for(r=0; r<row; r++){
        for(c=0; c<col; c++){
            printf("%d\t",arr1[r][c]);
        }printf("\n");
    }
    
    printf("\narray 2: \n");                        // display array 2
    for(r=0; r<row; r++){
        for(c=0; c<col; c++){
            printf("%d\t",arr2[r][c]);
        }printf("\n");
    }
    
    while(1){
    printf("\n1 for search in array 1.\n2 for search in array 2.\n3 for sum.\n");
    printf("4 for substraction\n5 for multiplication\n6 for transpose both array.\n0 for exit.\n");
    printf("\nenter your choice: ");
    scanf("%d",&ch);
    
    switch(ch){
        case 1:
            printf("\nEnter element to search in array 1: ");
            scanf("%d",&element);
            search(arr1, row, col, element);
        break;
        
        case 2:
            printf("\nEnter element to search in array 2: ");
            scanf("%d",&element);
            search(arr2, row, col, element);
        break;
            
        case 3:
            printf("\nSum is: \n");
            for(r=0; r<row; r++){
                for(c=0; c<col; c++){
                    printf("%d\t",arr1[r][c] + arr2[r][c]);
                }printf("\n");
            }
        break;
        
        case 4:
            printf("\nSubstraction is: \n");
            for(r=0; r<row; r++){
                for(c=0; c<col; c++){
                    printf("%d\t",arr1[r][c] - arr2[r][c]);
                }printf("\n");
            }
        break;
        
        case 5:
            if(row==col){
                printf("\nMultiplication is: \n");
                for(r=0; r<row; r++){
                    for(c=0; c<col; c++){
                        mul[r][c] = 0;
                        for(int k=0; k<col; k++){
                            mul[r][c] += arr1[r][k] * arr2[k][c];
                        }
                        printf("%d\t",mul[r][c]);
                    }printf("\n");
                }
            }else{
                printf("\n-> matrix multiplication not possible.\n");
            }
        break;
        
        case 6:
            printf("\nTransposing array 1: \n");
            for(c=0; c<col; c++){
                for(r=0; r<row; r++){
                    printf("%d\t",arr1[r][c]);
                }printf("\n");
            }
            printf("\nTransposing array 2: \n");
            for(c=0; c<col; c++){
                for(r=0; r<row; r++){
                    printf("%d\t",arr2[r][c]);
                }printf("\n");
            }
        break;
        
        case 0: printf("\n-> Exited.\n"); exit(0);
        
        default: printf("\n-> enter valid choice.\n");
            
            
    }
    }
}


