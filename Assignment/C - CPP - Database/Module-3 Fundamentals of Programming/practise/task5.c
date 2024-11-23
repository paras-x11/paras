// task5
// 1 2 3 4 5
//   1 2 3 4
//     1 2 3
//       1 2
//         1

#include<stdio.h>
void main(){
    int r,c,s,n=1;

    for(r=0; r<=5; r++){
        for(s=0; s<r; s++){
            printf("  ");
        }

        for(c=5; c>=r; c--){
            printf("%d ",n++);
        }
    n=1;
    printf("\n");
    }
   
}
