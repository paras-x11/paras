// Write a program of structure employee that provides the following 
// a. information -print and display empno, empname, address and age 

#include<stdio.h>
struct employee 
{
    int emp_no;
    char emp_name[20];
    char address[50];
    int age;
} e1;

void main(){

    printf("\nEnter employee no.: ");
    scanf("%d",&e1.emp_no);

    while ((getchar()) != '\n');
    printf("\nEnter name: ");
    gets(e1.emp_name);

    printf("\nEnter address: ");
    gets(e1.address);

    printf("\nEnter age: ");
    scanf("%d",&e1.age);

    printf("\nDetails of Employee: ");
    printf("\nEmployee Number: %d",e1.emp_no);
    printf("\nEmployee Name: %s",e1.emp_name);
    printf("\nEmployee address: %s",e1.address);
    printf("\nEmployee age: %d",e1.age);
    
   
}