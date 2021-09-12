class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        vals = []
        for w, h in rectangles:
            vals.append(w/h)
        count = collections.Counter(vals)
        ret = 0
        for val, freq in count.items():
            if freq > 1:
                i = freq - 1
                ret += i*(i+1) // 2
        return ret