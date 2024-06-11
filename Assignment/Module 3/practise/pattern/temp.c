#include<stdio.h>
void main(){
    for (int r = 1; r <= 5; r++) {

        for (int c = 1; c <= 5; c++) {

            if  (r == 3 &&  c == 2) {
                printf("- ");  
            } 
            
            else {
                printf("* ");
            }
        }
        printf("\n");
    } 
}


// if (i == 1 && j == 2) {
//     // Character at row 2, column 3:
// }
// if (i == 1 && j == 2) {
// Character at row 2, column 3:
// }