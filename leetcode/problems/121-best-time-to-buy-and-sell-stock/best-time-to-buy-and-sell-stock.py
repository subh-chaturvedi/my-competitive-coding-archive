class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minP = prices[0]
        ans=0

        for i in prices:
            if i<=minP:
                minP=i
            else:
                ans=max(ans,i-minP)
        
        return ans
