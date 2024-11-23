// task 15:
//3. insert an element at specific position in array.

#include<stdio.h> 
void main(){
    int n, i, pos, val;

    printf("Enter the number of elements in the array: ");
    scanf("%d", &n);

    int arr[n+1];

    for(i=0; i<n; i++){
        printf("\nEnter element  at position %d: ",i);
        scanf("%d",&arr[i]);
    }

    printf("\nAt Position:\t");
    for(i=0; i<n; i++){
        printf("%d\t",i);
    }

    printf("\nElements are\t");
    for(i=0; i<n; i++){
        printf("%d\t",arr[i]);
    }

    printf("\n\nEnter the position you want to insert an element: ");
    scanf("%d",&pos);

    if(pos>=0 && pos<=n){
        printf("\nEnter the value you want to insert: ");
        scanf("%d",&val);

        for(i=n; i>pos; i--){
            arr[i]=arr[i-1];                //arr[i]=arr[i]; and remove n++; for replace the element.
        }

        arr[pos]=val;

        n++;

        printf("\nAt Position:\t");
        for(i=0; i<n; i++){
            printf("%d\t",i);
        }

        printf("\nElements are\t");
        for(i=0; i<n; i++){
            printf("%d\t",arr[i]);
        }
    }
    else{
        printf("\nEnter valid position.");
    }
}


