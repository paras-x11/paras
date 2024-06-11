// #include<stdio.h>
// void main(){
//     int i,n,number[5],fact[5];

//     for(n=0; n<5; n++){
//         printf("\nEnter number %d: ",n+1);
//         scanf("%d",&number[n]);
//     }  

//     for(n=0; n<5; n++){
//         fact[n] = 1;

//         for(i=1; i<=number[n]; i++){
//             fact[n] = fact[n] * i;
            
//         }
//                 printf("\nFactorial of %d is: %d",number[n],fact[n]);  

//     }
// }

// #include<stdio.h>

// void main(){
//     int row, col, n=1;

//     for(row=0; row<5; row++){

//         for(col=0; col<10; col++){
//             printf("%02d\t", n);
//             n++;
//         }
//         printf("\n");
//     }  
// }
/*
#include<stdio.h>

void main() {
    int r, c, s;

    for(r = 1; r <= 5; r++) { 

        
        for(c = 1; c <=r; c++) {
            printf("* ");
        }

        printf("\n");
    }

    for(int i = 6; i <= 10; i++) { 

        for(int j = 0; j >=i; j--) {

            printf("* ");
        }

        printf("\n");
    }
}*/

// *
// *  *
// *  *  *
// *  *  *  *
// *  *  *  *  *
// *  *  *  *  *  *
// *  *  *  *  *
// *  *  *  *
// *  *  * 
// *  *
// *   //anu reverse
/*
#include<stdio.h>
void main() {
    int r, c, s;

    for(r = 5; r >= 0; r--) { 
        for(s=0; s<r; s++){
            printf("  ");
        }

        for(c = 5; c >= r; c--) {
            printf("* ");
        }

        printf("\n");
    }

    for(r = 0; r < 5; r++) { 
        for(s=0; s<=r; s++){
            printf("  ");
        }
        
        for(c=5; c>r; c-- ){
            printf("* ");
        }

        printf("\n");
    }   
}
*/

/*#include<stdio.h>
void main(){
    int n, f, l;

    printf("enter:");
    scanf("%d",&n);

    l=n%10;

    for(; f>=10 ; n=n/10)
    {
       f = n; 
    }
    printf("%d",f+l);
   
}*/

//22. Accept 3 numbers from user using while loop and check each numbers palindrome.
/*
#include<stdio.h>
void main(){
    int num[3], rev[3], rem, temp;

  
    for(int n=0; n<3; n++){
        printf("\nEnter number: ");
        scanf("%d", &num[n]);
        temp = num[n];
        rev[n] = 0;
        
       
        while(temp > 0){
            rem = temp % 10;
            rev[n] = rev[n]*10 + rem;
            temp = temp / 10;
        }
    }

  
    for(int n=0; n<3; n++){
        printf("\nNumber: %d, Reversed: %d", num[n], rev[n]);
        if(num[n] == rev[n]){
            printf("\n%d is Palindrome.", num[n]);
        }
        else{
            printf("\n%d is Not Palindrome.", num[n]);
        } 
    }
}*/

//28. 1 2 3 6 9 18 27 54... 
// a   b   c 
// 1   2   3       4       5        6        7        8           <-- place
// 1 + 2 = 3 * 2 = 6 + 3 = 9 * 2 = 18 + 9 = 27 * 2 = 54....... 

#include<stdio.h>
void main(){
    int n, a=1, b=2, c=0;

    printf("\nEnter number: ");
    scanf("%d", &n);
    printf("%d %d ",a,b);

    for(int i=3; i<=n; i++){
        if(i%2==0){
            c = b *2;
        }
        else{
            c= a + b;
        }
        a=b;
        b=c;
    printf("%d ",c);
    }
   
}