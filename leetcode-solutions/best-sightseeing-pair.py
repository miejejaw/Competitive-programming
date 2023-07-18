class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:

        length = len(values)
        ans,prev = 0,values[0]-1
        for ind in range(1,length):
            ans = max(ans,prev+values[ind])
            prev = max(prev,values[ind]) - 1
        
        return ans