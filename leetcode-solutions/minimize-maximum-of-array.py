class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        
        total = 0
        ans = 0
        length = len(nums)
        for ind in range(length):
            total += nums[ind]
            ans = max(ans,ceil(total/(ind+1)))
        
        return ans