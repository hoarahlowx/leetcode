int* maxDepthAfterSplit(char* seq, int* returnSize) {
    *returnSize = strlen(seq);
    int* ans = malloc(*returnSize * sizeof(int));
    int open = 0;
    int close = 0;

    for (int i = 0; i < *returnSize; i++){
        if (seq[i] == '('){
            ans[i] = open;
            close = open;
            open = (open + 1) % 2;
        }
        else{
            ans[i] = close;
            open = close;
            close = (close + 1) % 2;
        }
    }
    return ans;
}