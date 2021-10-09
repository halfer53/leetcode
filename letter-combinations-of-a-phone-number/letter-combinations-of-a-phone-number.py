class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        if digits == '':
            return ''
        le = [letters[x] for x in digits]
        n = len(le)
        m = len(digits)
        # print(le)
        ret = []
        def dfs(track: List[str], path: List[str]):
            if len(path) == m:
                ret.append(''.join(path))
                return
            for i in range(len(track)):
                for j in range(len(track[i])):
                    dfs(track[i+1:], path + [track[i][j]])
        dfs(le, [])
        return ret