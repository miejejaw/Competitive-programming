class Solution:
    def flipEquiv(self, root1, root2) -> bool:
        return self.dfs(root1,root2)
    
    def dfs(self, curr1, curr2):

        if curr1 and curr2:
            if curr1.val != curr2.val:
                return False
            
            res = self.dfs(curr1.left,curr2.left)
            res = res and self.dfs(curr1.right,curr2.right)

            res2 = self.dfs(curr1.left,curr2.right)
            res2 = res2 and self.dfs(curr1.right,curr2.left)
            return True if res or res2 else False
        
        return curr1 == curr2
