class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        
        length = len(scores)
        arr = [[ages[idx],scores[idx],idx] for idx in range(length)]
        arr.sort()
        ans = arr[0][1]

        for idx in range(1,length):
            _max = 0
            i = arr[idx][2]
            for j in range(idx-1,-1,-1):
                if scores[i] >= scores[arr[j][2]] or arr[idx][2] == arr[j][2]:
                    _max = max(_max,arr[j][1])
            arr[idx][1] += _max
            ans = max(ans,arr[idx][1])
        
        return ans Best-Team-With-No-Conflicts.py
