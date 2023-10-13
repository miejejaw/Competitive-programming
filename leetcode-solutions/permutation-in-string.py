class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        w1 = Counter(s1)
        temp = defaultdict(int)
        beg = 0
        length = len(s2)

        for end in range(length):
            if s2[end] not in w1:
                while beg < end:
                    temp[s2[beg]] -= 1
                    if temp[s2[beg]] == 0:
                        temp.pop(s2[beg])
                    
                    if temp == w1: return True
                    beg += 1
                beg += 1
            else:
                temp[s2[end]] += 1
                while beg < end and temp[s2[end]]>w1[s2[end]]:
                    temp[s2[beg]] -= 1
                    if temp[s2[beg]] == 0:
                        temp.pop(s2[beg])
                    
                    beg += 1

            if temp == w1: return True
            
        return False