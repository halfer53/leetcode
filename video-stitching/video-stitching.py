class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort()
        start, end = 0, 0
        i = ret = 0
        while start <= end:
            ret += 1
            newstart, newend = end + 1, end
            while i < len(clips) and start <= clips[i][0] <= end:
                newend = max(newend, clips[i][1])
                if newend >= time:
                    return ret
                i += 1
            start, end = newstart, newend
        return -1
        