// 16. Accept 5 numbers from user and perform sum of array

 #include<stdio.h>
 void main(){
     int arr[5], i, sum=0;

    printf("\nEnter 5 numbers in array: \n");
    for(i=0; i<5; i++){
        scanf("%d",&arr[i]);
    }

    printf("\nYour array is: \n");
    for(i=0; i<5; i++){
        printf("%d\t",arr[i]);
    }

    for ( i = 0; i < 5; i++){
        sum += arr[i]; 
    }

    printf("\nSum of array is: %d",sum);
}