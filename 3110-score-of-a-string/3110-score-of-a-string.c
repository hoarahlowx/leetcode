#include <stdlib.h>


int scoreOfString(char* s) {
    int ans = 0;
    for (int i = 0; s[i + 1] != '\0'; i++){
        ans += abs(s[i] - s[i + 1]);
    }
    return ans;
}