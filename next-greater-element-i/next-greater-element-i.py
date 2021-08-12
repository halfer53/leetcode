class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapping = dict()
        stack = []
        for val in nums2:
            while len(stack) and stack[-1] <= val:
                last = stack.pop()
                mapping[last] = val
            stack.append(val)
        result = []
        for val in nums1:
            if val not in mapping:
                result.append(-1)
            else:
                result.append(mapping[val])
        return result