#include <stdio.h>
#include <stdlib.h>

char a[9] = {'1', '2', '3', '4', '5', '6', '7', '8', '9'};
void check(char, char);
void gameName() {
    printf("\n\t\t\t         TIC-TAC-TOE GAME\n");
}

void show() {
    printf("\n\n");
    printf("\t\t\t\t     |     |     \n");
    printf("\t\t\t\t  %c  |  %c  |  %c  \n", a[0], a[1], a[2]);
    printf("\t\t\t\t_____|_____|_____\n");
    printf("\t\t\t\t     |     |     \n");
    printf("\t\t\t\t  %c  |  %c  |  %c  \n", a[3], a[4], a[5]);
    printf("\t\t\t\t_____|_____|_____\n");
    printf("\t\t\t\t     |     |     \n");
    printf("\t\t\t\t  %c  |  %c  |  %c  \n", a[6], a[7], a[8]);
    printf("\t\t\t\t     |     |     \n");
}

void inputSymbol() {
    printf("\nPlayer 1 is: 'x'");
    printf("\nPlayer 2 is: '0'");
}

void start(char* pa) {
    printf("\nEnter who will start the game (1 for player 1, 2 for player 2): ");
    scanf(" %c", pa);
}

void play() {
    char p, s;
    printf("\nEnter position and symbol for the player: ");
    scanf(" %c %c", &p, &s);
    check(p, s);
}

void check(char P, char S) {
    int i;
    for(i = 0; i < 9; i++) {
        if(a[i] == P) {
            a[i] = S;
        }
    }
}

int end() {
    if((a[0] == 'x' && a[1] == 'x' && a[2] == 'x') ||
       (a[0] == 'x' && a[3] == 'x' && a[6] == 'x') ||
       (a[0] == 'x' && a[4] == 'x' && a[8] == 'x') ||
       (a[1] == 'x' && a[4] == 'x' && a[7] == 'x') ||
       (a[2] == 'x' && a[5] == 'x' && a[8] == 'x') ||
       (a[2] == 'x' && a[4] == 'x' && a[6] == 'x') ||
       (a[3] == 'x' && a[4] == 'x' && a[5] == 'x') ||
       (a[6] == 'x' && a[7] == 'x' && a[8] == 'x')) {
        return 100;
    }
    else if((a[0] == '0' && a[1] == '0' && a[2] == '0') ||
            (a[0] == '0' && a[3] == '0' && a[6] == '0') ||
            (a[0] == '0' && a[4] == '0' && a[8] == '0') ||
            (a[1] == '0' && a[4] == '0' && a[7] == '0') ||
            (a[2] == '0' && a[5] == '0' && a[8] == '0') ||
            (a[2] == '0' && a[4] == '0' && a[6] == '0') ||
            (a[3] == '0' && a[4] == '0' && a[5] == '0') ||
            (a[6] == '0' && a[7] == '0' && a[8] == '0')) {
        return 200;
    }
    else {
        return 300;
    }
}

int main() {
    char pa, ch;
    int k = 0;

    do {
    
        for(int i = 0; i < 9; i++) {
            a[i] = '1' + i;
        }

        system("cls");
        gameName();
        show();
        inputSymbol();
        start(&pa);

        while (1) {
            system("cls");
            gameName();
            show();
            play();
            k = end();

            if (k != 300) {
                break;
            }
        }

        system("cls");
        gameName();
        show();

        if (k == 100) {
            printf("\nPlayer 1 Wins.\n");
        } else if (k == 200) {
            printf("\nPlayer 2 Wins.\n");
        }

        printf("\nDo you want to play again ('y' for yes or 'n' for no): ");
        scanf(" %c", &ch);
        while ((getchar()) != '\n');

    } while (ch == 'y' || ch == 'Y');

    printf("\nExited.\n");
    return 0;
}
