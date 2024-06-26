// 3. Write a program in C to print individual characters of a string in reverse order.

#include <stdio.h>
#include <string.h>
void main(){
    int i, len=0;
    char str[100];
    
    printf("\nEnter string: ");
    gets(str);
    
    for(i=0; str[i] != '\0'; i++){
        len++;
    }
    
    printf("\nLength is: %d\n",len);
    
    printf("\nindividual characters of a string in reverse order: \n");
    for(i=0; i<=len; i++){
        printf("%c ",str[len - i]);
    }
    
    printf("\n");
    for(i=len; i>=0; i--){
        printf("%c",str[i]);
    }
}