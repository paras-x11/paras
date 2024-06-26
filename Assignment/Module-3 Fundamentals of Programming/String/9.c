// 9. Write a program in C to find the maximum number of characters in a string.

#include <stdio.h>
#include <ctype.h>

void main(){
    int i, characters=0, space=0;
    char str[100];
    
    printf("\nEnter string: ");
    gets(str);
    
    for(i=0; str[i]!='\0'; i++){
        characters++;
        if(isspace(str[i])){
            space++;
        }
        
    }

    printf("\nspace: %d", space);
    printf("\nmaximum characters(including space): %d", characters);
    
}