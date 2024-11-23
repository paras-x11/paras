//M3_10 Find the area of rectangular prism formula: A=2(wl+hl+hw).

#include <stdio.h>
void main() {
    int l, w, h, sum, area;
    
    printf("\nEnter length: ");
    scanf("%d", &l);
    
    printf("\nEnter width: ");
    scanf("%d", &w);
    
    printf("\nEnter height: ");
    scanf("%d", &h);
    
    area =2 * (w*l + h*l + l*w); //20+24+20
    
    printf("\nArea of rectangular prism is: %d", area);
}