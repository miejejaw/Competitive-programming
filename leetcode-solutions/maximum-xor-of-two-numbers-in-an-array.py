class Trie:
    def __init__(self):
        self.root = {}
    
    def insert(self, word, num): 
        node = self.root

        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node["num"] = num 
    
    def search(self, word, num):
        
        node = self.root
        for char in word:
            temp = str(1-int(char))
            if temp in node:
                node = node[temp] 
            else:
                node = node[char] 
        return node["num"] ^ num

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
  
        trie = Trie()

        for num in nums:
            binary = bin(num)[2:].zfill(31)
            trie.insert(binary,num)
        
        ans = 0
        for num in nums:
            binary = bin(num)[2:].zfill(31)
            ans = max(ans,trie.search(binary,num))
            
        return ans 
        