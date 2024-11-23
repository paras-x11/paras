//task7
//EEEEE
//DDDD
//CCC
//BB
//A 

#include<stdio.h>
void main(){
    int r, c;
    char ch = 'E';

    for(r=1; r<=5; r++){
        for(c=5; c>=r; c--){
            printf("%c ",ch);
        }
    ch--;
    printf("\n");
    }
   
}