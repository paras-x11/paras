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


#include<stdio.h>
#include<stdlib.h>

int main(){
    int p;
    char ch;

    start:
    printf("\nEmter value: ");
    scanf("%d",&p);

    printf("\np * 2 = %d",p*2);

    while ((getchar()) != '\n'); // This consumes all characters in the input buffer until a newline


    printf("\nDo You Want To Place More Order: y or n: ");
    scanf(" %c", &ch);

    if(ch == 'y' || ch == 'Y'){

        goto start;
    
    }
    
    else{
        printf("\nexited.");
    }
    return 0;
}