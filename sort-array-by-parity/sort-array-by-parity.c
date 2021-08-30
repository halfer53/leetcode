

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* sortArrayByParity(int* nums, int numsSize, int* returnSize){
    int left = 0, right = numsSize - 1;
    int val, tmp;
    while (left <= right){
        val = nums[left];
        if (val % 2 != 0){
            tmp = nums[right];
            nums[right] = nums[left];
            nums[left] = tmp;
        }
        if (nums[left] % 2 == 0){
            left += 1;
        }else{
            right -= 1;
        }
    }
    *returnSize = numsSize;
    return nums;
}