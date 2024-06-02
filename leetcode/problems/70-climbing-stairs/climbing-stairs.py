class Solution:
    def climbStairsDP(self, n: int, dp) -> int:
        
        if n <=2:
            return n
        
        if dp[n]!=-1:
            return dp[n]

        dp[n] = self.climbStairsDP(n-1,dp)+self.climbStairsDP(n-2,dp)
        return dp[n]

    def climbStairs(self, n):

        return self.climbStairsDP(n,[-1]*(n+1))
