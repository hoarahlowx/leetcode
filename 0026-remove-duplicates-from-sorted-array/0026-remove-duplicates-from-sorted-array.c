int removeDuplicates(int* nums, int numsSize) {
    int l = 0;
    int r = 1;
    while (r < numsSize)
    {
        if (nums[l] == nums[r]){
            nums[r] = '_';
        }
        else{
            l += 1;
            nums[l] = nums[r];
        }
        r += 1;
    }
    return l + 1;
}