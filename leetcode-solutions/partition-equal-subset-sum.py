class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summ = sum(nums)
        if summ%2:
            return False
        self.cache = {}
        
        return self.check(nums, 0, summ//2)

    def check(self, nums, i, target):
        if target >= 0 and i < len(nums):
            if nums[i] == target: return True
            
            if (i, target) in self.cache:
                return self.cache[(i, target)]
            
            result = self.check(nums, i+1, target - nums[i]) or self.check(nums, i+1, target)
            self.cache[(i, target)] = result
            return result
        return False