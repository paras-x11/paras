//27. 1/2 - 2/3 + 3/4 - 4/5 + 5/6 ........... n 
#include<stdio.h>
void main(){
    float n, d=0, sum=0;

    printf("\nEnter the number : ");
    scanf("%f",&n);

    for(int i=1; i<=n; i++){
        
        if(i % 2 == 0){

            sum -= (float)i / (i+1);
        }
        else{
            
            sum += (float)i / (i+1);      // 1/2 + 2/3 + 3/4 + 4/5 + 5/6 ........... n
        }
    }

    printf("\nSum is: %.2f",sum); 
}


