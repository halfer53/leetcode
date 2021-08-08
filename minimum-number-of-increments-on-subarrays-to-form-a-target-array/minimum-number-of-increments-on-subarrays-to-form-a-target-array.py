class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        ops_reuse = total = target[0]
        for i in range(1, len(target)):
            num = target[i]
            if num < ops_reuse:
                ops_reuse = num
            else:
                total += num - ops_reuse
                ops_reuse = num
        return total