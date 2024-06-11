//M3_12 ccept number of students from user. i need to give 5 apples to each student. how many apples are reqiured?

#include <stdio.h>
void main() {
    int n, apples;
    printf("Enter the number of students: ");
    scanf("%d",&n);
    
    apples = n * 5;
    
    printf("\nyou need %d apples for %d students",apples,n);
}