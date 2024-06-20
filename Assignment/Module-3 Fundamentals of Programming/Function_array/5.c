// 5. WAP to take two Array input from user and sort them in ascending or descending order as per user’s choice.

#include<stdio.h>
#include<stdlib.h>
void main(){
    int i, j, ch, a1[5], a2[5], temp;

    printf("\nEnter elements of array1: ");
    for(i=0; i<5; i++){
        scanf("%d",&a1[i]);
    }
    
    printf("\nEnter elements of array2: ");
    for(i=0; i<5; i++){
        scanf("%d",&a2[i]);
    }

    printf("\nElements of array1: ");
    for(i=0; i<5; i++){
        printf("%d\t",a1[i]);
    }

    printf("\nElements of array2: ");
    for(i=0; i<5; i++){
        printf("%d\t",a2[i]);
    }

    printf("\n");
    printf("\n(Enter 0 for exit.)");

    start:
    printf("\n");
    printf("\n--------------------------------------------------------");
    printf("\nEnter 1 for ascending or 2 for descending: ");
    scanf("%d",&ch);

    switch(ch){
        case 1:
            for(i=0; i<5; i++){
                for(j=0; j<5; j++){

                    if(a1[i] < a1[j]){
                        temp = a1[i];
                        a1[i] = a1[j];
                        a1[j] = temp;
                    }
                }
            }
            printf("\n-> acsending array1: ");
            for(i=0; i<5; i++){
                printf("\t%d",a1[i]);
            }

            printf("\n");
            for(i=0; i<5; i++){
                for(j=0; j<5; j++){

                    if(a2[i] < a2[j]){
                        temp = a2[i];
                        a2[i] = a2[j];
                        a2[j] = temp;
                    }
                }
            }
            printf("\n-> acsending array2: ");
            for(i=0; i<5; i++){
                printf("\t%d",a2[i]);
            }
        break;

        case 2:
            for(i=0; i<5; i++){
                for(j=0; j<5; j++){

                    if(a1[i] > a1[j]){
                        temp = a1[i];
                        a1[i] = a1[j];
                        a1[j] = temp;
                    }
                }
            }
            printf("\n-> descending array1: ");
            for(i=0; i<5; i++){
                printf("\t%d",a1[i]);
            }


            printf("\n");
            for(i=0; i<5; i++){
                for(j=0; j<5; j++){

                    if(a2[i] > a2[j]){
                        temp = a2[i];
                        a2[i] = a2[j];
                        a2[j] = temp;
                    }
                }
            }
            printf("\n-> descending array2: ");
            for(i=0; i<5; i++){
                printf("\t%d",a2[i]);
            }
        break;

        case 0: printf("\nExited.");
                exit(0);

        default: printf("\nEnter valid choice (1 or 2).");
        break;
    }
    goto start;
}

