// * * * * * * * * * 
// * *           * *
// *   *       *   * 
// *     *   *     *
// *       *       *
// *     *   *     *
// *   *       *   *
// * *           * *
// * * * * * * * * *

#include<stdio.h>
void main(){
    int r, c, s;

    for(r=10; r>=0; r--){
        
        for(c=0; c<=10; c++){
            if(r==10 || c==10 || r==0 || c==0 || r==c || r + c == 10){
                printf("* ");
            }
            else{
                printf("  ");
            }
        }
    
    printf("\n");
    }
}


