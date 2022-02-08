class SnapshotArray:

    def __init__(self, length: int):
        self.dic = collections.defaultdict(list)
        self.snapid = 0
        self.len = length

    def set(self, index: int, val: int) -> None:
        self.dic[self.snapid].append((index, val))

    def snap(self) -> int:
        ret = self.snapid
        self.snapid += 1
        return ret

    def get(self, index: int, snap_id: int) -> int:
        if index >= self.len:
            return -1
        for ops in reversed(range(snap_id+1)):
            for idx, val in self.dic[ops][::-1]:
                if idx == index:
                    return val
        return 0


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)