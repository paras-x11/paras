// 9. WAP to show difference between Structure and Union.

// Structure:

// #include<stdio.h>
// struct employee 
// {
//     int emp_no;
//     char emp_name[20];
//     char address[50];
//     int age;
// } e1;

// void main(){

//     printf("\nEnter employee no.: ");
//     scanf("%d",&e1.emp_no);

//     while ((getchar()) != '\n');
//     printf("\nEnter name: ");
//     gets(e1.emp_name);

//     printf("\nEnter address: ");
//     gets(e1.address);

//     printf("\nEnter age: ");
//     scanf("%d",&e1.age);

//     printf("\nDetails of Employee: ");
//     printf("\nEmployee Number: %d",e1.emp_no);
//     printf("\nEmployee Name: %s",e1.emp_name);
//     printf("\nEmployee address: %s",e1.address);
//     printf("\nEmployee age: %d",e1.age);
    
   
// }


// Union: 

#include<stdio.h>

union employee 
{
    int emp_no;
    int salary;    
    int age;
} e1;

void main(){

    printf("\nEnter employee no.: ");
    scanf("%d",&e1.emp_no);
    printf("\nEmployee Number: %d\n",e1.emp_no);


    printf("\nEnter salary: ");
    scanf("%d", &e1.salary);
    printf("\nEmployee salary: %d\n",e1.salary);


    printf("\nEnter age: ");
    scanf("%d",&e1.age);
    printf("\nEmployee age: %d\n",e1.age);


    printf("\nAfter entering all details: ");
    printf("\nEmployee Number: %d",e1.emp_no);
    printf("\nEmployee salary: %d",e1.salary);
    printf("\nEmployee age: %d",e1.age);
    
   
}