class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.ans = 0
        self.seen = defaultdict(int)
        self.seen[0] = 1
        self.dfs(root,0,targetSum)
        return self.ans
    
    def dfs(self,curr,prefix,target):
        if curr:
            prefix += curr.val
            if prefix-target in  self.seen:
                self.ans +=  self.seen[prefix-target]

            self.seen[prefix] += 1
            self.dfs(curr.left,prefix,target)
            self.dfs(curr.right,prefix,target)
            self.seen[prefix] -= 1
            