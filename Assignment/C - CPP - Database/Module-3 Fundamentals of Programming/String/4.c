// 4. Write a program in C to count the total number of words in a string.

#include <stdio.h>
#include <ctype.h>
#include <string.h>

void main(){
    int i, len=0, words=1;
    char str[100];
    
    printf("\nEnter string: ");
    gets(str);
    
    for(i=0; str[i] != '\0'; i++){
        len++;
    }
    
    // len = strlen(str);
    // printf("\nLength is: %d\n",len);
    
    for(i=0; i<len; i++){
        
        if(isspace(str[i])){
            printf("\n");
            words++;
        }
        else{
            printf("%c", str[i]);
        }
    }
    
    printf("\ntotal number of words in a string is: %d\n", words);
}
