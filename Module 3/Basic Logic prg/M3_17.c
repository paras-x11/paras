//M3_17 calculate person's insurance premium based on salary.

#include <stdio.h>
void main() {
    int ip,salary,pr;
    
    printf("Enter the salary: ");
    scanf("%d",&salary);
    
    printf("\nEnter the premium rate: ");
    scanf("%d",&pr);
    
    ip = salary*pr/100;
    
    printf("\nperson's insurance premium based on salary is: %d",ip);
}