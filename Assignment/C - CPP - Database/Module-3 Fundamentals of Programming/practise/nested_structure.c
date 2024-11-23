#include <stdio.h>

struct employee{
    int e_id;
    float salary;

    struct department
    {
        int dept_id;
        char dept_name[20];
    } dept;                                 // nested structure variable always here.
    
};

void main(){

    struct employee e1, e2, e3;

    printf("Enter emp_id: ");
    scanf("%d", &e1.e_id);

    printf("\nEnter salary: ");
    scanf("%02f", &e1.salary);

    printf("\nEnter department id: ");
    scanf("%d", e1.dept.dept_id);

    printf("\nEnter department name: ");
    scanf("%s", e1.dept.dept_name);

    printf("\n\nDetails of employee 1: \n");
    printf("\nEmp_id: %d", e1.e_id);
    printf("\nSalary: %f", e1.salary);
    printf("\nDepartment id: %d", e1.dept.dept_id);
    printf("\nDepartment name: %s", e1.dept.dept_name);


    
   
}