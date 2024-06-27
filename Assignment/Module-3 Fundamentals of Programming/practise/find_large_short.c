#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main() {
    char str[1000], largest[50] = "", smallest[50] = "", word[50];
    int i = 0, j = 0;
    
    printf("Enter a string: ");
    fgets(str, sizeof(str), stdin);
    
    // Remove trailing newline from fgets
    // str[strcspn(str, "\n")] = 0;
    
    int len = strlen(str);

    // Initialize largest and smallest with the first word
    while (i < len) {
        // Extracting each word from the sentence
        while (i < len && !isspace(str[i])) {
            word[j++] = str[i++];
        }
        word[j] = '\0'; // Null-terminate the word

        // Compare current word with largest and smallest
        if (strlen(word) > strlen(largest)) {
            strcpy(largest, word);
        }
        if (strlen(smallest) == 0 || strlen(word) < strlen(smallest)) {
            strcpy(smallest, word);
        }

        // Reset word index for next word
        j = 0;
        i++;
    }
    
    printf("Largest word: %s\n", largest);
    printf("Smallest word: %s\n", smallest);
    
    return 0;
}
