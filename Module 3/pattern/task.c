//task 1:
//A
//* *
//B C D
//* * * *
//E F G H I

//task2:
//1
//2 3
//4 5 6
//7 8 9 10
//11 12 13 14 15

//task3:
//A
//B C
//D E F
//G H I J
//K L M N 0

//task4:
//*
//* *
//*   *
//*     *
//* * * * *

//task5:
// 1 2 3 4 5
//   1 2 3 4
//     1 2 3
//       1 2
//         1

//task6:
// A B C D E
// A B C D
// A B C
// A B
// A

//task7:
//EEEEE
//DDDD
//CCC
//BB
//A 

//task8:
//eeeee
// dddd
//  ccc
//   bb
//    a

//task9:
//5 5 5 5 5
//  4 4 4 4
//    3 3 3
//      2 2
//        1

//task10:
//1 2 3 4 5
//  2 3 4 5
//    3 4 5
//      4 5
//        5

//task 1:
//A
//* *
//B C D
//* * * *
//E F G H I

/*
#include<stdio.h>
void main(){
    int row,col;
    char ch = 'A';

    for ( row = 0; row <= 5; row++){
        for(col = 0; col<=row; col++){
            if(row%2==0){
                printf("%c ",ch++);
            }
            else{
                printf("* ");
            }
        }
    printf("\n");
    }
    
}*/

//task2:
//1
//2 3
//4 5 6
//7 8 9 10
//11 12 13 14 15
/*
#include<stdio.h>
void main(){
    int r, c, n=1;

    for(r=0; r<=5; r++){
        for(c=0; c<=r; c++){

            printf(" %d",n);
            n++;
        }
    printf("\n");
    }
}*/

//task3:
//A
//B C
//D E F
//G H I J
//K L M N 0

/*
#include<stdio.h>
void main(){
    int r, c;
    char ch='A';

    for(r=0; r<=5; r++){
        for(c=0; c<=r; c++){

            printf(" %c",ch);
            ch++;
        }
    printf("\n");
    }
   
}
*/

//task4:
//*
//* *
//*   *
//*     *
//* * * * *

/*
#include<stdio.h>
void main(){
    int r, c;

    for(r=0; r<=5; r++){
    
        for (c = 0; c<=r; c++){
        
            if(c==0||c==5||c==r||r==5){
                printf(" *");
            }
            else{
                printf("  ");
            }
        }
        printf("\n");
    }
}*/

