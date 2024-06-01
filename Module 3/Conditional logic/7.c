//M3_7 Accept marks from user and check pass or fail.

#include<stdio.h>
void main(){
    int m;
    
    printf("Enter marks :");
    scanf("%d",&m);
    
    if(m >= 33){
        printf("\nPASS");
    }
    else{
        printf("\nFAIL");
    }
}