class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        self.memo = {}
        return self.helper(root,False)

    def helper(self,curr,isTaken):
        if curr:
            if (curr,isTaken) not in self.memo:
                notTaken = self.helper(curr.left,False)
                notTaken += self.helper(curr.right,False)
                taken = 0
                if not isTaken:
                    taken = self.helper(curr.left,True)
                    taken += self.helper(curr.right,True)
                    taken += curr.val

                self.memo[(curr,isTaken)] = max(notTaken,taken)
            return self.memo[(curr,isTaken)]
        return 0


