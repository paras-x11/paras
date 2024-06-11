 // 25. (1*1) + (2*2) + (3*3) + (4*4) + (5*5) + ... + (n*n) 

 #include<stdio.h>
 void main(){
     int n, sum=0, m=0;
    
    printf("\nEnter the number : ");
    scanf("%d",&n);

    for(int i=1; i<=n; i++){
        m = i * i;
        sum = sum + m;
    }

    printf("\nSum is: %d",sum);
    
 }