class Solution:
    def f(self,n,dp):
        if n<=2:
            return dp[n]
        if dp[n]==-1:
            dp[n] = self.f(n-1,dp) + self.f(n-2,dp) + self.f(n-3,dp)
        
        # print(dp)
        return dp[n]

    def tribonacci(self, n: int) -> int:
    
        dp = [-1]*max(n+1,3)

        dp[0]=0
        dp[1]=1
        dp[2]=1

        return self.f(n,dp)

        
