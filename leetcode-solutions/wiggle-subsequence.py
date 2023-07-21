class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:

        self.memo = {}
        self.length = len(nums)
        res = self.helper(nums,0,True)+1
        res = max(res,self.helper(nums,0,False)+1)
        return res

    def helper(self, nums, ind, isUp):
        if ind < self.length:       
            if (ind,isUp) not in self.memo:
                res = self.helper(nums,ind+1,isUp)
                if ind and ((isUp and nums[ind]>nums[ind-1]) or (not isUp and nums[ind]<nums[ind-1])):
                        res = max(res,self.helper(nums,ind+1,not isUp)+1)
                self.memo[(ind,isUp)] = res
            return self.memo[(ind,isUp)]
        return 0
