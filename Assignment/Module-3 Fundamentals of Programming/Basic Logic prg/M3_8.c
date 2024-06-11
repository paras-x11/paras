// M3_8 Find circumference of rectangle formula: C = 2l + 2w or 2(l+w).

#include <stdio.h>
void main() {
    int l, w, circumference;
    
    printf("\nEnter the length of rectangle: ");
    scanf("%d", &l);
    
    printf("\nEnter the width of rectangle: ");
    scanf("%d", &w);
    
    circumference = 2*(l+w); //2l + 2w

    printf("\nCircumference of rectangle is: %d", circumference);
}