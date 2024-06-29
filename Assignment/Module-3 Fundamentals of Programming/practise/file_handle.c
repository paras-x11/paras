#include <stdio.h>
void main(){
    FILE *fp;
    char str[5][50], str1[100];
    
    printf("\nEnter Data to input: ");
    for(int i=0; i<5; i++){
        gets(str[i]);
    }

    fp = fopen("D:\\paras\\Assignment\\Module-3 Fundamentals of Programming\\practise\\demo.txt", "w+");

    if( fp == NULL){
        printf("\nFile not created.");
    }
    else{
        printf("\nFile created.");
    }

    if(strlen(str) > 0){

        for(int i=0; i<5; i++){
            fputs(str[i], fp);
            fputs("\n", fp);
        }
    }

    printf("\nData is inserted.");
    fclose(fp);

    fp = fopen("D:\\paras\\Assignment\\Module-3 Fundamentals of Programming\\practise\\demo.txt", "r+");

    if(fp==NULL){
        printf("File not created.");
    }
    else{
        while( fgets(str1, 100, fp) != NULL){
            printf("\n %s", str1);
        }
    }    
}