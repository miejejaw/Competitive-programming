class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        self.ddp = {}
        return self.dp(s,0,len(s)-1) 

    def dp(self, s, left, right):
        if left < right:
            if (left,right) not in self.ddp:
                res = 0
                if s[left] == s[right]:
                    res = 2 +  max(res,self.dp(s,left+1,right-1))
                else:
                    res = max(res,self.dp(s,left+1,right))
                    res = max(res,self.dp(s,left,right-1))
                self.ddp[(left,right)] = res
            return self.ddp[(left,right)]
        return 1 if left==right else 0
