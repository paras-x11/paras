// 14. Write a program in C to combine two strings manually 

#include <stdio.h>
#include <string.h>

void main(){
    int i, a, b, c;
    char str1[100], str2[100];


    printf("Enter string 1: ");
    gets(str1);
    
    printf("\nEnter string 2: ");
    gets(str2);

    a = strlen(str1);
    b = strlen(str2);

    c = a + b;

    char combine[c + 1];
    // printf("\na=%d, b=%d\n", a, b);

    for(i=0; i<c; i++){
        
        if(i < a){
            combine[i] = str1[i];
        }
        else{
            combine[i] = str2[i - a];
        }
        // printf("%c", combine[i]);
    }

    combine[c] = '\0';              // here index start from 0 so no need to write c+1;

    printf("\nCombine string is: %s",combine);    
}



// #include <stdio.h>
// #include <string.h>

// void main(){
//     int i, j, a, b, c;
//     char str1[100], str2[100];


//     printf("Enter string 1: ");
//     gets(str1);
    
//     printf("\nEnter string 2: ");
//     gets(str2);

//     a = strlen(str1);
//     b = strlen(str2);

//     c = a + b;

//     char combine[c + 1];  

//     printf("\na = %d, b = %d\n", a, b);

//     for (i = 0; i < a; i++) {
//         combine[i] = str1[i];
//     }

//     for (j = 0; j < b; j++) {
//         combine[i + j] = str2[j];
//     }

//     combine[c] = '\0';

//     puts(combine);
// }
