//M3_11 Find the circumference of square formula: C=4*l.

#include<stdio.h>
void main() {
    int l , circumference;
    
    printf("\nEnter the length of square: ");
    scanf("%d", &l);
    
    circumference = 4 * l;

    printf("\nCircumference of square is: %d", circumference);
}