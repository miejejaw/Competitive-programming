class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def dfs(curr, num):
    if curr:
        if curr.val < num:
            if not curr.right:
                curr.right = Node(num)
            else:
                dfs(curr.right,num)
        else:
            if not curr.left:
                curr.left = Node(num)
            else:
                dfs(curr.left,num)
        

nums = list(map(int,input().split()))
root = Node(nums[0])

for i in range(1,len(nums)):
    dfs(root,nums[i])

def dfs_in(curr):
    if curr:
        dfs_in(curr.left)
        print(curr.val,end=" ")
        dfs_in(curr.right)

dfs_in(root)