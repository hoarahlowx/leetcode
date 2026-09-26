int* findDegrees(int** matrix, int matrixSize, int* matrixColSize, int* returnSize) {
    *returnSize = matrixSize;
    int* ans = (int*)calloc(matrixSize, sizeof(int));
    for (int i = 0; i < matrixSize; i++) {
        for (int j = 0; j < matrixColSize[i]; j++) {
            ans[i] += matrix[i][j];
        }
    }
    return ans;
}