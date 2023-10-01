class TrieNode:
    def __init__(self):
        self.children = {}
        self.val = 0
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, value):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        node.val = value
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return 0
            node = node.children[char]
        return self.find_sum(node)

    def find_sum(self, node):   
        if node:
            total = node.val
            for char in node.children:
                total += self.find_sum(node.children[char])
    
            return total
        return 0

class MapSum:

    def __init__(self):
        self.root = Trie()

    def insert(self, key: str, val: int) -> None:
        self.root.insert(key,val)

    def sum(self, prefix: str) -> int:
       return self.root.search(prefix)
