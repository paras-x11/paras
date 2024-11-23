//M3_20 Accept monthly salary from the user and deduct 10% insurance premium, 10% loan installment. find out of remaining salary.

#include<stdio.h>
void main(){
    int m_salary, net_salary;
    int ip, li;

    printf("Enter the monthly salary: ");
    scanf("%d",&m_salary);

    ip = m_salary * 0.1;

    li = m_salary * 0.1;

    net_salary = m_salary - (ip + li);

    printf("\ninsurance premium is: %d",ip);
    printf("\nloan installment is: %d",li);
    printf("\nnet slary is: %d",net_salary);
}