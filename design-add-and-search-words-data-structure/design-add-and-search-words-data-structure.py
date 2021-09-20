class TrieNode:
    def __init__(self):
        self.nodes = collections.defaultdict(TrieNode)
        self.isend = False
        
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            curr = curr.nodes[c]
        curr.isend = True

    def search(self, word: str) -> bool:
        def dfs(i, curr) -> bool:
            if i >= len(word):
                if curr and curr.isend:
                    return True
                return False
            if word[i] in curr.nodes:
                return dfs(i+1, curr.nodes[word[i]])
            ret = False
            if word[i] == '.':
                for c, child in curr.nodes.items():
                    ret = ret or dfs(i+1, child)
                return ret
            return False
        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)