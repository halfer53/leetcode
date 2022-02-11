class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ret = []
        stack = []
        i = 0
        n = len(words)
        while i < n:
            curr = 0
            j = i
            while j < n and ( (curr == 0 )
                             or (len(words[j]) + curr + 1 <= maxWidth)):
                stack.append(words[j])
                if curr > 0:
                    curr += 1
                curr += len(words[j])
                j += 1
            totallength = sum([ len(x) for x in stack])
            spaces = maxWidth - totallength
            if len(stack) == 1:
                line = stack[0] + ' ' * (maxWidth - len(stack[0]))
            elif j >= n:
                line = ' '.join(stack)
                line = line + ' ' * (maxWidth - len(line))
            else:
                spacesbetween = len(stack) - 1
                filling = ' ' * (spaces // spacesbetween)
                line = filling.join(stack)
                remain = spaces % spacesbetween
                chars = list(line)
                k = 0
                while remain != 0 :
                    while k < len(chars) and chars[k] != ' ':
                        k += 1
                    chars.insert(k, ' ')
                    while k < len(chars) and chars[k] == ' ':
                        k += 1
                    remain -= 1
                line = ''.join(chars)
                        
            ret.append(line)
            stack = []
            i = j
        return ret
            
            