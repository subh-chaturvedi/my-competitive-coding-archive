class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy = -1
        profit=0
        
        for i in range(len(prices)):
            if buy == -1:
                if i==(len(prices)-1) or prices[i]<prices[i+1]:
                    buy = prices[i]
                    # print(buy)
            else:
                if i==(len(prices)-1) or prices[i]>prices[i+1]:
                    profit += prices[i]-buy
                    # print(prices[i],profit)
                    buy=-1
        
        return profit
