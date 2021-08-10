class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        ops_reuse = 0
        ret = 0
        for num in target:
            if num > ops_reuse:
                ret += num - ops_reuse
                ops_reuse = num
            else:
                ops_reuse = num
        return ret