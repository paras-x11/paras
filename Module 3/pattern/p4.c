//           * 
//         * * 
//       * * * 
//     * * * * 
//   * * * * * 
// * * * * * * 
//   * * * * * 
//     * * * * 
//       * * * 
//         * * 
//           * 


#include<stdio.h>
void main() {
    int r, c, s;

    for(r = 5; r >= 0; r--) { 
        for(s=0; s<r; s++){
            printf("  ");
        }

        for(c = 5; c >= r; c--) {
            printf("* ");
        }

        printf("\n");
    }

    for(r = 0; r < 5; r++) { 
        for(s=0; s<=r; s++){
            printf("  ");
        }
        
        for(c=5; c>r; c-- ){
            printf("* ");
        }

        printf("\n");
    }   
}