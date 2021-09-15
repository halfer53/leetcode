class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        glasses = [[0.0] * 100 for _ in range(100)]
        glasses[0][0] = poured
        for i in range(query_row):
            for j in range(i+1):
                q = (glasses[i][j] - 1.0) / 2.0
                if q > 0:
                    glasses[i+1][j] += q
                    glasses[i+1][j+1] += q
        return min(1.0, glasses[query_row][query_glass])
                    
                    