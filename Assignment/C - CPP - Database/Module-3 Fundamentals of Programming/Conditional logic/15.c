/*
15. Write a C program to determine eligibility for admission to a professional course based on the following criteria 
Eligibility Criteria : 
Marks in Maths >=65 and Marks in Phy >=55 and Marks in Chem>=50 and Total in all three subject >=190 or Total in Maths and Physics >=140 
--------------------------------------
Input the marks obtained in Mathematics :72 
Input the marks obtained in Physics :65 
Input the marks obtained in Chemistry :51  

Total marks of Maths, Physics and Chemistry : 188 Total marks of Maths and Physics : 137 The candidate is not eligible. */

#include<stdio.h>
void main(){
    int m, p, c, sum, mp;

    printf("Enter marks of maths: ");
    scanf("%d",&m);
    
    printf("Enter marks of physics: ");
    scanf("%d",&p);
    
    printf("Enter marks of chemistry: ");
    scanf("%d",&c);

    mp = m + p;

    sum = m + p + c;
    
    if ( ((m >= 65) && (p >= 55) && (c >= 50) && (sum >= 190)) || (mp >= 140) )
    {
        printf("\n--------------------------");
        printf("\nThe candidate is eligible");
        printf("\nTotal is: %d",sum);
        printf("\nTotal in maths and physics is: %d",mp);
    }

    else
    {
        printf("\n--------------------------");
        printf("\ncandidate is not eligible");
        printf("\nTotal is: %d",sum);
        printf("\nTotal in maths and physics is: %d",mp);
    }
    
    
}