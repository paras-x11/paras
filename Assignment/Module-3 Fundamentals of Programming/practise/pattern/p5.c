#include<stdio.h>
void main(){
    int r, c, s, n=1;

    for(r=0; r<=5; r++){
        
        for(s=5; s>=r; s--){
            printf(" ");
        }

        for(c=0; c<=r; c++){            
           printf("* ");
        }

        printf("\n");
    }
}



// #include<stdio.h>
// void main(){
//     int r, c, s, n=1;

//     for(r=0; r<=5; r++){
//         for(s=5; s>=r; s--){
//             printf("  ");
//         }

//         for(c=1; c<=r; c++){
//             printf("%d ",c);
//         }

//         for(c=r-1; c>=1; c--){
            
//             printf("%d ",c);
//         }
//         n++;
//         printf("\n");
//     }
   
// }


//      *
//     * *
//    *   *
//   *     *
//  * * * * *