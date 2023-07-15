class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:

        dp = defaultdict(int)
        ans = 0
        for num in arr:
            dp[num] = 1 + dp[num-difference]
            ans = max(ans,dp[num])
        
        return ans