// 5. Write a program in C to compare two strings without using string library functions.

#include <stdio.h>
#include <string.h>

void main(){
    int i, flag=1;
    char str1[100], str2[100];
    
    printf("\nEnter string 1: ");
    gets(str1);
    
    printf("\nEnter string 2: ");
    gets(str2);
    
    for(i=0; str1[i]!='\0' && str2[i]!='\0'; i++){
        
        if(str1[i] != str2[i]){
            flag = 0;
            break;
        }
        else{
            flag = 1;
        }
    }
    
    if(flag == 1 && str1[i] == '\0' && str2[i] == '\0'){            // for check both string have same length or end.

        printf("\nString 1 is same as string 2.");
    }
    else{
        printf("\nString 1 is not same as string 2.");
    }
}