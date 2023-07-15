class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:

        self.length = len(arr)
        self.dp = defaultdict(int)
        self.ans = 0
        self.helper(arr,difference,0)
        return self.ans

    def helper(self, arr, difference, ind):
        if ind < self.length:
            self.helper(arr,difference,ind+1)
            self.dp[arr[ind]] = 1 + self.dp[arr[ind]+difference]
            self.ans = max(self.ans,self.dp[arr[ind]])