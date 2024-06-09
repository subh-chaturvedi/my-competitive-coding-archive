class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        amt=amount
        small = min(coins)
        def f(amt,dp):
            if amt<small:
                return 2**32
            if amt in coins:
                return 1
            
            if dp[amt]==-1:
                mini=2**30
                for i in coins:
                    mini=min(mini, 1 + f(amt-i,dp))
                dp[amt] = mini
            
            return dp[amt]
        
        dp = [-1]*(amt+1)

        if amt==0:
            return 0

        x = f(amt,dp)

        if x>2**20:
            return -1
        else:
            return x



