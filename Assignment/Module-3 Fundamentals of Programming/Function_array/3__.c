// 3. WAP to find reverse of string using recursion.

#include<stdio.h>
#include<string.h>

void reverse(char* str, int len, int i, int temp){

    if(i < len){

        temp = str[i];
        str[i] = str[len - 1];
        str[len - 1] = temp;
        i++;
        len--;
        reverse(str, len, i, temp);
    }
}

void main(){

    char str[100];

    printf("Enter String: ");
    gets(str);

    int len = strlen(str);

    reverse(str, len, 0, 0);

    printf("%s",str);
      
}