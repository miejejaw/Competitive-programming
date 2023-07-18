class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        self.length = len(prices)
        self.memo = {}
        return self.helper(prices,False,0)

    def helper(self, prices, isBought, ind):
        if ind < self.length:
            if (ind,isBought) not in self.memo:
                if isBought:
                    selled = self.helper(prices,False,ind+2)+prices[ind]
                    notSelled = self.helper(prices,True,ind+1)
                    self.memo[(ind,isBought)] = max(selled,notSelled)
                else:
                    bought = self.helper(prices,True,ind+1)-prices[ind]
                    notBought = self.helper(prices,False,ind+1)
                    self.memo[(ind,isBought)] = max(bought,notBought)
            
            return self.memo[(ind,isBought)]
        return 0