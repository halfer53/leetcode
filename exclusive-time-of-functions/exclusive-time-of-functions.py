class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        logs = [x.split(':') for x in logs]
        ret = [0] * n
        stack = []
        for fid, action, time in logs:
            fid = int(fid)
            time = int(time)
            print(fid, action, time, stack)
            if action == 'start':
                if stack and stack[-1][1] >= 0:
                    pfid, ptime = stack.pop()
                    ret[pfid] += time - ptime
                    stack.append([pfid, -1])
                stack.append([fid, time])
            else:
                pfid, ptime = stack.pop()
                if pfid == fid:
                    if ptime >= 0:
                        ret[pfid] += time - ptime + 1
                if stack and stack[-1][1] == -1:
                    stack[-1][1] = time + 1
        return ret