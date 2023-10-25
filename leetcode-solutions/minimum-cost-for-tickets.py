class Solution:
    def mincostTickets(self, days, costs) -> int:
        length = days[-1]+1
        memo = [0]*length
        i = 0

        for idx in range(1,length):
            if days[i] == idx:
                res = costs[0] + memo[max(0,idx-1)]
                res = min(res, costs[1] + memo[max(0,idx-7)])
                res = min(res, costs[2] + memo[max(0,idx-30)])

                memo[idx] = res
                i += 1
            else:
                memo[idx] = memo[idx-1]

        return memo[-1]