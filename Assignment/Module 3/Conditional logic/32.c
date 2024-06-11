/*32. Write a C program to input basic salary of an employee and calculateits 
Gross salary according to following: 
Basic Salary <= 10000 : HRA = 20%, DA = 80% 
Basic Salary <= 20000 : HRA = 25%, DA = 90% 
Basic Salary  > 20000 : HRA = 30%, DA = 95%      */

#include<stdio.h>
void main(){
    int basic_salary, hra, da, gross_salary;

    printf("\nEnter the basic salary: ");
    scanf("%d",&basic_salary);

    if((basic_salary > 0) && (basic_salary <= 10000)){

        hra = basic_salary * 0.20;
        da = basic_salary * 0.80;
        gross_salary = basic_salary + hra + da;
        printf("\nHRA = %d, DA = %d",hra,da);
        printf("\nGross salary is: %d",gross_salary);
    }

    else if((basic_salary > 10000) && (basic_salary <= 20000)){

        hra = basic_salary * 0.25;
        da = basic_salary * 0.90;
        gross_salary = basic_salary + hra + da;
        printf("\nHRA = %d, DA = %d",hra,da);
        printf("\nGross salary is: %d",gross_salary);
    }

    else if(basic_salary > 20000){

        hra = basic_salary * 0.30;
        da = basic_salary * 0.95;
        gross_salary = basic_salary + hra + da;
        printf("\nHRA = %d, DA = %d",hra,da);
        printf("\nGross salary is: %d",gross_salary);
    }

    else{
        printf("\nInvalid salary");
    }
    
}