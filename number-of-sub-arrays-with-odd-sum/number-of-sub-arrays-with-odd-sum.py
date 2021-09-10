class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        odd = [0] * n
        even = [0] * n
        if arr[0] % 2 == 0:
            even[0] = 1
        else:
            odd[0] = 1
        for i in range(1, n):
            if arr[i] % 2 == 0:
                even[i] = even[i-1] + 1
                odd[i] = odd[i-1]
            else:
                odd[i] = even[i-1] + 1
                even[i] = odd[i-1]
        ret = sum(odd)
        return ret % (pow(10,9) + 7)