//    1
//   12
//  123
// 1234
//12345

#include<stdio.h>
int main(){
    int r,c,s;

    for(r=1; r<=5; r++){

        for(s=4; s>=r; s--){
            printf(" ");
        }
        for(c=1;c<=r;c++){
            printf("%d ",c);
        }
        
    printf("\n");
    }
}