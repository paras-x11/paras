//M3_26 Convert temperature Fahrenheit to Celsius.

#include<stdio.h>
void main(){
   float f, c;
   
   printf("Enter Fahrenheit: ");
   scanf("%f",&f);

   c = (f - 32)*5/9;
   
   printf("Celsius: %f ", c);
}