//task6
// A B C D E
// A B C D
// A B C
// A B
// A

#include<stdio.h>
void main(){
    int r, c, s;
    char ch='A';

    for(r=0; r<=5; r++){
        for(c=5; c>=r; c--){
            printf("%c ",ch++);
        }
        ch='A';
        printf("\n");
    }
   
}