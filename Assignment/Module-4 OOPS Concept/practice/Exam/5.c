// 5. WAP c prg giving employee number, name , basic salary, insert the data into external file and give file name emp.txt

#include <stdio.h>

void main() {
    
    FILE *fp;
    int n, s;
    char name[50];

    char str1[50] = "Enter Employee Number: ";
    char str2[50] = "Enter Employee Name: ";
    char str3[50] = "Enter Employee Salary: ";
    
    printf("Enter Employee Number: ");
    scanf("%d", &n);

    printf("Enter Employee Name: ");
    scanf("%s", &name);

    printf("Enter Employee Salary: ");
    scanf("%d", &s);

    fp = fopen("D:\\paras\\Assignment\\Module-4 OOPS Concept\\practice\\Exam\\emp.txt", "w+");
    
    if(fp == NULL){
        printf("\nFile not created.");
    }
    else{
        printf("\nFile is created.");
    }

    // if(strlen(name) > 0 && n!=NULL && s!=NULL){
        fputs(str1, fp);

        fprintf(fp, "%d", n);
        // fputc(n, fp);
        // fscanf(fp, n);
        fputs("\n", fp);  

        fputs(str2, fp);
        fputs(name, fp);        
        fputs("\n", fp);  
        
        fputs(str3, fp);
        fprintf(fp, "%d", s); 
       
    // }

    // else{
    //     printf("Data is not inserted.");
    // }

    printf("\nData is inserted");

    fclose(fp);
    
}