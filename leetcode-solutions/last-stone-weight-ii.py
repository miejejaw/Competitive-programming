class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        self.length = len(stones)
        self.avg = ceil(sum(stones)/2)
        self.memo = {}
        self.ans = 0
        self.dfs(stones,0,0)
        return abs(sum(stones)-(2*self.ans))
    
    def dfs(self, stones, idx, num):
        if idx < self.length:
            if num > self.avg: return
            if (idx,num) not in self.memo: 
                self.dfs(stones, idx+1, num)
                self.dfs(stones, idx+1, num+stones[idx])
                self.memo[(idx,num)] = num
            return 
        if self.ans<num <= self.avg:
            self.ans = num
        self.memo[(idx,num)] = num





