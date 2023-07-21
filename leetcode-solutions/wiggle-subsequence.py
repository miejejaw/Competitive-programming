class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:

        self.memo = {}
        self.length = len(nums)
        res = self.helper(nums,0,True,nums[0])+1
        res = max(res,self.helper(nums,0,False,nums[0])+1)

        return res

    def helper(self, nums, ind, isUp, prev):
        if ind < self.length:       
            if (ind,isUp) not in self.memo:
                res = self.helper(nums,ind+1,isUp,nums[ind])
                if (isUp and nums[ind]>prev) or (not isUp and nums[ind]<prev):
                        res = max(res,self.helper(nums,ind+1,not isUp,nums[ind])+1)
                self.memo[(ind,isUp)] = res
            return self.memo[(ind,isUp)]
        return 0
        