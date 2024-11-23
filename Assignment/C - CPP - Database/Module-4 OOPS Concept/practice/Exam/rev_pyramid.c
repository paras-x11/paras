// * * * * * * * * *
//   * * * * * * *
//     * * * * *
//       * * *
//         *

#include <stdio.h>

void main() {
    int r, c, s;

    for(r = 4; r >= 0; r--){

        for(s = 4; s > r; s--){   
            printf("  ");
        }

        for(c = (r*2)+1; c >= 1; c--){
            printf("* ");
        }

        printf("\n");
    }
    
}