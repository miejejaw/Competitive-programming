class Solution:
    def findDuplicateSubtrees(self, root) -> List[Optional[TreeNode]]:
        self.ans = []
        self.visited = defaultdict(int)
        self.dfs(root)
        return self.ans

    def dfs(self, curr):
        if curr:
            res = ":"
            res += self.dfs(curr.left)
            res += str(curr.val)
            res += self.dfs(curr.right)

            if self.visited[res] == 1:
                self.ans.append(curr)
            self.visited[res] += 1
            return res
        return ":"
        