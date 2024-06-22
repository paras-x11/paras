// 8. WAP to reverse a string and check that the string is palindrome or not.

// #include<stdio.h>
// char rev[50];

// void check(char str[]){                                     // without using string function.
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

#include<stdio.h>
void main(){
    char rev[20], str[20] = "nayan";

    strrev(str);
    strcpy(rev,str);
    printf("%s\n",rev);
    strrev(str);
   
    int flag = 1;
    for(int i=0; str[i] != '\0'; i++){
        if(rev[i] != str[i]){
            flag=0;
        }
    }

    if(flag==1){
        printf("\npalindrome.");
    }
    else{
        printf("\nnot palindrome.");
    }
   
}