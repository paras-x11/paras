// Structure is a user define data-type.

#include<stdio.h>

struct student{
    int roll_no;
    char name[10];
    float marks;
} s1, s2;                                           // s1, s2 = structure variable.

void main(){

    // struct student s1, s2;                       // 2nd method of defining structure variable (in main func).

    printf("\nEnter details for student 1: \n");
    printf("\nEnter roll no.: ");
    scanf("%d",&s1.roll_no);

    while ((getchar()) != '\n');
    printf("\nEnter name: ");
    gets(s1.name);

    printf("\nEnter marks: ");
    scanf("%f",&s1.marks);

    printf("\nEnter details for student 2: \n");
    printf("\nEnter roll no.: ");
    scanf("%d",&s2.roll_no);

    while ((getchar()) != '\n');
    printf("\nEnter name: ");
    gets(s2.name);

    printf("\nEnter marks: ");
    scanf("%f",&s2.marks);

    printf("\nDetails of student 1: ");
    printf("\nRoll_no.: %d",s1.roll_no);
    printf("\nName.: %s",s1.name);
    printf("\nMarks.: %f\n",s1.marks);

    printf("\nDetails of student 2: ");
    printf("\nRoll_no.: %d",s2.roll_no);
    printf("\nName.: %s",s2.name);
    printf("\nMarks.: %f",s2.marks);

}