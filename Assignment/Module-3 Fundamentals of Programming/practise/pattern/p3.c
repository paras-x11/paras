#include<stdio.h>
void main(){
    int r,c,n=1;
    

     for(r = 0; r <= 5; r++) { 

        for(c = 5; c >= r; c--){
            printf("%d ",n++ );
            
        }
        n=1;
        printf("\n");
    }

   
}