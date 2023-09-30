class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEOW = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEOW = True

    def search(self, node, word, idx, n):
        if idx < n:
            if word[idx] in node.children:
                return self.search(node.children[word[idx]],word,idx+1,n)
            elif word[idx] != "." and word[idx] not in node.children:
                return False
            else: 
                for char in node.children:
                    if self.search(node.children[char],word,idx+1,n):
                        return True
                return False
        return node.isEOW


class WordDictionary:

    def __init__(self):
        self.NewTrie = Trie()

    def addWord(self, word: str) -> None:
        self.NewTrie.insert(word)

    def search(self, word: str) -> bool:
        root = self.NewTrie.root
        return self.NewTrie.search(root,word,0,len(word))


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
