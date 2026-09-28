int** largestLocal(int** grid, int gridSize, int* gridColSize, int* returnSize, int** returnColumnSizes) {
    *returnSize = gridSize - 2;
    *returnColumnSizes = (int*)malloc(*returnSize * sizeof(int));
    int** ans = (int**)malloc(*returnSize * sizeof(int*));

    for (int i = 0; i < *returnSize; i++){
        (*returnColumnSizes)[i] = *returnSize;
        ans[i] = (int*)malloc(*returnSize * sizeof(int));
        for (int j = 0; j < *returnSize; j++){
            int max_val = 0;
            for (int l = i; l < i + 3; l++){
                for (int r = j; r < j + 3; r++){
                    if (grid[l][r] > max_val){
                        max_val = grid[l][r];
                    }
                }
            }
            ans[i][j] = max_val;
        }
    }
    return ans;
}