// 6. WAP to make addition, Subtraction and multiplication of two matrix using 2-D Array

#include<stdio.h>
void main(){
    int row, col, i, j, arr1[20][20], arr2[20][20], sum[20][20], sub[20][20], mul[20][20];

    printf("\nEnter the raw: ");
    scanf("%d",&row);

    printf("\nEnter the column: ");
    scanf("%d",&col);

    printf("\nEnter element for array 1: ");                //enter element for Array 1.
    for(i=0; i<row; i++){
        for(j=0; j<col; j++){
            scanf("%d", &arr1[i][j]);
        }
    }

    printf("\nEnter element for array 2: ");                //enter element for Array 2.
    for(i=0; i<row; i++){
        for(j=0; j<col; j++){
            scanf("%d", &arr2[i][j]);
        }
    }

    printf("\n-> Array 1: \n");                //display Array 1.
    for(i=0; i<row; i++){
        for(j=0; j<col; j++){
            printf("   %d\t", arr1[i][j]);
        }
        printf("\n");
    }

    printf("\n-> Array 2: \n");                //display Array 2.
    for(i=0; i<row; i++){
        for(j=0; j<col; j++){
            printf("   %d\t", arr2[i][j]);
        }
        printf("\n");
    }
    
    for(i=0; i<row; i++){
        for(j=0; j<col; j++){
            sum[i][j] = arr1[i][j] + arr2[i][j];
        }
    }

    printf("\n-> Sum of this 2 arrays is: \n");                //display Sum.
    for(i=0; i<row; i++){
        for(j=0; j<col; j++){
            printf("   %d\t", sum[i][j]);
        }
        printf("\n");
    }

    for(i=0; i<row; i++){
        for(j=0; j<col; j++){
            sub[i][j] = arr1[i][j] - arr2[i][j];
        }
    }

    printf("\n-> Subtraction of this 2 arrays is: \n");                //display Substraction.
    for(i=0; i<row; i++){
        for(j=0; j<col; j++){
            printf("   %d\t", sub[i][j]);
        }
        printf("\n");
    }

    if(row == col){
        for(i=0; i<row; i++){
            for(j=0; j<col; j++){
                mul[i][j]=0;

                for(int k=0; k<col; k++){
                    mul[i][j] += arr1[i][k] * arr2[k][j];
                }
            }
        }

        printf("\n-> Multiplication of this 2 arrays is: \n");                //display Multiplication.
        for(i=0; i<row; i++){
            for(j=0; j<col; j++){
                printf("   %d\t", mul[i][j]);
            }
            printf("\n");
        }
    }
}