class Codec:
    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        ret = ['CODE']
        for s in strs:
            ret.append(hex(len(s))[2:].zfill(2))
            for c in s:
                ret.append(hex(ord(c))[2:])
        # print(ret)
        return ''.join(ret)

    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        ret = []
        if 'CODE' == s[:4]:
            i = 4
            n = len(s)
            while i < n:
                strlen = int(s[i:i+2], 16)
                i += 2
                m = i + strlen * 2
                ret.append(bytearray.fromhex(s[i:m]).decode())
                i = m
        # print(ret)
        return ret
                    


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))