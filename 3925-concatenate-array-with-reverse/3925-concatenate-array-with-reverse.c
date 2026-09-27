int* concatWithReverse(int* nums, int numsSize, int* returnSize) {
    *returnSize = numsSize * 2;
    int *ans = malloc(*returnSize * sizeof(int));
    for (int i = 0; i < numsSize; i++){
        ans[i] = nums[i];
        ans[*returnSize - 1 - i] = nums[i];
    }
    return ans;
}