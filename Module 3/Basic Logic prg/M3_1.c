//Module 3: 1. DIsplay Information USing printf

#include<stdio.h>
void main(){

    char name[30] = "paras rana";
    char birth_date[10] = "11-2-2004";
    int age = 20;
    char address[50] = "2/4624, sagrampura main road, surat";

    printf("\n");
    printf("INFORMATION\n");
    printf("------------------------\n");
    printf("your Name is: %s\n", name);
    printf("your Birth Date is: %s\n", birth_date);
    printf("your Age is: %d\n", age);
    printf("your Address is: %s\n", address);
}