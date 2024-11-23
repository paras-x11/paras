#include<stdio.h>
void main(){
    int arr[5]={10,20,30,40,50};
    int n;

    for(int i=0; i<5; i++){
        printf("arr[%d] = %d\n",i, arr[i]);
    }
    
    printf("\nEnter index: ");
    scanf("%d",&n);

    printf("\nElement at index %d is: %d", n, arr[n]);
}