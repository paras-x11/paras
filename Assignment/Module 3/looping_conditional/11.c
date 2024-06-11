//11. Accept 5 names from user at run time. 

#include<stdio.h>
void main(){
    char name[10];

    for(int i = 1 ; i <= 5 ; i++){
        
        printf("\nEnter name %d: ",i);
        scanf("%s",&name);
        gets(name);
    }
   
}