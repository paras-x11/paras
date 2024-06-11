#include<stdio.h>
#include<stdlib.h>

int show(int a, char ch, int b, int r){
    printf("\n%d %c %d = %d\n",a,ch,b,r);
}

int sum(int a, int b){
    int r;
    printf("\n-> Enter number 1: ");
    scanf("%d",&a);

    printf("\n-> Enter number 2: ");
    scanf("%d",&b);

    r = a + b;
    show(a,'+',b,r);
}

int sub(int a, int b){
    int r;
    printf("\n-> Enter number 1: ");
    scanf("%d",&a);

    printf("\n-> Enter number 2: ");
    scanf("%d",&b);

    r = a - b;
    show(a,'-',b,r);
}

int multi(int a, int b){
    int r;
    printf("\n-> Enter number 1: ");
    scanf("%d",&a);

    printf("\n-> Enter number 2: ");
    scanf("%d",&b);

    r = a * b;
    show(a,'*',b,r);
}

int division(int a, int b){
    int r;
    printf("\n-> Enter number 1: ");
    scanf("%d",&a);

    printf("\n-> Enter number 2: ");
    scanf("%d",&b);

    r = a / b;
    show(a,'/',b,r);
}
    
    
void main(){
    int x, y, choice;

    // start:
    do{
    printf("\n-----------------------");
    printf("\n1 -> sum.");
    printf("\n2 -> substraction.");
    printf("\n3 -> multiply.");
    printf("\n4 -> division.");
    printf("\n0 -> exit.");
    printf("\n-----------------------\n");

    printf("\nEnter choice: ");
    scanf("%d",&choice);

    switch (choice)
    {
    case 1: sum(x, y);
        // goto start;
        break;

    case 2: sub(x, y);
        // goto start;
        break;

    case 3: multi(x, y);
        // goto start;
        break;

    case 4: division(x, y);
        // goto start;
        break;

    case 0: printf("\nExited.");
        exit(0);
        break;
    
    default: printf("\nInvalid choice.. \n");
        // goto start;
        break;
    }
    }while( choice != 0);
   
}

