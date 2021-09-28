class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        dic = collections.defaultdict(list)
        for i in range(m):
            for j in range(n):
                dic[i+j].append(mat[i][j])
        ret = []
        for entry in dic.items():
            if entry[0] % 2 == 0:
                ret += entry[1][::-1]
            else:
                ret += entry[1][:]
        return ret