//task9:
//5 5 5 5 5
//  4 4 4 4
//    3 3 3
//      2 2
//        1

#include<stdio.h>
void main(){
    int r, c, s, n=6;

    for(r=0; r<=5; r++){
        for(s=0; s<r; s++){
            printf("  ");
        }

        for(c=5; c>=r; c--){
            printf("%d ",n);
        }
    n--;
    printf("\n");
    }
   
}