int reverseDegree(char* s) {
    int ans = 0;
    for (int i = 0; s[i]; i++){
        int pos = i + 1;
        int rev_alph = 'z' - s[i] + 1;
        ans += pos * rev_alph;
    }
    return ans;
}