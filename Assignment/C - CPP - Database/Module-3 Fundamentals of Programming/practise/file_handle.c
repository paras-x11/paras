#include <stdio.h>
void main(){
    FILE *fp;
    char str[5][50], str1[100], append[2][100];
    
    // printf("\nEnter Data to input: ");
    // for(int i=0; i<5; i++){
    //     gets(str[i]);
    // }

    // fp = fopen("D:\\paras\\Assignment\\Module-3 Fundamentals of Programming\\practise\\file_handle.txt", "w+");

    // if( fp == NULL){
    //     printf("\n\nFile not created.");
    // }
    // else{
    //     printf("\n\nFile created.");
    // }

    // if(strlen(str) > 0){

    //     for(int i=0; i<5; i++){
    //         fputs(str[i], fp);
    //         fputs("\n", fp);
    //     }
    // }

    // printf("\n\nData is inserted.");
    // fclose(fp);

    fp = fopen("D:\\paras\\Assignment\\Module-3 Fundamentals of Programming\\practise\\file_handle.txt", "r+");

    if(fp==NULL){
        printf("\n\nFile is not exist.");
    }
    else{
        printf("\n\nData is: \n");
        while( fgets(str1, 100, fp) != NULL){
            printf("\n %s", str1);
        }
    }    
    fclose(fp);

    printf("\nEnter Data to input: ");
    for(int i=0; i<2; i++){
        gets(append[i]);
    }

    fp = fopen("D:\\paras\\Assignment\\Module-3 Fundamentals of Programming\\practise\\file_handle.txt", "a+");

    if( fp == NULL){
        printf("\n\nFile not created.");
    }
    else{
        printf("\n\nFile created.");
    }

    if(strlen(append) > 0){

        for(int i=0; i<2; i++){
            fputs(append[i], fp);
            fputs("\n", fp);
        }
    }

    printf("\n\nData is appended.");
    fclose(fp);

    fp = fopen("D:\\paras\\Assignment\\Module-3 Fundamentals of Programming\\practise\\file_handle.txt", "r+");

    if(fp==NULL){
        printf("\n\nFile is not exist.");
    }
    else{
        printf("\n\nUpdated Data is: \n");
        while( fgets(str1, 100, fp) != NULL){
            printf("\n %s", str1);
        }
    }    
    fclose(fp);



}