class Solution:
    def reorderSpaces(self, text: str) -> str:
        prev = None
        i = 0
        n = len(text)
        letters = []
        spaces = 0
        while i < n:
            if text[i].isalpha():
                if prev is None:
                    prev = i
            else:
                if prev is not None:
                    letters.append(text[prev:i])
                    prev = None
                spaces += 1
            i += 1
        if prev is not None:
            letters.append(text[prev:n])
        if len(letters) == 1:
            return letters[0] + ' ' * spaces
        div = len(letters) - 1
        even = spaces // div
        return (' ' * even).join(letters) + (spaces % div) * ' '