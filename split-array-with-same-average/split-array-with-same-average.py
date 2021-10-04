class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        n = len(nums)
        m = int(n / 2)
        totalSum = sum(nums)   
        isPossible = False 
        for i in range(1, m+1):
            if totalSum * i % n == 0:
                isPossible = True
                break 
        if not isPossible:
            return False 
        
        sums = [set() for _ in range(m+1)]
        sums[0].add(0)  
        for num in nums:
            for i in range(m, 0, -1):
                for t in sums[i-1]:
                    sums[i].add(t + num)
        for i in range(1, m+1):
            if totalSum * i % n == 0 and int(totalSum * i /n) in sums[i]:
                return True
        return False
            