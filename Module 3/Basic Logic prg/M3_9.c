//M3_9 Find circumference of triangle formula: c = a+b+c.

#include <stdio.h>
void main() {
    int a, b, c, circumference;
    
    printf("\nEnter the length of boundaries: ");
    printf("\nEnter a: ");
    scanf("%d", &a);
    
    printf("\nEnter b: ");
    scanf("%d", &b);
    
    printf("\nEnter c: ");
    scanf("%d", &c);
    
    circumference = a+b+c;

    printf("\nCircumference of triangle is: %d", circumference);
}