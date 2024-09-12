// 1. wap to copy string from one string to another string without using string func.

#include <stdio.h>
#include <string.h>

int main(){

    int i;
    char str1[50], str2[50];
    
    printf("Enter String 1: ");
    scanf("%s", &str1);

    for(i=0; str1[i] != '\0'; i++){
        str2[i] = str1[i];
    }

    printf("\nString 2 is: %s", str2);

}