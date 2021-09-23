class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        maxnum=0
        for i in range(-1,-len(prices),-1):


            if prices[i]>maxnum:
                prevmin=min(prices[:i])
                localmax=prices[i]-prevmin
                if localmax>profit:
                    profit=localmax
                maxnum=prices[i]

            
        return profit
