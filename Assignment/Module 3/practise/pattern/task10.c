//task10:
//1 2 3 4 5
//  2 3 4 5
//    3 4 5
//      4 5
//        5



// #include<stdio.h>
// void main(){
//     int r, c, s, n=1;

//     for(r=0; r<=5; r++){
//         n= r+1;
//         for(s=0; s<r; s++){
//             printf("  ");
//         }

//         for(c=5; c>=r; c--){
//             printf("%d ",n++);
//         }
//         n=1;

//     printf("\n");
//     }
    
// }



#include<stdio.h>
void main(){
    int r, c, s;

    for(r=6; r>=0; r--){
        
        for(s=6; s>r; s--){
            printf(" ");
        }

        for(c=r; c>=1; c--){
            printf("%d ",c);
        }
    
    printf("\n");
    }
}
