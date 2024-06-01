//M3_8. WAP to accept the height of a person in centimeters and categorize the person according to their height
//if height is less than 150 centimeter, then the person is dwarf and if the height is between 151 to 165 then it is categorized as average and if the height is between 165 to 175 then it is categorized as tall.

#include<stdio.h>
void main (){
    int h;
    
    printf("Enter height in cm: ");
    scanf("%d",&h);
    
    if(h <= 150){
        printf("\nPerson is dwarf");
    }
    
    else if((h >= 151) && (h <= 165)){
        printf("\nPerson is average");
    }
    
    else {
        printf("\nPerson is tall");
    }
}
