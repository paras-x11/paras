#include<stdio.h>
void main(){
    int i, n;

    printf("\nEnter number: ");
    scanf("%d",&n);

    for(i=2; i<=n/2; i++){

        if(n%i==0){
            break;
            goto label;
        }
    }

    label:
    if(i>n/2){
        printf("\nNumber is prime.");
    }

    else{
        printf("\nNumber is not prime.");

    }

}