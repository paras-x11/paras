// task 15:
// 2. wap to accept 2 number & find the GCD using loop of 2 numbers.

//        2 |24            2 | 36                               2 | 24 | 36
//        2 |12            2 | 18                               2 | 12 | 18
//        2 | 6            3 |  9                               2 |  6 |  9
//        3 | 3            3 |  3                               3 |  3 |  9
//          | 1              |  1                               3 |  1 |  3
//                                                                |    |  1

// GCD of 24 and 36 is 2 × 2 × 3 = 12               // LCM of 24 and 36 is 2 x 2 x 2 x 3 x 3 = 72

// GCD (a,b) = (a*b) / lcm(a,b);                    // LCM (a,b) = |a*b| / GCD(a,b);#include <stdio.h>

#include <stdio.h>
int main() {
    int a, b, lcm, max;

    printf("Enter two numbers: ");
    scanf("%d %d", &a, &b);

    // max = (num1 > num2) ? num1 : num2;                       // Start with the maximum of the two numbers
    lcm = (a > b) ? a : b;

    while (1) {                                                 // Increment lcm until it is divisible by both num1 and num2
        if (lcm % a == 0 && lcm % b == 0) {
            // lcm = max;
            break;
        }
        // max++;
        lcm++;
    }

    printf("LCM of %d and %d is %d\n", a, b, lcm);

    return 0;
}