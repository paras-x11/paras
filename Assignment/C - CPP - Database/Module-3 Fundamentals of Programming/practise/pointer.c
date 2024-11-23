// Pointers:

// #include <stdio.h>
// void main(){
//     int i = 10;
//     int *ptr;
//     ptr = &i;

//     printf("\n i = %d", i);
//     printf("\n adress of i is: %d", ptr);
//     printf("\n value at address %d is: %d", ptr, *ptr);
// }


// 1. Write program to make an addition of two number using pointer.

// #include <stdio.h>
// void main(){
//     int a, b, c;
//     int *p1, *p2;

//     p1 = &a;
//     p2 = &b;

//     printf("\nEnter a: ");
//     scanf("%d", &a);

//     printf("\nEnter b: ");
//     scanf("%d", &b);

//     printf("\n a = %d", a);
//     printf("\n adress of a is: %d\n", p1);

//     printf("\n b = %d", b);
//     printf("\n adress of b is: %d\n", p2);

//     c = *p1 + *p2;
//     // printf("\n %d + %d = %d", a, b, c);
    
//     printf("\n %d + %d = %d", a, b, *p1 + *p2);
// }



// 2. Write a program to sort the numbers using pointer and functions.

// #include <stdio.h>
// void main(){
//     int i, j, temp, n=5;
//     int arr[5] = {25, 18, 30, 28, 45};
//     int *p, *p1, *p2;

//     p1 = &arr[0];
//     p2 = &arr[4];

//     printf("\n adress of %d is: %d\n", *p1, p1);
//     printf("\n adress of %d is: %d\n", *p2, p2);

//     // p = &arr will cause a compilation error &arr gives the address of the entire array, not the address of the first element.

//     p = arr;                        // Equivalent to p = &arr[0]

//     for(i=0; i<n; i++){
        
//         for(j=0; j<n; j++){

//             if(*(p+i) < *(p+j)){                       // < or >

//                 temp = *(p+i);
//                 *(p+i) = *(p+j);
//                 *(p+j) = temp;
//             }
//         }
//     }

//     for(i=0; i<n; i++){
//         printf("%d\t", *(p+i));
//     }
// }


// 3. C Program for Reverse a String Using Pointer.


// 4. Write a program to concatenate the two string using pointer. 


// 5. Write a C Program to Compare Two Strings Using Pointers.


// 6. Open a File(open a Program Itself) Using Pointer.


// 7. swap values using pointer.

// #include <stdio.h>

// int main() {
//     int a = 10, b = 20;
//     int *p1 = &a, *p2 = &b;

//     printf("Before swapping:\n");
//     printf("a = %d, address of a: %p\n", a, p1);
//     printf("b = %d, address of b: %p\n", b, p2);

//     int temp = *p1;
//     *p1 = *p2;
//     *p2 = temp;

//     printf("\nAfter swapping:\n");
//     printf("a = %d, address of a: %p\n", a, p1);
//     printf("b = %d, address of b: %p\n", b, p2);

//     return 0;
// }
