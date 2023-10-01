class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if not node.children[char].is_end_of_word:
                return False
            node = node.children[char]
        return True

class Solution:
    def longestWord(self, words: List[str]) -> str:

        NewTrie = Trie()

        for word in words:
            NewTrie.insert(word)

        ans = ""
        for word in words:
           if NewTrie.search(word):
               if len(ans) < len(word) or (len(ans)==len(word) and word<ans):
                        ans = word

        return ans
