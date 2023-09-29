class Solution:
    def minSteps(self, n: int) -> int:
        
        memo = [0]*(n+1)
        
        for num in range(2,n+1):
            memo[num] = num
            for i in range(num-1,1,-1):
                if num%i == 0:
                    memo[num] = memo[i] + (num//i)
                    break

        return memo[n]
