class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:

        length = len(costs)
        arr = [(costs[i][0] - costs[i][1], i) for i in range(length)]
        
        arr.sort()
        total = 0
        
        for i in range(length):
            
            if i < length//2:
                total += costs[arr[i][1]][0]
            else:
                total += costs[arr[i][1]][1]
        
        return total