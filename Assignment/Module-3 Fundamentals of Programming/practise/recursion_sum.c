#include<stdio.h>

int sum (int n){

    if(n>0){

        n=n+sum(n-1);
        return n;
    }
    else{
        return 0;                //if there is no statement in body then u can return 0;
    }
}

int main(){
    int num;

    printf("\nenter number: ");
    scanf("%d", &num);

printf("\nAddition= %d", sum(num));

}