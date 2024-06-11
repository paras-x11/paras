//28. 1 2 3 6 9 18 27 54... 
// a   b   c 
// 1   2   3       4       5        6        7        8           <-- place
// 1 + 2 = 3 * 2 = 6 + 3 = 9 * 2 = 18 + 9 = 27 * 2 = 54....... 

#include<stdio.h>
void main(){
    int a=1, b=2, n, c=0;
    printf("\nEnter the number : ");
    scanf("%d",&n);

    printf("%d ",a);
    printf("%d ",b);

    for(int i = 3; i<=n; i++){

        if(i%2==0){
            c = b * 2;
        }
        else{
            c = a + b;
        }

        a = b;
        b = c;
        
        printf("%d ",c);
    }
   
}