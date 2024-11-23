 // 15. Store 5 numbers in array and sort it in ascending order 

 #include<stdio.h>
 void main(){
     int arr[5], i, temp;

    printf("\nEnter 5 numbers in array: \n");
    for(i=0; i<5; i++){
        scanf("%d",&arr[i]);
    }

    printf("\nYour array is: \n");
    for(i=0; i<5; i++){
        printf("%d\t",arr[i]);
    }

    for ( i = 0; i < 5; i++){
        for(int j = 0; j < 5; j++){

            if(arr[i] < arr[j]){
                
                temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }

    printf("\nArray in ascending order: \n");
    for(i=0; i<5; i++){
        printf("%d\t",arr[i]);
    }  
}