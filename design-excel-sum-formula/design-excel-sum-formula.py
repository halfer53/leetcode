class Excel:

    def __init__(self, height: int, width: str):
        self.sheet = [[{'val': 0, 'sum': None} for i in range(ord(width) - ord('A') + 1)] for j in range(height)]

    def set(self, row: int, column: str, val: int) -> None:
        ref = self.sheet[row-1][ord(column) - ord('A')]
        ref['val'] = val
        ref['sum'] = None

    def get(self, row: int, column: str) -> int:
        ref = self.sheet[row-1][ord(column) - ord('A')]
        if ref['sum'] is None:
            return ref['val']
        return sum(self.get(*pos) * ref['sum'][pos] for pos in ref['sum'])

    def sum(self, row: int, column: str, numbers: List[str]) -> int:
        ref = self.sheet[row-1][ord(column) - ord('A')]
        li = self.parse(numbers)
        ref['sum'] = li
        ref['val'] = 0
        return self.get(row, column)
        
    def parse(self, numbers: List[str]) -> List[object]:
        ret = collections.Counter()
        for num in numbers:
            r1, r2 = num.split(':')[0], num.split(':')[1] if ':' in num else num
            print(num, r1, r2)
            for i in range(int(r1[1:]), int(r2[1:]) + 1):
                for j in range(ord(r1[0]), ord(r2[0]) + 1):
                    ret[(i, chr(j))] += 1
        return ret


# Your Excel object will be instantiated and called as such:
# obj = Excel(height, width)
# obj.set(row,column,val)
# param_2 = obj.get(row,column)
# param_3 = obj.sum(row,column,numbers)