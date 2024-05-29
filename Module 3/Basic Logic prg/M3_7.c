//M3_7 Find area of rectangle formula: A = w*l

#include <stdio.h>
void main() {
    int w, l , area;
    
    printf("\nEnter the width of rectangle: ");
    scanf("%d", &w);
    
    printf("\nEnter the length of rectangle: ");
    scanf("%d", &l);
    
    area = w * l;
    printf("\nArea of rectangle is: %d", area); 
}