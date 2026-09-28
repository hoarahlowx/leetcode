#include <stdlib.h>
#include <string.h>

char* longestCommonPrefix(char** strs, int strsSize) {
    if (strsSize == 0) return "";

    int max_len = strlen(strs[0]);
    char* prefix = (char*)malloc((max_len + 1) * sizeof(char));

    for (int col = 0; col < max_len; col++) {
        char current_char = strs[0][col];

        for (int row = 1; row < strsSize; row++) {
            if (strs[row][col] == '\0' || strs[row][col] != current_char) {
                prefix[col] = '\0';
                return prefix;
            }
        }

        prefix[col] = current_char;
    }

    prefix[max_len] = '\0';
    return prefix;
}