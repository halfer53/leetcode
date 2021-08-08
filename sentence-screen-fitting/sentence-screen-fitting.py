class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        s = ' '.join(sentence) + ' '
        length = len(s)
        start = 0
        for i in range(rows):
            start += cols
            if s[(start % length)] == ' ':
                start += 1
            else:
                while start and s[((start - 1) % length)]  != ' ':
                    start -= 1
        return start // length
        