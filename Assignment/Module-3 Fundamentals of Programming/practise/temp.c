// #include<stdio.h>
// void main(){
//     for (int r = 1; r <= 5; r++) {

//         for (int c = 1; c <= 5; c++) {

//             if  (r == 3 &&  c == 2) {
//                 printf("- ");  
//             } 
            
//             else {
//                 printf("* ");
//             }
//         }
//         printf("\n");
//     } 
// }


// if (i == 1 && j == 2) {
//     // Character at row 2, column 3:
// }
// if (i == 1 && j == 2) {
// Character at row 2, column 3:
// }


// take element as input and give its position in array using function.

#include<stdio.h>
int search(int arr[], int n, int element){

    for(int i=0; i<n; i++){
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

    position = search(arr, n, element);

    if(position>=0){
        printf("\nPosition of %d is: %d",element,position);
    }
    else{
        printf("\nElement not found in array.");
    } 
}
