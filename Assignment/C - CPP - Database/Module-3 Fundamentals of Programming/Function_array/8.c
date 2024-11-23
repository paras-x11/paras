// 8. WAP to reverse a string and check that the string is palindrome or not.

#include<stdio.h>                                               // without using another string.
#include<string.h>
void main(){
    char str[50];
    int i, len=0, r=0;

    printf("\nenter string: ");
    gets(str);

    len = strlen(str);

    for(i=0; i < len/2; i++){

        if(str[i] == str[len-i-1]){
            r++;
        }
    }

    if(r == len/2){
        printf("\nstring is palindrome- %s",str);
    }
    else{
        printf("\nstring is not palindrome- %s",str);        
    }
   
}

// #include<stdio.h>                                            // without using string function, but using another string.
// #include<string.h>
// char rev[50];

// void check(char str[]){                                     
//     int i, len = 0, flag = 1;

//     for(i=0; str[i] != '\0'; i++){
//         len++;
//     }
//     printf("Length is: %d", len);

//     for(i=len; i>=0; i--){

//         rev[len - i - 1] = str[i];
    
//     }

//     for(i=0; i<len; i++){
//         if(rev[i] != str[i]){
//             flag = 0;
//         }
//     }

//     if(flag == 1){
//         printf("\n%s is palindrome.\n",str);
//     }
//     else{
//         printf("\n%s is not palindrome.\n",str);
//     } 
// }

// void main(){
//     char str1[20], str2[] = "nayan";

//     printf("\nEnter string 1: ");
//     gets(str1);

//     printf("\nstr1: %s\n",str1);
//     check(str1);

//     printf("\nstr2: %s\n",str2);
//     check(str2);
         
// }


// #include<stdio.h>                                       // using in-built string function.
// #include<string.h>
// void main(){
//     char rev[20], str[20];

//     printf("\nEnter String: ");
//     scanf("%s", &str);

//     strrev(str);
//     strcpy(rev,str);
//     printf("rev= %s\n",rev);

//     strrev(str);
//     printf("str= %s\n",str);
   
//     if( strcmp(str, rev) == 0 ){
//         printf("\npalindrome.");
//     }
//     else{
//         printf("\nnot palindrome.");
//     }
   
// }