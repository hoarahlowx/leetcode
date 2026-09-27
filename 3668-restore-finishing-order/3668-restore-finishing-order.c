int* recoverOrder(int* order, int orderSize, int* friends, int friendsSize, int* returnSize) {
    *returnSize = friendsSize;
    int *ans = malloc(friendsSize * sizeof(int));
    int c = 0;
    for (int i = 0; i < orderSize; i++){
        for (int j = 0; j < friendsSize; j++){
            if (order[i] == friends[j]){
                ans[c] = order[i];
                c++;
                break;
            }
        }
    }
    return ans;
}