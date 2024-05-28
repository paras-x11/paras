//M3_18 calculate persons annual salary.

#include <stdio.h>
void main() {
    int m_salary,a_salary;
    
    printf("Enter the monthly salary: ");
    scanf("%d",&m_salary);
    
    a_salary = m_salary*12;
    
    printf("\nperson's annual salary is: %d",a_salary);
}