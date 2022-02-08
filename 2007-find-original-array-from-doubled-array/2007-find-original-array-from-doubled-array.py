class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changedset = collections.Counter(changed)
        changed.sort()
        ret = []
        for idx, val in enumerate(changed):
            doubleval = val * 2
            if doubleval in changedset and changedset[val] > 0 and changedset[doubleval] > 0:
                if val == 0 and changedset[val] < 2:
                    continue
                changedset[val] -= 1
                changedset[doubleval] -= 1
                ret.append(val)
        if len(ret) * 2 == len(changed):
            return ret
        return []