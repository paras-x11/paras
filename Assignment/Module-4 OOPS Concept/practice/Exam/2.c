// 2. wap to read and write data from the file.

#include <stdio.h>
#include <string.h>

int main(){
    FILE *fp;
    int i;
    char str1[5][20], str2[5][20];
    
    printf("Enter data for insert: \n");
    for(i=0; i<5; i++){
        gets(str1[i]);
    }

    fp = fopen("D:\\paras\\Assignment\\Module-4 OOPS Concept\\practice\\Exam\\file.txt", "w+");
    
    if(fp == NULL){
        printf("\nFile not created.");
    }
    else{
        printf("\nFile is created.");
    }

    if(strlen(str1) > 0){

        for(i=0; i<5; i++){
            fputs(str1[i], fp);
            fputs("\n", fp);
        }
    }

    printf("\nData is inserted");

    fclose(fp);


    fp = fopen("D:\\paras\\Assignment\\Module-4 OOPS Concept\\practice\\Exam\\file.txt", "r+");
    
    if(fp == NULL){
        printf("\nFile not existed.");
    }
    else{
        printf("\nData is: \n");
        while(fgets(str1,100,fp)!=NULL){
            printf("%s", str1);
                
        }
    }
    fclose(fp);
}