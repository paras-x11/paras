//M3_6 Find the Character Is Vowel or Not.

#include<stdio.h>
#include<ctype.h>

void main(){
    char ch;
    
    printf("Enter character: ");
    scanf("%c",&ch);
    
    if(!isalpha(ch)){
        printf("\ninvalid character");
    }
    
    else if((ch=='a') || (ch=='e') || (ch=='i') || (ch=='o') || (ch=='u')){
        printf("\n%c is vowel",ch);
    }
    
    else{
        printf("\n%c is not a vowel",ch);
    }
}
