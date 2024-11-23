// Write a program of structure employee that provides the following:
// b. Write a program of structure for five employee that provides the following information -print and display empno, empname, address and age

#include<stdio.h>
struct employee
{
    int emp_no[5];
    char emp_name[5][20];
    char address[5][50];
    int age[5];
} e1;

void main(){
    int i;

    for(i=0; i<5; i++){

        printf("\nEnter Details For Employee %d: ",i+1);
        printf("\nEnter employee no.: ");
        scanf("%d",&e1.emp_no[i]);

        while ((getchar()) != '\n');
        printf("\nEnter name: ");
        scanf("%s", &e1.emp_name[i]);

        printf("\nEnter address: ");
        scanf("%s", &e1.address[i]);

        printf("\nEnter age: ");
        scanf("%d",&e1.age[i]);
    }

    for(i=0; i<5; i++){

        printf("\nDetails of Employee %d: ",i+1);
        printf("\n Number: %d",e1.emp_no[i]);
        printf("\n Name: %s",e1.emp_name[i]);
        printf("\n Address: %s",e1.address[i]);
        printf("\n Age: %d\n",e1.age[i]);
    }
   
}