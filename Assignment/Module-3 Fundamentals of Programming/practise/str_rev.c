// reverse string without in-built function strrev();

#include<stdio.h>

void reverse(char str[]){
    
    char rev;
    int i, end = 0;

    for(i=0; str[i] != '\0'; i++){
        end++;
    }
    printf("Length is: %d", end);

    for(i=0; i<=end; i++, end--){

            rev = str[end-1];
            str[end-1] = str[i];
            str[i] = rev;
    
    }
    printf("\nReverse string is: %s\n", str);


}
void main(){
    char str1[20], str2[] = "hello";

    printf("\nEnter string 1: ");
    gets(str1);

    printf("\nstr1: %s\n",str1);
    reverse(str1);

    printf("\nstr2: %s\n",str2);
    reverse(str2);
      
}


// #include<stdio.h>                     //can't check palindrome

// void reverse(char str[]){

//     char rev[20];
//     int len = 0, i, j;

//     for(i=0; str[i] != '\0'; i++){
//         len++;
//     }
//     printf("Length is: %d\n", len);

//     printf("Reversed string is: ");
//     for(i=0; i<=len; i++){
//         for(j=0; j<=len; j++){

//             rev[i] = str[len-i];
            
//         }
//         printf("%c",rev[i]);
//     }printf("\n");

// }

// void main(){
//     char str1[20], str2[] = "hello";

//     printf("\nEnter string 1: ");
//     gets(str1);

//     printf("\nstr1: %s\n",str1);
//     reverse(str1);

//     printf("\nstr2: %s\n",str2);
//     reverse(str2);
      
// }