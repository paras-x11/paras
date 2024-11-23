// 3. WAP to find reverse of string using recursion.

// #include<stdio.h>
// #include<string.h>
// void reverse(char* str, int len, int i, int temp){

//     if(i<len){
//         temp = str[i];
//         str[i] = str[len-1];
//         str[len-1] = temp;
//         i++;
//         len--;
//         reverse(str,len,i,temp);
//     }
// }

// void main(){
//     char str[10] = "paras";

//     int len = strlen(str); 
//     printf("%d",strlen(str));

//     reverse(str,len,0,0);

//     printf("\nReverse = %s",str);

// }


// sorting array ascending:

// #include<stdio.h>
// void main(){

//     int a1[5] = {9,3,7,12,6};
//     int i, j, temp;

//     for(i=0; i<5; i++){
//                 for(j=0; j<5; j++){

//                     if(a1[i] < a1[j]){                 //if(a1[i] < a1[j]) for decsending.
//                         temp = a1[i];
//                         a1[i] = a1[j];
//                         a1[j] = temp;
//                     }
//                 }
//             }
//             printf("\n-> acsending array1: ");
//             for(i=0; i<5; i++){
//                 printf("\t%d",a1[i]);
//             }
//     }




// 4. WAP to find factorial using recursion 

// #include<stdio.h>
// int factorial(int n){

//     if(n<=1){
//         return 1;
//     }
//     else{
//         return n*factorial(n-1);
//     }
    
// }

// void main(){
//     int n;

//     printf("\nEnter n: ");
//     scanf("%d",&n);
    
//     printf("\nFactorial = %d",factorial(n));
   
// }

// multiplication of 2d array:
// #include<stdio.h>
// void main(){

//     int row, col, i, j, result[2][2];

//     int arr1[2][2] = {{1,2}, {4,5}};
//     int arr2[2][2] = {{2,3}, {6,4}};


//     printf("\n-> Array 1: \n");                //display Array 1.
//     for(i=0; i<2; i++){
//         for(j=0; j<2; j++){
//             printf("   %d\t", arr1[i][j]);
//         }
//         printf("\n");
//     }

//     printf("\n-> Array 2: \n");                //display Array 2.
//     for(i=0; i<2; i++){
//         for(j=0; j<2; j++){
//             printf("   %d\t", arr2[i][j]);
//         }
//         printf("\n");
//     }
    
//     for(i=0; i<2; i++){
//         for(j=0; j<2; j++){
//             result[i][j]=0;
//             for(int k=0; k<2; k++){
//                 result[i][j] += arr1[i][k] * arr2[k][j];
//             }
//         }
//     }

//     printf("\n-> Multiplication of this 2 arrays is: \n");                //display Multiplication.
//     for(i=0; i<2; i++){
//         for(j=0; j<2; j++){
//             printf("   %d\t", result[i][j]);
//         }
//         printf("\n");
//     }
// } 


// 14. Perform 2D matrix array 

#include<stdio.h>
#include<stdlib.h>
void main(){
    int row, col, r, c, element, position, flag;

    printf("\nEnter row: ");
    scanf("%d",&row);
    printf("\nEnter column: ");
    scanf("%d",&col);
    
    int arr1[row][col] ;

    printf("\nEnter element in array 1: \n");                // enter array 1.
    for(r=0; r<row; r++){
        for(c=0; c<col; c++){
            scanf("%d",&arr1[r][c]);
        }
    }
    
    printf("\nArray 1: \n");                                // display array 1.
    for(r=0; r<row; r++){
        for(c=0; c<col; c++){
            printf("%d\t",arr1[r][c]);
        }printf("\n");
    }
        
    printf("\nEnter Element to search in array 1: ");
    scanf("%d",&element);

    for(r=0; r<row; r++){
        for(c=0; c<col; c++){
            if(arr1[r][c] == element){
                printf("\n%d is found at position [%d][%d]",element, r, c);
                flag=1;
            }
        }
    }

    if(flag != 1){
        printf("\n%d is not found.",element);
    }
}
