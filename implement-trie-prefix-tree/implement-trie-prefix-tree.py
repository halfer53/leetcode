class TrieNode:
    def __init__(self):
        self.nodes = collections.defaultdict(TrieNode)
        self.isend = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            node = node.nodes[c]
        node.isend = True

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c in node.nodes:
                node = node.nodes[c]
            else:
                return False
        return node.isend
                

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if c in node.nodes:
                node = node.nodes[c]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)