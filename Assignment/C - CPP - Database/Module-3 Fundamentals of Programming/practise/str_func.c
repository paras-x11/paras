//string functions:

#include<stdio.h>
#include<string.h>

int length(char str[]){                    
    int len = 0;

    for(int i=0; str[i] != '\0'; i++){                   // find length without in-built function strlen();
        len++;
    }

    return len;
    // printf("\nLength of str is: %d", len);
}

void main(){
    char rev[20], str1[20], str2[20], str3[20], str[20] = "nayan";

    strrev(str);
    strcpy(rev,str);
    
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

    // printf("\nEnter string 1: ");
    // gets(str1);

    // printf("\nEnter string 2: ");
    // gets(str2);

    // printf("\nstr1: %s",str1);
    // printf("\nstr2: %s\n",str2);

    // printf("\nLength of str1 is: %d", length(str1));
    // printf("\nLength of str2 is: %d", length(str2));

    // printf("\nLength of str1 is: %d",strlen(str1));
    // printf("\nLength of str2 is: %d\n",strlen(str2));

    // printf("\nUPPER CASE str1: %s",strupr(str1));
    // printf("\nUPPER CASE str2: %s\n",strupr(str2));

    // printf("\nlower case str1: %s",strlwr(str1));
    // printf("\nlower case str2: %s\n",strlwr(str2));

    // printf("\nComparison if str1 > str2 strings: %d\n",strcmp(str1, str2));
    // printf("\nComparison if str2 > str1 strings: %d\n",strcmp(str2, str1));

    // printf("\nString reverse: \n");
    // printf("\nstr1: %s\n",strrev(str));
    
    
    
    // printf("\nstr1: %s\n",strrev(str1));
    // printf("\nstr2: %s\n",strrev(str2));



    // printf("\nString copy str3 = str1: %s",strcpy(str3,str1));

    // printf("\nString inside string: %s", strstr(str, "ll"));
    // printf("\nCharacter inside string: %s", strchr(str, "l"));

    // printf("\nString concatenate: %s", strcat(str1, str2));

    // printf("\nString set: %s", strset(str1, 'f'));

}