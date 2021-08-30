

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int cmp(const void*a, const void* b){
    return (*(int*)a) - (*(int*)b);
}
int* intersection(int* nums1, int nums1Size, int* nums2, int nums2Size, int* returnSize){
    int l1 = 0, l2 = 0;
    int size = nums1Size < nums2Size ? nums1Size : nums2Size;
    int *ret = malloc(size * sizeof(int));
    int *p = ret;
    
    qsort(nums1, nums1Size, sizeof(int), cmp);
    qsort(nums2, nums2Size, sizeof(int), cmp);
    while (l1 < nums1Size && l2 < nums2Size){
        if(nums1[l1] == nums2[l2]){
            int *added = ret;
            bool duplicate = false;
            while (added <= p){
                if(*added++ == nums1[l1]){
                    duplicate = true;
                    break;
                }
            }
            if(!duplicate)
                *p++ = nums1[l1];
        }
        if (nums1[l1] >= nums2[l2]){
            l2 += 1;
        }else{
            l1 += 1;
        }
    }
    *returnSize = p - ret;
    return ret;
    
}