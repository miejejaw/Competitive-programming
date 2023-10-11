class Solution:
    def lowestCommonAncestor(self, root, p, q) -> 'TreeNode':
        self.ans = None
        return self.dfs(root,p,q)

    def dfs(self, curr, p, q):
        if curr:
            if p==curr or q==curr:
                return curr
            left = self.dfs(curr.left,p,q)
            right = self.dfs(curr.right,p,q)

            if left and right:
                return curr
            elif left:
                return left
            elif right:
                return right                

        return None