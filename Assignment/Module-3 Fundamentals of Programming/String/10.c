// 10. Write a program in C to extract a substring from a given string.


#include <stdio.h>                              // dynamic input
#include <string.h>

void main(){
    int i, len = 0, start, end;
    char str[100];
    
    printf("\nEnter string: ");
    gets(str);
    
    len = strlen(str);
    
    printf("\nEnter postion to Start: ");
    scanf("%d", &start);
    
    printf("\nEnter postion to end(maximum end is %d): ",len);
    scanf("%d", &end);
    
    char str1[end-start+1];
    
    if(start>=0 && end<=len){
        for(i=0; start<=end ; i++){
            
            str1[i] = str[start];
            start++;
        }
        str1[i] = '\0';
        puts(str1);
    }
    else{
        printf("\ninvalid position.");
    }
    
}


// #include <stdio.h>                                  // static input
// #include <string.h>

// void main(){
//     int i, len = 0, start, end;
//     char str[100] = "I Love India";
//     printf("%s", str);
    
//     len = strlen(str);
    
//     printf("\nEnter postion to Start: ");
//     scanf("%d", &start);
    
//     printf("\nEnter postion to end(default end is %d): ",len);
//     scanf("%d", &end);
    
//     char str1[end - start +1];
    
//     if(start>=0 && end<=len){
//         for(i=0; start<=end ; i++){
            
//             str1[i] = str[start];
//             start++;
//         }str[i]='\0';
//     }
//     else{
//         printf("\ninvalid position.");
//     }
    
//     printf("%s", str1);
    
// }
