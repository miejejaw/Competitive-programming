class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:

        self.length = len(prices)
        self.memo = {}
        return self.helper(prices,fee,False,0)

    def helper(self, prices, fee, isBought, ind):
        if ind < self.length:
            if (ind,isBought) not in self.memo:
                if isBought:
                    selled = self.helper(prices,fee,False,ind+1)+prices[ind]
                    notSelled = self.helper(prices,fee,True,ind+1)
                    self.memo[(ind,isBought)] = max(selled,notSelled)
                else:
                    bought = self.helper(prices,fee,True,ind+1)-prices[ind]-fee
                    notBought = self.helper(prices,fee,False,ind+1)
                    self.memo[(ind,isBought)] = max(bought,notBought)
            
            return self.memo[(ind,isBought)]
        return 0