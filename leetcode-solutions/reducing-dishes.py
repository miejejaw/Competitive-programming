class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        
        satisfaction.sort()
        length = len(satisfaction)

        total = 0
        prefix = 0
        for idx in range(length-1,-1,-1):
            prefix += satisfaction[idx]
            if prefix <= 0:
                break
            total += prefix
        
        return total