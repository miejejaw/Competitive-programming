class TrieNode:
    def __init__(self):
        self.children = {}
        self.index = -1
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word,idx):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        node.index = idx

    def search(self, pref, suff):
        node = self.root
        ch = ""
        for char in pref:
            if char not in node.children:
                return -1
            ch += char
            node = node.children[char]
        return self.backtrack(node,suff,ch)

    def backtrack(self, node, suff, word):
        idx = -1
        for char in node.children:
            idx = max(idx,self.backtrack(node.children[char],suff,word+char))

        if node.is_end_of_word and word.endswith(suff):
            idx = max(idx,node.index)
        return idx

class WordFilter:

    def __init__(self, words: List[str]):
        self.root = Trie()
        for idx,word in enumerate(words):
            self.root.insert(word,idx)

    def f(self, pref: str, suff: str) -> int:
        return self.root.search(pref,suff)


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)