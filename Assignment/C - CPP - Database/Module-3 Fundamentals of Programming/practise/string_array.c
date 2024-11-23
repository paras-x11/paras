// 12. WAP to accept 5 students name and store it in array

#include<stdio.h>
void main(){
    int i;
    char s_name[5][50];

    // This declares a 2D array of characters. 
    // It can be visualized as an array of 5 rows and 50 columns. 
    // Each row can hold a string of up to 49 characters plus the null terminator ('\0').

    printf("\nEnter 5 students name. \n");
    for(i=0; i<5; i++){
        printf("\nEnter name %i: ",i+1);
        fgets(s_name[i], sizeof(s_name[i]), stdin);    
        // it reads a full line of input, including spaces, until a newline or the maximum size is reached.
        // scanf("%s",&s_name[i]);   //it takes space as new line.
    }

    for(i=0; i<5; i++){
        printf("\nName %d: %s",i+1, s_name[i]);
    }
}