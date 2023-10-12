class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        length = len(gas)
        idx = -1
        for i in range(length):
            gas[i] -= cost[i]
            if gas[i]>=0 and idx == -1:
                idx = i
            
        if sum(gas)<0: return -1
        
        total = 0       
        for i in range(idx,length):
            total += gas[i]
            if total >= 0 and idx == -1:
                idx = i
            elif total < 0:
                idx = -1
                total = 0
                      
        return idx

