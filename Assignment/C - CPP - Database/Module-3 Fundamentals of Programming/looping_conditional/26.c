// 26. (1)+ (1+2) + (1+2+3) + (1+2+3+4) + ... + (1+2+3+4+...+n).

 #include<stdio.h>
 void main(){
     int n, sum=0, inner_sum=0;

    printf("\nEnter the number : ");
    scanf("%d",&n);

    for(int i=1; i<=n; i++){
        
        inner_sum = inner_sum + i;

        sum = sum + inner_sum;

    }

    printf("\nOutput is: %d",sum); 
 }