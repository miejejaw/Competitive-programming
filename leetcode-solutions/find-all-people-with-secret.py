class Union:
    
    def __init__(self, size, ind):
        self.rep = [i for i in range(size)]
        self.rep[ind] = 0
        
    def find(self,val):
        if self.rep[val] == val:
            return val
        
        self.rep[val] = self.find(self.rep[val])
        return self.rep[val]
        
    def union(self,x, y):
        x = self.find(x)
        y = self.find(y)

        if x > y:
            x, y = y, x

        self.rep[y] = x
            

class Solution:
    def findAllPeople(self, n, meetings, firstPerson) -> List[int]:
        
        size = len(meetings)
        New_Union = Union(n, firstPerson)
        meetings.sort(key = lambda s : s[2])       
        
        left = right = 0
        ans = set({0,firstPerson})

        while right < size:
            
            while right < size and  meetings[left][2] == meetings[right][2]:
                New_Union.union(meetings[right][0], meetings[right][1])
                right += 1
                
            while left < right:
                x = New_Union.find(meetings[left][0])
                y = New_Union.find(meetings[left][1])
                
                if x and y:
                    New_Union.rep[meetings[left][0]] = meetings[left][0]
                    New_Union.rep[meetings[left][1]] = meetings[left][1] 
                else:
                    ans.add(meetings[left][0])
                    ans.add(meetings[left][1])

                left += 1     
        return list(ans)