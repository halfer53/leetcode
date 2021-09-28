class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        nums = [0]
        for row in mat:
            row.sort()
        for row in mat:
            tmp = set()
            for i in nums:
                for x in row:
                    tmp.add(x + i)
                    if x + i > target:
                        break
            nums = tmp
        return min(map(lambda x: abs(target - x), nums))
            
        